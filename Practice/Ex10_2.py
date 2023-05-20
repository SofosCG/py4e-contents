name = input("Enter file:")
handle = open(name)
hrlst = dict()

for lines in handle:
    if lines.startswith("From "):
        time = lines.split()[5]
        hours = time.split(":")[0]
        hrlst[hours] = hrlst.get(hours,0) + 1

lst = list()
for h,v in hrlst.items():
    newtup = (h,v)
    lst.append(newtup)

lst = sorted(lst,reverse = False)

for h,v in lst[:]:
    print(h,v)
