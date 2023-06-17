def main():
    amount = int(50)
    accepted_coins = [1, 5, 10, 25]
    inserted_coins = int(0)
    while amount != 0:
        try:
            print(f"Amount Due: {amount}")
            inserted_coins = int(input("Insert coin: "))
            if inserted_coins not in accepted_coins:
                continue
            else:
                amount = amount - inserted_coins
            if amount <= 0:
                print(f"Change owed: {abs(amount)}")
                break
        except ValueError:
            continue;
main()