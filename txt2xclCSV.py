import csv

with open('Book1.csv', 'r') as csv_file: #same directory as the file that am currently writing
    csv_reader = csv.reader(csv_file) #reader method
    
    

    with open('new_Book1.csv', 'w') as new_file:
        csv_writer =csv.writer(new_file, delimiter='-')


        for line in csv_reader:
            csv_writer.writerow(line)
        