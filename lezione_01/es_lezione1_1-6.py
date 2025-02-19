tot=0
ordine:dict= {"pizza": 9.00, "hamburger": 15.50, "verdura_del_giorno": 7.00, "focaccia": 6.00}

tot= tot + ordine["pizza"]
tot= tot + ordine["hamburger"]
tot= tot + ordine["verdura_del_giorno"]
tot= tot + ordine["focaccia"]

print (f"{tot:.2f}$")