# Mert Erciyas Pizza calculator 
smallPizza = int(input("Hoeveel kleine pizzas wilt u?\n")) # hierbij kan je invoeren hoeveel small pizzas je wilt
mediumPizza = int(input("Hoeveel medium pizzas wilt u?\n")) # hierbij kan je invoeren hoeveel medium pizzas je wilt
largePizza = int(input("Hoeveel grote pizzas wilt u?\n")) # hierbij kan je invoeren hoeveel large pizzas je wilt

smallPizzaPrice = 7.50 # hier zie je de prijs van de small pizza
mediumPizzaPrice = 9.50 # hier zie je de prijs van de medium pizza
largePizzaPrice = 11.50 # hier zie je de prijs van de large pizza

smallPizzaKosten = (smallPizza * smallPizzaPrice)
mediumPizzaKosten = (mediumPizza * mediumPizzaPrice)
largePizzaKosten = (largePizza * largePizzaPrice)

print("Dus jij hebt" , smallPizza , "small pizzas" , mediumPizza , "medium pizzas" , largePizza , "large pizzas\n") # hierbij laat hij weten hoeveel pizzas je hebt besteld
print("dat word dan" , smallPizzaKosten , "euro voor de small pizza's" , mediumPizzaKosten , "euro voor de medium pizza's" , largePizzaKosten , "euro voor de large pizza's\n Dat word dan in totaal:" )
kosten = (float((smallPizza * smallPizzaPrice) + (mediumPizza * mediumPizzaPrice) + (largePizza * largePizzaPrice))) # hier berekend hij de kosten van alle pizzas
print(kosten , "euro") # hier laat hij zien hoeveel de pizzas in totaal kosten