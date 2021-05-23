from replyengine import get_reply
from random import randint

print("You have entered into a conversation with Botty, the bot. Type end to exit the conversation.")

while True:
    inp = input().lower().replace(",","").replace("?","").replace("!","").replace(".","")

    if inp == "end":
        break 

    reply = get_reply("csv_dataset.txt", inp)
   
    if reply != None:
        print(reply[randint(0,1)])

    else : 
        print("No appropriate output found!")




