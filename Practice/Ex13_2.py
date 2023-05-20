import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter Location: ')
print('Retrieving', url)
js = urllib.request.urlopen(url).read()
data = json.loads(js)["comments"]

sum = 0
count = 0
for item in data:
    count = count + 1
    sum = sum + item['count']

print('Count:', count)
print('Sum:', sum)