from library.labyrinth import *

# der Spieler ist bei 0,0
# Das Spielfeld hat Größe 15 x 15

for x in range(1, 5):
    add_block(x, 0, "grass")
add_block(1, 1, "coal")
add_block(2, 3, "coal")
add_block(5, 4, "goal")
add_block(5, 5, "water")
add_block(7, 3, "water")


#for i in range(5):
#    make_move("right")
#    make_move("down")

start()
