from library.labyrinth import set_size, waehle_spieler, block, block_typ, bewegung, start

# der Spieler ist bei 0,0
# Das Spielfeld hat Größe 10 x 10

set_size(10, 10)
waehle_spieler("girl")
# Labyrinth aufbauen

block(0, 1, "Gras") # Block setzen

print(block_typ(0, 1))  # Den block typ an stelle x, y holen

# Durch das labyrinth navigieren
bewegung("Rechts")

start()
