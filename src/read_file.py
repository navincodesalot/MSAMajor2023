def get_menu_dictionary():
    pass

def main():
    data_file = open("file.txt", "r")

    menu_item = get_menu_dictionary()
    for line_of_data in data_file:
        key_values = line_of_data.strip().split(", ")
        menu_item[key_values[0]] = float(key_values[1])

    data_file.close()

    for item, price in menu_item.items():
        print(f"{item}, ${price:0.2f}")

main()