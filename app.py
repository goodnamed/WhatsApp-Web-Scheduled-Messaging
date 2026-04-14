from playwright.sync_api import sync_playwright
import time
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import googlesheet
import os


WHATSAPP_WEB_URL = "https://web.whatsapp.com/"
PROFILE_DIR = "whatsapp_profile"


def open_whatsapp(): #Opens whatsapp
    p = sync_playwright().start()
    browser = p.chromium.launch_persistent_context(
        user_data_dir=PROFILE_DIR,
        headless=False,
        viewport={"width": 1280, "height": 700},
    )

    page = browser.pages[0] if browser.pages else browser.new_page()
    page.goto(WHATSAPP_WEB_URL, wait_until="domcontentloaded")

    return p, browser, page


def send_message(page, group_name: str, message: str, image_path: str = None) -> None:
    searchbar = page.get_by_role("textbox")
    searchbar.fill(group_name)


    page.locator(f'span[title="{group_name}"]').first.click()

    if image_path:
        with page.expect_file_chooser() as fc_info:
            page.get_by_role("button", name="Attach").click()
            page.get_by_text("Photos & videos", exact=True).click()

        file_menu = fc_info.value
        file_menu.set_files(os.path.join("images", image_path))

        caption_box = page.locator('div[contenteditable="true"][role="textbox"][aria-label="Type a message"]:visible').first

        if message:
            caption_box.click()
            caption_box.fill(message)

        caption_box.press("Enter")

        caption_box.wait_for(state="hidden", timeout=15000)

        print(f"Image sent to {group_name}.")
        return

    
    message_box = page.locator('div[contenteditable="true"][role="textbox"]').last
    message_box.click()
    message_box.fill(message)
    message_box.press("Enter")


    print("Message sent.")


def scheduled_job(group_name: str, message: str, image_path: str = None):
    p, browser, page = open_whatsapp()
    try:
        send_message(page, group_name, message, image_path)
        time.sleep(2)
    except:
        pass
    finally:
        browser.close()
        p.stop()

if __name__ == "__main__":
    messages_to_send = googlesheet.get_information()
    scheduler = BlockingScheduler()

    for info in messages_to_send:
        group = info[0]
        message = info[1]   
        image = info[2]
        date = info[3]

        if(date):
            run_time = datetime.strptime(date, "%Y-%m-%d %H:%M")
            scheduler.add_job(scheduled_job, trigger="date", run_date = run_time, args=[group, message, image])
        else:
            scheduled_job(group, message, image)


    
    scheduler.start()