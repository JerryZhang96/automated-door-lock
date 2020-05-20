import RPi.GPIO as GPIO
import time
import pyrebase

config = {
    
    # Firebase project configs
  "apiKey": "api_key",
  "authDomain": "auth_domain", 
  "databaseURL": "database-url",
  "storageBucket": "storage-bucket",
}

firebase = pyrebase.initialize_app(config)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

db = firebase.database()

while(True):

      Door = db.child("Door").get()
      
      for user in Door.each():
		
          if(user.val() == "Lock"):

              GPIO.output(18, False)
	
          else:
		
              GPIO.output(18, True) 
    
          time.sleep(0.1)


