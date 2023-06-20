import random

def prompt_solve(level, questions):
    if level == 1:
        return gen_questions(questions, 0, 9)
    elif level == 2:
        return gen_questions(questions, 10, 99)
    elif level == 3:
        return gen_questions(questions, 100, 999)
        
def gen_questions(questions, min, max):
    correct = 0
    for i in range(questions):
            x = random.randint(min, max)
            y = random.randint(min, max)
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    print("CORRECT!!!")
                    correct += 1
                else:
                    print("WRONG!!!")
            except ValueError:
                print("WRONG!!!")
    return correct

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

    correct = prompt_solve(level, questions)
                
    score = correct / questions * 100
    print(f"You got {correct} out of {questions} correct: {score:.2f}%")

main()