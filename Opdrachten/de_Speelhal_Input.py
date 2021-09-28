ticket = int(input("hoeveel tickets willen jullie? 1 kost €7,45\n"))
vipTicket = int(input("hoeveel mensen willen VIP tickets? 1 minuut is €0,37\n"))
ticketKosten = float(7.45)
vipTicketKosten = float(0.37)

print("Dat word dan:")
print(int(((ticket * ticketKosten) + (vipTicket * vipTicketKosten))* 100),"cent")