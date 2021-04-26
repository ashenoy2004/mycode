#!/usr/bin/env python3
user_input = input("Enter your Name:")

user_day_of_week = input("Enter Day of Week: ")
## the line below creates a single string that is passed to print()
# print("You told me the IPv4 address is:" + user_input)

## print() can be given a series of objects separated by a comma
print (f"Hello,{ user_input}! Happy {user_day_of_week}!")
