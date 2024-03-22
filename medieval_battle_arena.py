# -*- coding: utf-8 -*-
"""Medieval battle arena.ipynb

import time
import random

class Character:
    def __init__(self, name, health, attack, defense, weapon):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.weapon = weapon

    def __str__(self):
        return f"{self.name}\nHealth: {self.health}\nAttack: {self.attack}\nDefense: {self.defense}\nWeapon: {self.weapon}\n"

class BattleArena:
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty

def countdown():
    for i in range(3, 0, -1):
        print(i, end=' ', flush=True)  # Print in the same line
        time.sleep(1)
    print("Fight!")
    time.sleep(1)

def choose_character(characters):
    while True:
        print("Choose your character:")
        for idx, character in enumerate(characters, start=1):
            print(f"{idx}. {character}")

        choice = input("Enter the number of your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(characters):
                return characters[choice - 1]
        print("Invalid choice. Please enter a number within the range.")

def simulate_battle(player_character, enemy_character):
    while player_character.health > 0 and enemy_character.health > 0:
        player_damage = max(player_character.attack - enemy_character.defense, 0)
        enemy_damage = max(enemy_character.attack - player_character.defense, 0)

        enemy_character.health -= player_damage
        print(f"You attack the enemy with your {player_character.weapon} for {player_damage} damage.")
        if enemy_character.health <= 0:
            print("Congratulations! You emerge victorious!")
            break

        player_character.health -= enemy_damage
        print(f"The enemy attacks you with their {enemy_character.weapon} for {enemy_damage} damage.")
        if player_character.health <= 0:
            print("Good luck next time! You are defeated!")
            break

def start_game():
    characters = [
        Character("Knight", 100, 30, 60, "Sword"),
        Character("Archer", 80, 100, 55, "Bow"),
        Character("Barbarian", 120, 35, 10, "Axe")
    ]

    arenas = [
        BattleArena("Colosseum", "Medium"),
        BattleArena("Forest Arena", "Hard"),
        BattleArena("Ruins Arena", "Easy")
    ]

    player_character = choose_character(characters)
    print(f"You've chosen: {player_character.name}")

    arena = random.choice(arenas)
    print(f"You're entering the {arena.name} ({arena.difficulty} difficulty)!")
    countdown()

    enemy_character = random.choice(characters)
    print(f"You encounter an enemy: {enemy_character.name}")

    simulate_battle(player_character, enemy_character)

start_game()

