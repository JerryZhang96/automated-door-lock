import smtplib,ssl  
from picamera import PiCamera  
from time import sleep  
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase  
from email.mime.text import MIMEText  
from email.utils import formatdate  
from email import encoders
from gpiozero import Button, LED, Buzzer
from signal import pause


button = Button(21)
led = LED(23)
buzzer = Buzzer(17)
camera = PiCamera()

while True:

    button.wait_for_press()
    led.on()
    buzzer.on()
    button.wait_for_release()
    led.off()
    buzzer.off()

    
    def capture():
        camera.rotation = 180
        camera.capture('/home/pi/image.jpg')

    button.when_pressed = capture


    def send_an_email():  
        toaddr = 'your_email' # To id 
        me = 'your_email'     # your id
        subject = "Who's There"               # Subject
      
        msg = MIMEMultipart()  
        msg['Subject'] = subject  
        msg['From'] = me  
        msg['To'] = toaddr  
        msg.preamble = "test "   
        #msg.attach(MIMEText(text))  
      
        part = MIMEBase('application', "octet-stream")  
        part.set_payload(open("image.jpg", "rb").read())  
        encoders.encode_base64(part)  
        part.add_header('Content-Disposition', 'attachment; filename="image.jpg"')   # File name and format name
        msg.attach(part)  
      
        try:  
            s = smtplib.SMTP('smtp.gmail.com', 587)  # Protocol
            s.ehlo()  
            s.starttls()  
            s.ehlo()  
            s.login(user = 'your_email', password = 'your_password')  # User id & password
            #s.send_message(msg)  
            s.sendmail(me, toaddr, msg.as_string())  
            s.quit()  
        #except:  
        #   print ("Error: unable to send email")    
        except SMTPException as error:  
                print ("Error")                # Exception
      
    send_an_email()

