import csv

with open('Book1.csv', 'r') as csv_file: #same directory as the file that am currently writing
    csv_reader = csv.DictReader(csv_file) #reader method

    for line in csv_reader:
        print(line['Object number'])