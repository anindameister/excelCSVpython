import csv

with open('Book1.csv', 'r') as csv_file: #same directory as the file that am currently writing
    csv_reader = csv.reader(csv_file) #reader method
    #print(csv_reader) #<_csv.reader object at 0x000001F4CEF68F28> , just an object in memory
    for line in csv_reader:
        #print(line) #['Image name', 'Object number', 'X1', 'Y1', 'X2', 'Y2', 'object name'], field names
                    #['download (1).jpg.txt', '2', '26', '22', '277', '144', 'car'], list of all the values
        print(line[2]) #x1 is 3rd hence 2, values under x1
        