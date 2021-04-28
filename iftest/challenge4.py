#!/usr/bin/env python


# Can we guess your age by your Taste In Movies

Movies = ["Beauty and Beast","The Little Mermaid","Gurdian of Galaxy","Pulp Fiction",""]

movie_selected =input(f"Pick your Selection {Movies}")

print(movie_selected)

if movie_selected == "Beauty and Beast":
    print("your age is 15")
elif movie_selected == "The Little Mermaid":
    print("Your age is 10")
elif movie_selected =="Pulp Fiction":
    print("Your age is 55")
else:
    print("Cannot guess your age")

