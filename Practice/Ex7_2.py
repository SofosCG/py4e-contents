fname = input("Enter file name: ")
fh = open(fname)
jog = 0
count = 0

for line in fh:
    line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    text = line
    num = float(text[text.find('0'):])
    count = count + 1
    jog = jog + num

avg = jog/count
print("Average spam confidence:", avg)
