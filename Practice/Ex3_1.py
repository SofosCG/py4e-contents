hrs = input("Enter Hours: ")
h = float(hrs)
rts = input("Rate per Hour: ")
r = float(rts)

if h <= 40:
    p = h * r
elif h > 40:
    p = (40 * r) + ((h - 40) * (r * 1.5))

print(p)
