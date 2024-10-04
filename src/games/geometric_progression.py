import random

def generate_progression(length=10):
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    progression = [start * (ratio ** i) for i in range(length)]
    return progression

def hide_element(progression):
    index = random.randint(0, len(progression) - 1)
    hidden_value = progression[index]
    progression[index] = '..'
    return progression, hidden_value

def geometric_progression_game():
    progression = generate_progression()
    hidden_progression, hidden_value = hide_element(progression)
    print(f"Guess the missing number: {' '.join(map(str, hidden_progression))}")
    
    answer = int(input("Your answer: "))
    
    if answer == hidden_value:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {hidden_value}.")
