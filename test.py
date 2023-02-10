
import smtplib
import imghdr
from email.message import EmailMessage



print("hello")
email_address  ="faraimatyukira1@gmail.com"
email_password  ="rkmy yrqm qgpb rulf"
try:
    msg = EmailMessage()
    msg['Subject'] = 'Welcome to Salus'                    
    msg['From'] = email_address
    msg['To']= "faraimatyukira1@gmail.com"
    msg.add_alternative(f"""
                            <!DOCTYPE html>
                            <html>
                                <body>
                                    <h1 style ="color:#96c8cc;">Account Made</h1> 
                                    <h2 style ="color:#96c8cc;">Thank you Gerni</h2>
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