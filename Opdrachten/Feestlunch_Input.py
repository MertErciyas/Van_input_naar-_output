print("Goeiemorgen\n")
croissant = int(input("croissant kosten €0,39. Hoeveel croissant wilt u?\n"))
bagguette = int(input("bagguette kost dan €2,78. Hoeveel Bagguetes wilt u?\n"))
croissantKosten = float(0.39)
bagguetteKosten = float(2.78)
korting = float(1.50)

print(int((((croissant * croissantKosten) + (bagguette * bagguetteKosten) - korting) * 100)),"cent")