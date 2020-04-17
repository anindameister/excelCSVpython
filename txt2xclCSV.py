import csv

with open('Book1.csv', 'r') as csv_file: #same directory as the file that am currently writing
    csv_reader = csv.reader(csv_file) #reader method
    print(csv_reader) #<_csv.reader object at 0x000001F4CEF68F28> , just an object in memory
