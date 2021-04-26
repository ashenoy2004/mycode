#!/usr/bin/env python3
icecream= ["flavors","salty"]

name =input("Enter your name:")

num =99
print(f'99',icecream[0], ",and ",name,"chooses to be", icecream[1])

icecream.append(num)

print(f'{icecream[-1]} {icecream[0]} ,and {name} chooses to be { icecream[1]}')
