from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3753f14be63f54f52db1bd94fbffa248"
# Your Auth Token from twilio.com/console
auth_token  = "e45e0cb48709f219098c70f5a8f4977b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919741939070",
    from_="+13475148260",
    body="scharati@aryahamsa.org via Twilio Python rest client")

print(message.sid)