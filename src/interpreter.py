cool = input("Enter a problem: ")
cool = cool.split(" ")
x = float(cool[0])
y = cool[1]
z = float(cool[2])

sum = float(0)

if y == "+":
    sum = x + z
elif y == "-":
    sum = x - z
elif y == "*":
    sum = x * z
elif y == "/":
    sum = x / z
print(f"{sum:0.1f}")