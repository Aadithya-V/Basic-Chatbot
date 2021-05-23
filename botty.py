import csv
from random import randint
print("You have entered into a conversation with Botty, the bot. Type end to exit the conversation.")
csv_f =open("csv_dataset.txt", "r") 
csv_reader = csv.reader(csv_f, delimiter=",")

while True:
    match = 0
    inp = input().lower()
    
    if inp == "end":
        break 
    
    for line in csv_reader:
        if inp == line[0]:
            match = 1
            print(line[randint(1, 2)])

    csv_f.seek(0)       
       
    if match == 0:
        print("No matching output found!")


csv_f.close()


