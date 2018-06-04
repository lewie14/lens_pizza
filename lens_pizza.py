#Set up lists for toppings and prices
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

#Number of pizzas is the length of the toppings list
num_pizzas = len(toppings)

#let user know how many types of pizza
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#Combine prices and toppings into one list called pizzas
pizzas = list(zip(prices, toppings))
print(pizzas)

#sort pizzas so lowest price at start of list
pizzas.sort()
cheapest_pizza = pizzas[0]

#Find most expensive pizza
priciest_pizza = pizzas[6]

#Find the three cheapest
three_cheapest = pizzas[:3]
print(three_cheapest)
