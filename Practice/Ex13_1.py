import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('URL: ')
print("Retrieving", url)
xml = urllib.request.urlopen(url, context=ctx).read()
print("Retrieving", len(xml), "Characters")
tree = ET.fromstring(xml)
counts = tree.findall('.//count')
print("Count:", len(counts))

sum = 0
for item in counts:
    sum = sum + int(item.text)

print("Sum:", sum)