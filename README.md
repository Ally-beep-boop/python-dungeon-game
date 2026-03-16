# Dungeon Crawler

A text-based dungeon crawler game built in Python, developed as part of 
my transition into software development and data science.

## About

The player fights through 3 rooms of randomly spawned monsters before 
facing a final boss — the Dragon. Each combat round involves strategic 
choices, randomised damage, and resource management between rooms.

This project was built from scratch to practice core Python fundamentals
learnt from the beginning phase of my studies, including
object-oriented programming, modular design, and clean, 
readable code.

## How to run

Make sure you have Python 3 installed, then run:

    python dungeon.py

No external libraries required — just the Python standard library.

## Gameplay

- Enter your hero's name to begin
- Each room spawns a random monster (Goblin, Skeleton, or Troll)
- Choose to attack or run each turn
- Survive all 3 rooms to face the Dragon boss
- Win by defeating the Dragon with your HP above zero

## What this project demonstrates

- **Object-oriented programming** — `Player` and `Monster` classes with 
  encapsulated attributes and shared methods
- **Loops and conditionals** — a `while` loop driving a turn-based 
  combat system
- **Modular design** — separate functions for combat, monster spawning, 
  and game flow
- **Random number generation** — variable damage rolls to keep 
  fights unpredictable
- **Input validation** — handling unexpected user input gracefully

## What I'd add next

- An inventory system for collecting weapons and potions
- A save/load feature using JSON files
- Coloured terminal output using `colorama`
- Unit tests using `pytest`
- Data logging to track player stats across sessions (great crossover 
  with data analysis!)

## About me

I'm a career changer currently completing a data science 
bootcamp with HyperionDev and Stellenbosch University.
I bring 2 years of professional experience from healthcare
marketing, and I'm actively looking for junior developer or data analyst/
science intern roles where I can apply my growing technical skills 
alongside my real-world problem-solving background.

[LinkedIn] https://linkedin.com/in/ally-remas-900aa1255
