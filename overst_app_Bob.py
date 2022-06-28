# Rotterdam Metro Overstap App, benadering van Bob
# CopyLeft 2022, Jan Kroon (Rotterdam University of Applied Sciences)

# De Metro Stations

stations  = [{“Vlaardingen West”: [lijn_A, lijn_B, ...]},
             {“Vlaardingen Centrum”: [lijn_A, lijn_B, ...]},
             {“Vlaardigen Oost”: [lijn_A, lijn_B, ...]},
             {“Schiedam Nieuwland”: [lijn_A, lijn_B, ...]},
             {“Schiedam Centrum”: [lijn_A, lijn_B, lijn_C, ...]},
             {“Marconiplein”: [lijn_A, lijn_B, lijn_C, ...]},
             {“Delfshaven”: [lijn_A, lijn_B, lijn_C,...]},
             {“Coolhaven”: [lijn_A, lijn_B, lijn_C,...]},
             {“Dijkzicht”: [lijn_A, lijn_B,lijn_C,...]},
             {“Eendrachtsplein”: [lijn_A, lijn_B, lijn_C, ...]},
             {“Beurs”: [lijn_A, lijn_B, lijn_C, ...]},
             { “Blaak”, [lijn_A, lijn_B, lijn_C, ...]},
             {“Oostplein”:[lijn_A, lijn_B,...]},
             {“Gerdesiaweg”,[lijn_A, lijn_B,...]},
             {“Voorschoterlaan”,[lijn_A, lijn_B,...]},
             {“Kralingse Zoom”,[lijn_A, lijn_B,...]},
             {“Capelsebrug”,[lijn_A, lijn_B,...]},
             {“Schenkel”,[lijn_A, lijn_B,...]},
             {“Prinsenlaan”,[lijn_A, lijn_B,...]},
             {“Oosterflank”,[lijn_A, lijn_B,...]},
             {“Alexander”,[lijn_A, lijn_B,...]},
             {“Graskruid”,[lijn_A, lijn_B,...]},
             {“Romeynshof”,[lijn_A, ...]},
             {“Binnenhof”], [lijn_A, ...]},
             {“Hoek van Holland Haven”,[lijn_B, ...]},
             {“Steendijkpolder”,[lijn_B, ...]},
             {"Maassluis West”, [lijn_B, ...]},
             {“Maassluis Centrum”, [lijn_B, ...]},
             {”Hesseplaats”, [lijn_B, ...]},
             {“Nieuw Verlaat”, [lijn_B, ...]},
             {“Ambachtsland”, [lijn_B, ...]},
             {“De Tochten”, [lijn_B, ...]},
             {“Nesselande”, [lijn_B, ...]},
             {“De Akkers”, [lijn_C, ...]},
             {“Heemraadlaan”, [lijn_C, ...]},
             {“Spijkenisse Centrum”, [lijn_C, ...]},
             {“Zalmplaat”, [lijn_C, ...]},
             {“Hoogvliet”, [lijn_C, ...]},
             {“Tussenwater”, [lijn_C, ...]},
             {“Pernis”, [lijn_C, ...]},
             {“Vijfsluizen”, [lijn_C, ...]},
             {“Troelstralaan”, [lijn_C, ...]},
             {“Parkweg”, [lijn_C, ...]},
             {“Poortugaal”,[lijn_C, ...]},
             {“Rhoon”, [lijn_C, ...]},
             {“Slinge”,[lijn_C, ...]},
             {“Zuidplein”,[lijn_C, ...]},
             {“Maashaven”,[lijn_C, ...]},
             {“Rijnhaven”, [lijn_C, ...]},
             {“Wilhelminaplein”,[lijn_C, ...]},
             {“Leuvehaven”,[lijn_C, ...]},
 “Beurs”, “Blaak”, “Oostplein”, “Gerdesiaweg”, “Voorschoterlaan”, “Kralingse Zoom”, “Capelsebrug”, “Slotlaan”, “Capelle Centrum”, “De Terp”]
lijn_D = [“De Akkers”, “Heemraadlaan”, “Spijkenisse Centrum”, “Zalmplaat”, “Hoogvliet”, “Tussenwater”, “Poortugaal”, “Rhoon”, ]
lijn_E = [“Stadhuis”, “Rotterdam Centraal”, “Blijdorp”, “Melanchthonweg”, “Meijersplein”, “Rodenrijs”, “Berkel Westpolder”, “Pijnacker Zuid”, “Pijnacker Centrum”, “Nootdorp”, “Leidschenveen”, “Forepark”, “Leidschendam-Voorburg”, “Voorburg ‘t Loo”, Laan van NOI”, Den Haag Centraal”]


# User Interface
print("*** Rotterdam Metro Overst_App ***")

startpunt = input("Welk station stapt u in? ")
eindpunt = input("Welk station wilt u uitstappen? ")

# Route berekening
# Bob heeft het volgende bedacht. Ik kijk eerst of beginpunt en eindpunt toevallig op een zelfde lijn liggen.
# Als dat zo is, dan is deze lijn nemen de korste route (zonder overstappen).
# Als dat niet zo is, dan zoek ik een station dat zowel op een lijn door startpunt en een lijn door eindpunt ligt.
# Dat station is dan de ideale overstapstation!

for lijn in lijnen:
    if lijn.contains(startpunt):
        eerste_deel = lijn
        break

for lijn in lijnen:
    if lijn.contains(eindpunt):
        tweede_deel = lijn
        break

print(f"Stap in {eerste_deel}, stap uit op Station Beurs en stap over op {tweede_deel}, stap uit op {eindpunt}.") 

