# Rotterdam Metro Overstap App, benadering van Annette
# CopyLeft 2022, Jan Kroon (Rotterdam University of Applied Sciences)

# De Metro Lijnen

lijn_A = [“Vlaardingen West”, “Vlaardingen Centrum”, “Vlaardigen Oost”, “Schiedam Nieuwland”, “Schiedam Centrum”, “Marconiplein”, “Delfshaven”, “Coolhaven”, “Dijkzicht”, “Eendrachtsplein”, “Beurs”, “Blaak”, “Oostplein”, “Gerdesiaweg”, “Voorschoterlaan”, “Kralingse Zoom”, “Capelsebrug”, "Schenkel", “Prinsenlaan”, “Oosterflank”, “Alexander”, “Graskruid”, “Romeynshof”, “Binnenhof”]
lijn_B = [“Hoek van Holland Haven”, “Steendijkpolder”, Maassluis West”, “Maassluis Centrum”, “Vlaardingen West”, “Vlaardingen Centrum”, “Vlaardigen Oost”, “Schiedam Nieuwland”, “Schiedam Centrum”, “Marconiplein”, “Delfshaven”, “Coolhaven”, “Dijkzicht”, “Eendrachtsplein”, “Beurs”, “Blaak”, “Oostplein”, “Gerdesiaweg”, “Voorschoterlaan”, “Kralingse Zoom”, “Capelsebrug”, “Schenkel”, “Prinsenlaan”, “Oosterflank”, “Alexander”, “Graskruid”,”Hesseplaats”, “Nieuw Verlaat”, “Ambachtsland”, “De Tochten”, “Nesselande”]
lijn_C = [“De Akkers”, “Heemraadlaan”, “Spijkenisse Centrum”, “Zalmplaat”, “Hoogvliet”, “Tussenwater”, “Pernis”, “Vijfsluizen”, “Troelstralaan”, “Parkweg”, “Schiedam Centrum”, “Marconiplein”, “Delfshaven”, “Coolhaven”, “Dijkzicht”, “Eendrachtsplein”, “Poortugaal”, “Rhoon”, “Slinge”, “Zuidplein”, “Maashaven”, “Rijnhaven”, “Wilhelminaplein”, “Leuvehaven”, “Beurs”, “Blaak”, “Oostplein”, “Gerdesiaweg”, “Voorschoterlaan”, “Kralingse Zoom”, “Capelsebrug”, “Slotlaan”, “Capelle Centrum”, “De Terp”]
lijn_D = [“De Akkers”, “Heemraadlaan”, “Spijkenisse Centrum”, “Zalmplaat”, “Hoogvliet”, “Tussenwater”, “Poortugaal”, “Rhoon”, ]
lijn_E = [“Stadhuis”, “Rotterdam Centraal”, “Blijdorp”, “Melanchthonweg”, “Meijersplein”, “Rodenrijs”, “Berkel Westpolder”, “Pijnacker Zuid”, “Pijnacker Centrum”, “Nootdorp”, “Leidschenveen”, “Forepark”, “Leidschendam-Voorburg”, “Voorburg ‘t Loo”, Laan van NOI”, Den Haag Centraal”]

lijnen = [lijn_A, lijn_B, lijn_C, lijn_D, lijn_E]

# User Interface
print("*** Rotterdam Metro Overst_App ***")

startpunt = input("Welk station stapt u in? ")
eindpunt = input("Welk station wilt u uitstappen? ")

# Route berekening
# Annette wilde snel klaar zijn, de deadline was ook al in zicht. "Overstappen op Station Beurs gaat altijd goed.", had ze bedacht.
# Misschien niet de snelste route voor de gebruikers, maar wel het snelst voor de software developer.

for lijn in lijnen:
    if lijn.contains(startpunt):
        eerste_deel = lijn
        break

for lijn in lijnen:
    if lijn.contains(eindpunt):
        tweede_deel = lijn
        break

print(f"Stap in {eerste_deel}, stap uit op Station Beurs en stap over op {tweede_deel}, stap uit op {eindpunt}.") 

