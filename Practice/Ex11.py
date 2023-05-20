import re

hand = open("regex_sum_1529622.txt")
numlist = list()

for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    if len(x) < 1:
        continue
    for num in x:
        num = int(num)
        numlist.append(num)

sum = sum(numlist)
print(sum)
