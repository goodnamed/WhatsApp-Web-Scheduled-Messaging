# Setup Guide

## 1. Clone the Repository

```bash
git clone https://github.com/goodnamed/WhatsApp-Web-Scheduled-Messaging.git
cd WhatsApp-Web-Scheduled-Messaging
```


## 2. Install Dependencies

```
pip install -r requirements.txt
```


## 3. Install Playwright Browsers

```
playwright install
```

## 4. Prepare Your Google Sheet

Your sheet must contain the following columns:

Chat Name
Message Text Content
Image Name
Time to Send



6. Run the Script
```
python main.py
```