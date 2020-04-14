# -*- coding: utf-8 -*-
"""shopping_cart.ipynb

This is a shopping cart that helps users add items and get their total prices based on discounts
"""

import numpy as np

# Vars
budget = 200; # Budget
total = 0; # Total price
prices = { # Price list
    "Soup":0.65,
    "Bread":0.80,
    "Milk":1.30,
    "Apples":1.00
}

cart = [] # Shopping cart
element = input("""
====Item=====Price====
 
    Soup    :  65 p
    Bread   :  80 p
    Milk    :  1.30 £
    Apples  :  1.00 £
    
Enter your order in the below format with item and quantity
Eg: Milk 2:""")

if element:
  if " " in element:
    cmd, qty = element.split()
  else:
    element = input("You forgot to enter quantity, Enter order: ")
    cmd, qty = element.split()

while cmd in prices.keys():
    price = round(float(prices[cmd])*int(qty),2)

    cart+=[(qty,cmd,price)]
    el = input("Enter order: ")
    if el:
      if " " in el:
        cmd, qty = el.split()
      else:
        el = input("You forgot to enter quantity, Enter order: ")
        cmd, qty = el.split()
    else:
      cmd = ""
if cmd not in ["","\t","\n"]:
    print(cmd," is not available")

print("you cart contains :\n")
unique_list = []
if cart != []:
    # for item in cart:
    for i in range(len(cart)):
      for j in range(i + 1, len(cart)):
        if cart[i] == cart[j]:
          x = cart[i]
          y = cart[j]
          qty = int(x[0])+int(y[0])
          cmd = x[1]
          price = round(float(prices[cmd])*qty,2)
          cart += [(qty,cmd,price)]
          cart.remove(x)
          cart.remove(y)
SubTotal= 0
Total = 0
if cart != []:
  for item in cart:
    
      if item[1] != "Apples":
        print(item[1],"quantity: ", item[0],"Price: ",f'{item[2]:.2f}',"£")
        SubTotal += item[2]
      else:
        print("There is a 10% discount on Apples")
        print(item[1],"quantity: ", item[0],"Price: ",f'{item[2]:.2f}',"£")
        print(item[1],"discount 10% off: ","-",item[2]*10/100,"£")
        SubTotal += item[2]
        originalPrice = item[2]
        price = item[2] - item[2]*10/100
  Total = round(SubTotal - originalPrice + price, 2)
  print("Subtotal: ", f'{SubTotal:.2f}',"£")
  print("Total: ", f'{Total:.2f}',"£")       
else:
    print("Nothing")

input("\nPress enter to exit...")
