# Mert Erciyas Pizza calculator 
smallPizza = int(input("Hoeveel kleine pizzas wilt u?\n")) # hierbij kan je invoeren hoeveel small pizzas je wilt
mediumPizza = int(input("Hoeveel medium pizzas wilt u?\n")) # hierbij kan je invoeren hoeveel medium pizzas je wilt
largePizza = int(input("Hoeveel grote pizzas wilt u?\n")) # hierbij kan je invoeren hoeveel large pizzas je wilt

smallPizzaPrice = float(7.50) # hier zie je de prijs van de small pizza
mediumPizzaPrice = float(9.50) # hier zie je de prijs van de medium pizza
largePizzaPrice = float(11.50) # hier zie je de prijs van de large pizza

print("Dus jij hebt" , smallPizza , "small pizzas" , mediumPizza , "medium pizzas" , largePizza , "large pizzas\n Dat word dan:") # hierbij laat hij weten hoeveel pizzas je hebt besteld
kosten = (int((smallPizza * smallPizzaPrice) + (mediumPizza * mediumPizzaPrice) + (largePizza * largePizzaPrice))) # hier berekend hij de kosten van alle pizzas
print(kosten , "euro") # hier laat hij zien hoeveel de pizzas in totaal kosten