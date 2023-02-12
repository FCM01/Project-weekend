
import smtplib
import imghdr
from email.message import EmailMessage

email_address  ="faraimatyukira1@gmail.com"
email_password  ="rkmy yrqm qgpb rulf"
class email:
    def send_confirmation(self,email,name):
        try:
            msg = EmailMessage()
            msg['Subject'] = 'Welcome to Salus'                    
            msg['From'] = email_address
            msg['To']= email
            msg.add_alternative(f"""
                                    <!DOCTYPE html>
                                    <html>
                                        <body>
                                            <h1 style ="color:#96c8cc;">Account Made</h1> 
                                            <h2 style ="color:#96c8cc;">Thank you {name}</h2>
                                            <p>Welcome to Salus we happy to provide u a new way to get onto your school grounds to with safety and secure tracking while maintaining you safety on school gounds and notifying you of issues on school grounds</p>
                                            <p>Please  feel safe under Salus</p>
                                            <p> We care about your well being </p>
                                            <p>Yours sincerly</p>
                                            <p>The Salus Team</p>
                                        </body>
                                    </html>
                                    """,subtype= "html")
            files = ["saluswithname.jpg"]
            for images in files:
                with open(f"{images}","rb") as image :
                    file_data = image.read()
                    file_type = imghdr.what(image.name)
                    file_name= image.name
                    msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name)
            with smtplib.SMTP_SSL("smtp.gmail.com" ,465) as smtp:
                smtp.login(email_address,email_password)
                smtp.send_message(msg)
        except Exception as e :
                        print("[retrieve] retrieve() error:",e)
    def send_email(self, email,message):
        print("hello")
        try:
            msg = EmailMessage()
            msg['Subject'] = 'Welcome to Salus'                    
            msg['From'] = email_address
            msg['To']= email
            msg.add_alternative(f"""
                                    <!DOCTYPE html>
                                    <html>
                                        <body>
                                            <p>{message}</p>
                                            <p>The Salus Team</p>
                                        </body>
                                    </html>
                                    """,subtype= "html")
            files = ["saluswithname.jpg"]
            for images in files:
                with open(f"{images}","rb") as image :
                    file_data = image.read()
                    file_type = imghdr.what(image.name)
                    file_name= image.name
                    msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name)
            with smtplib.SMTP_SSL("smtp.gmail.com" ,465) as smtp:
                smtp.login(email_address,email_password)
                smtp.send_message(msg)
        except Exception as e :
                        print("[retrieve] retrieve() error:",e)


    def send_invite(self, email):
        try:
            msg = EmailMessage()
            msg['Subject'] = 'Invite'                    
            msg['From'] = email_address
            msg['To']= email
            msg.add_alternative(f"""
                                    <!DOCTYPE html>
                                    <html>
                                        <body>
                                             <h1 style ="color:#96c8cc;">Invite to make account</h1> 
                                            <p>We care about your well being and a dear friend has asked for you to join our email server platform for better comunication </p>
                                            
                                        </body>
                                    </html>
                                    """,subtype= "html")
            files = ["saluswithname.jpg"]
            for images in files:
                with open(f"{images}","rb") as image :
                    file_data = image.read()
                    file_type = imghdr.what(image.name)
                    file_name= image.name
                    msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name)
            with smtplib.SMTP_SSL("smtp.gmail.com" ,465) as smtp:
                smtp.login(email_address,email_password)
                smtp.send_message(msg)
        except Exception as e :
                        print("[retrieve] retrieve() error:",e)

    def send_appointment_confirmation(self,email):
        try:
            msg = EmailMessage()
            msg['Subject'] = 'Welcome to Salus'                    
            msg['From'] = email_address
            msg['To']= email
            msg.add_alternative(f"""
                                    <!DOCTYPE html>
                                    <html>
                                        <body>
                                             <h1 style ="color:#96c8cc;">Your appointment has be made</h1> 
                                            <p>We care about your day and we have made youe appoint ment and w will remind you when it occurs</p>
                                            
                                        </body>
                                    </html>
                                    """,subtype= "html")
            files = ["saluswithname.jpg"]
            for images in files:
                with open(f"{images}","rb") as image :
                    file_data = image.read()
                    file_type = imghdr.what(image.name)
                    file_name= image.name
                    msg.add_attachment(file_data,maintype="image",subtype=file_type,filename =file_name)
            with smtplib.SMTP_SSL("smtp.gmail.com" ,465) as smtp:
                    smtp.login(email_address,email_password)
                    smtp.send_message(msg)
        except Exception as e :
                        print("[retrieve] retrieve() error:",e)

tool  = email()
tool.send_confirmation("faraimatyukira1@gmail.com","Farai")