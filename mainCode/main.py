import numpy as np
import game_rules

row_number = int(input("Filas para jugar el juego: "))
col_number = int(input("Columnas para jugar el juego: "))


board = np.zeros((row_number,col_number)) # create  an empty board
game_in_progress = True
player_turn = 1 # Player 1 starts
while (game_in_progress):
    print (board)
    flag = True
    while (flag):
        print ("Jugador " + str(player_turn), ", dónde quiere colocar?")
        row_selected  = int(input("Mencione una fila: "))
        col_selected = int(input("Menciona una columna: "))
        




