
def get_reply(file_name, input): 
    import csv
    with open(file_name, "r") as csv_f:
        csv_reader = csv.reader(csv_f, delimiter = ",")  
        return search(csv_reader, input) 

def search(csv_reader, input) :
    
    for line in csv_reader:
        if input == line[0]:
            line.pop(0)
            return line 
        


