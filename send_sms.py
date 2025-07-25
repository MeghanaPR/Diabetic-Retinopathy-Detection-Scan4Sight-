from twilio.rest import Client

def send(value, classes):
#Your Account SID from twilio.com/console
     account_sid = "AC7af9c43a8eebf5f95e207e3074eeed88"
#Your Auth Token from twilio.com/console
     auth_token  = "00e6d135945ccca5cbb0324fce3fed09"

     client = Client(account_sid, auth_token)

     message = client.messages.create(
         to="+919535148572",
         from_="+17373734268",
         body=f"Blindness detection system report!\nSeverity level is : {value}\nClass is {classes}")

     print('Message sent Succesfully...')
     print(message.sid)
