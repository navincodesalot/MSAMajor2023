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
    attempts = 3
    for _ in range(questions):
            x = random.randint(min, max)
            y = random.randint(min, max)
            while True:
                try:
                    answer = int(input(f"{x} + {y} = "))
                    if answer == x + y:
                        print("CORRECT!!!")
                        correct += 1
                        break
                    else:
                        raise(ValueError)
                except ValueError:
                    print("WRONG!!!")
                    attempts -= 1
                    if attempts == 0:
                        print(f"Correct Answer: {x} + {y} = {x + y}")
                        attempts = 3
                        break
                    else:
                        continue
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
            questions = int(input("Enter number of questions to ask (3 to 10): "))
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