import urllib.request

url = "https://www.st-andrews.ac.uk/sport/"
search = "Occupancy: "

html = urllib.request.urlopen(url).read().decode()
index = html.find(search) + len(search)

if index == -1:
    quit()

char = html[index]

occupancy = "";

while char.isdigit():
    occupancy += char
    index += 1
    try:
        char = html[index]
    except IndexError:
        break

print(occupancy)
