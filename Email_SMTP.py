import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def Send_Email_Settings(Email_Send_From, Email_From_Password, Email_Send_To, Email_Subject, Email_Compose):
	msg = MIMEMultipart()
	msg['From'] = Email_Send_From
	msg['To'] = Email_Send_To
	msg['Subject'] = Email_Subject

	msg.attach(MIMEText(Email_Compose,'plain'))

	Email_Text = msg.as_string()

	Server = smtplib.SMTP('smtp.gmail.com', 587)
	Server.starttls()
	Server.login(Email_Send_From,Email_From_Password)

	Server.sendmail(Email_Send_From,Email_Send_To,Email_Text)
	print("Iris ->  Email enviado com sucesso!!!")
	Server.quit()
