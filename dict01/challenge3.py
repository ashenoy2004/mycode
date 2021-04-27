#!/usr/bin/env python

# Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz)

#  What statistic do you want to know about? (real name, powers, archenemy)

heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "magic",
    "archenemy": "Voldemort",},
"captain america":
    {"real name": "Steve Rogers",
    "powers": "frisbee shield",
    "archenemy": "Hydra",}
        }

character = input("What character  do you want to know about? (Wolverine,Harry Potter, Agent Fritz):")

stats = input(f"What statistic do you want to know about {character}? (real name,powers,archenemy):")

print(f"{character}'s {stats} is:  {heroes[character].get(stats)}")

print(heroes['wolverine'].get('real name'))
