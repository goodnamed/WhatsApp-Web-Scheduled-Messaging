import gspread


def get_information():
    gc = gspread.oauth()
    sh = gc.open_by_url("https://docs.google.com/spreadsheets/d/1KJESAHGnXXOjj60g0qC-7J1Ih9mZs0GgmZc1-F4qLlg/edit?gid=0#gid=0")
    worksheet = sh.sheet1

    all_values = worksheet.get_all_values()

    information = all_values
    return information


