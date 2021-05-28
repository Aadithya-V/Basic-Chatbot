import csv

def get_reply(file_name, input): 
    with open(file_name, "r") as csv_f:
        csv_reader = csv.reader(csv_f, delimiter = ",")  
        next(csv_f)
        return search(csv_reader, input) 

def search(csv_reader, input) :
    input = preprocess_input(input)
    for line in csv_reader:
        if input == line[0]:
            line.pop(0)
            return line 
        
def preprocess_input(input):
    input = input.lower().replace(",","").replace("?","").replace("!","").replace(".","")
    return input
