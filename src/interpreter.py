def main():
    while True:
        cool = input("Enter a problem: ")
        cool = cool.split(" ")
        if len(cool) != 3:
            print("Error: Invalid Format")
            continue

        x = int(cool[0])
        y = cool[1]
        z = int(cool[2])

        if z not in ["+", "-", "*", "/"]:
            print("Invalid Operator")
            continue
        
        if z == 0:
            print("Divide by Zero Error")
            continue
        sum = int(0)
        
        if y == "+":
            sum = x + z
        elif y == "-":
            sum = x - z
        elif y == "*":
            sum = x * z
        elif y == "/":
            sum = x / z

        print(f"{sum:0.1f}")
        another_calc = input("Would you like to evaluate another expression? Y to continue, any other key to exit ").lower()
        if another_calc != "y":
            break
main()