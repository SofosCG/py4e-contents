email = dict()
name = input("Enter file:")
handle = open(name)

for line in handle:
    if line.startswith("From "):
        mail = line.split()[1]
        email[mail] = email.get(mail, 0) + 1

bigcount = None
bigmail = None
for mail,count in email.items():
    if bigcount == None or count > bigcount:
        bigmail = mail
        bigcount = count

print(bigmail, bigcount)
