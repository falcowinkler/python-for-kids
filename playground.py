from library.labyrinth import *

# der Spieler ist bei 0,0
# Das Spielfeld hat Größe 15 x 15

set_size(15, 15)

# Labyrinth aufbauen

for x in range(1, 5):
    block(x, 0, "Gras")

block(0, 1, "Dreck")
block(1, 1, "Kohle")
block(2, 3, "Kohle")
block(5, 4, "Ziel")
block(5, 5, "Wasser")
block(7, 3, "Wasser")


# Durch das labyrinth navigieren

bewegung("Rechts")
bewegung("Links")

start()
