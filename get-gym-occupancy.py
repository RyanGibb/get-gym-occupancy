import urllib.request
import csv
import sys
import datetime

url = "https://www.st-andrews.ac.uk/sport/"
search = "Occupancy: "

html = urllib.request.urlopen(url).read().decode()
index = html.find(search) + len(search)

if index == -1:
    quit()

char = html[index]

occupancy = ""

while char.isdigit():
    occupancy += char
    index += 1
    try:
        char = html[index]
    except IndexError:
        break

print(occupancy)

# Handle recording
if len(sys.argv) == 2:

        date = datetime.datetime.now().replace(microsecond=0).isoformat()
        with open(sys.argv[1], 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([date, occupancy])
