# WhatsApp-Web-Scheduled-Messaging
A python script to sending WhatsApp messages and images to individuals or groups on a schedule. The needed information needed is read from a google sheet.



## Google Sheet Columns:
  Chat Name
  
  Message Text Content
  
  Image Name
  
  Time to send


## Chat Name
  This is the name of the WhatsApp chat you have saved, it can be a group chat or an individual.
  The name given on the google sheet has to exactly match the name of the WhatsApp chat.


## Message Text Content
  This is the content of the text message you send to the chat.
  It can be left empty if you attach an image


## Image Name
  This is the name of the image file that is sent to the chat.
  It can be left empty if you have message content, it can also be attached to a text message.
  The image to be sent must be downloaded and kept in the images folder.


## Time to send
  This is the date that the message is scheduled to send. It should be in the format:
  "YYYY-MM-DD HH:MM"
  If no time is specified, the message is sentimmediately.



This uses WhatsApp web, hence the user should run this script once and scan the QR code on Whatsapp Web. From thereon, the program will work as intended.


  
