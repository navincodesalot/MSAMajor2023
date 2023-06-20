import random

def main():
    while True:
        try:
            level = int(input("Enter level 1, 2, or 3: "))
            if level != 1 and level != 2 and level != 3:
                print("Invalid Input!")
                continue
            else:
                break
        except ValueError:
            print("Invalid Input!")
            continue

    while True:
        try:
            questions = int(input("Enter number of questions to ask (3 - 10): "))
            if questions < 3 or questions > 10:
                print("Please enter an integer value between 3 and 10!")
                continue
            else:
                break
        except ValueError:
            print("Invalid Input!")
            continue

    correct = 0
    score = 0
    x = 0
    y = 0

    if level == 1:
        for i in range(questions):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    print("CORRECT!!!")
                    correct += 1
                else:
                    print("WRONG!!!")
            except ValueError:
                print("WRONG!!!")
    elif level == 2:
        for i in range(questions):
            x = random.randint(10, 99)
            y = random.randint(10, 99)
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    print("CORRECT!!!")
                    correct += 1
                else:
                    print("WRONG!!!")
            except ValueError:
                print("WRONG!!!")
    elif level == 3:
        for i in range(questions):
            x = random.randint(100, 999)
            y = random.randint(100, 999)
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    print("CORRECT!!!")
                    correct += 1
                else:
                    print("WRONG!!!")
            except ValueError:
                print("WRONG!!!")
                
    score = correct / questions * 100
    print(f"You got {correct} out of {questions} correct: {score:.2f}%")
main()