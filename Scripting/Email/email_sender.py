import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path    # or os.path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Mad Max'
email['to'] = 'sajib@gmail.com'
email['subject'] = 'Hello new python dev!'
email.set_content(html.substitute({'name': 'Sajib'}), 'html')
# You can use plain text content like email.set_content('hola py dev')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('Your_mail_here', 'Your_Pass_here')
  smtp.send_message(email)
  print('all good dev!')