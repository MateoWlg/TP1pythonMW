minute_ecoule = int(input("Entrez le nombre de minutes ecoulées."))
heure = (minute_ecoule //60 ) % 24
jour = (minute_ecoule // 60) //24
minute = (minute_ecoule % 60)
jour_du_mois = (jour +1 , heure, minute)
print(f'La date associée est Jour : {Jour},Heure {heure} {minutes} minutes écoulées est le {jour_du_mois}')
