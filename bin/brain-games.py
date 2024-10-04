#!/usr/bin/env python3
import sys
import os

# Добавляем путь к src
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

#!/usr/bin/env python3
from cli import welcome_user
from games.lcm_game import lcm_game
from games.geometric_progression import geometric_progression_game
from engine import play_game

def main():
    welcome_user()
    print("Choose a game:")
    print("1. LCM Game")
    print("2. Geometric Progression Game")
    choice = input("Enter game number: ")
    
    if choice == '1':
        play_game(lcm_game)
    elif choice == '2':
        play_game(geometric_progression_game)

if __name__ == '__main__':
    main()

