def main():
    amount = int(50)
    accepted_coins = [1, 5, 10, 25]
    inserted_coins = int(0)
    while amount > 0:
        try:
            print(f"Amount Due: {amount}")
            inserted_coins = int(input("Insert coin: "))
            if inserted_coins not in accepted_coins:
                continue
            else:
                amount -= inserted_coins
        except ValueError:
            continue;
    print(f"Change owed: {abs(amount)}")
main()