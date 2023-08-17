import urllib.error
import urllib.parse
import urllib.request

#count number of words on the web page
fileHandle = urllib.request.urlopen('htttp://data.pr4e.org/romeo.txt')
counts = dict()
for line in fileHandle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0, +1)
print(counts)

#print out a web page
fHandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fHandle:
    print(line.decode().strip())