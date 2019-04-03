import csv
import socket

domainsFile= ''
fieldDelimiter = '\t'

with open(domainsFile, mode='r') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter = fieldDelimiter)
    line_count = 0

    for row in csv_reader:

        try:

            domainData = socket.getaddrinfo(row[0],80)
            ipv4Data = domainData[0]
            print(f'{row[0]} \t {ipv4Data[4]}')

        except:

            print(f'{row[0]} \t Non raggiungibile')

        line_count += 1

    print(f'{line_count} rows checked.')
