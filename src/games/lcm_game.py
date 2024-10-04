import math
import random

def find_lcm(a, b, c):
    return math.lcm(a, math.lcm(b, c))

def lcm_game():
    a, b, c = random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)
    print(f"Find the least common multiple of {a}, {b}, {c}: ")
    answer = int(input("Your answer: "))
    correct_answer = find_lcm(a, b, c)
    
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {correct_answer}.")
