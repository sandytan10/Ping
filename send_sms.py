from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9dae5fbe48041a8914f62f3ac15e2528"
# Your Auth Token from twilio.com/console
auth_token  = "e1cd7e2a73d88c3b0e3bd92caca662d0"

client = Client(account_sid, auth_token)
#if the number texts the twilio number add that number to list1

list1 = ["+16466967783","+15163034992","+19292636063",]
for x in list1:
    message = client.messages.create(

        to=x,
        from_="+18482259352",
        body="hi my name is li3l")

    print(message.sid)
