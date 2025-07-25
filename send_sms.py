from twilio.rest import Client

def send(value, classes):
#Your Account SID from twilio.com/console
     account_sid = "your_acc_sid"
#Your Auth Token from twilio.com/console
     auth_token  = "your_auth_token"

     client = Client(account_sid, auth_token)

     message = client.messages.create(
         to="+919535148572",
         from_="+17373734268",
         body=f"Blindness detection system report!\nSeverity level is : {value}\nClass is {classes}")

     print('Message sent Succesfully...')
     print(message.sid)
