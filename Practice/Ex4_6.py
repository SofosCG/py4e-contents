def computepay(h, r):
    a = float(h)
    b = float(r)
    if a < 40:
        return a * b
    elif a > 40:
        return (40 * b) + ((a - 40) * (b * 1.5))

hrs = input("Enter Hours: ")
rts = input("Enter Rate per Hour: ")
p = computepay(hrs, rts)
print("Pay", p)
