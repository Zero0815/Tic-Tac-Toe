# TicTacToe Python Projekt
# !/usr/bin/env python3


# Reihen als Listen, damit die Reihen einfacher angesprochen werden können und auch sauber untereinander angezeigt werden.
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

# Liste aller Reihen, damit jede Reihe durch eine Whileschleife ausgegeben wird.
rows = [row1, row2, row3]

# Spieler 1 bekommt als Zeichen das X und Spieler 2 als Zeichen das O
player1 = 'X'
player2 = 'O'

# Ausgabe des Spielfelds.
for element in rows:
    print(element)

# Funktion für die Aktionen.
def action(mark, row, column):
    while True:
        
        # Wenn bei der Reihen Abfrage 1 eingegeben wird.
        if row == 1:
            
            # Wenn die Spalte leer ist.
            if row1[column] == ' ':

                # Ersetzt die leere Spalte durch das Zeichen
                row1[column] = mark

                # Beendet die Schleife, da sonst das ganze Feld mit dem jeweiligen Zeichen ausgefüllt wird.
                break
        elif row == 2:
            if row2[column] == ' ':
                row2[column] = mark
                break
        elif row == 3:
            if row3[column] == ' ':
                row3[column] = mark
                break

def win_check(mark):

    """
    
    Wenn Markierung im Feld Senkrecht ist:
    ['X',' ',' ']
    ['X',' ',' ']
    ['X',' ',' '] 
    
    """

    if mark in row1[0] and mark in row2[0] and mark in row3[0]:
        if mark == 'O':
            print('Spieler 2 hat gewonnen.')
            return True
        else:
            print('Spieler 1 hat gewonnen.')
            return True

    """
    
    Wenn Markierung im Feld Senkrecht ist:
    [' ','X',' ']
    [' ','X',' ']
    [' ','X',' '] 
    
    """

    if mark in row1[1] and mark in row2[1] and mark in row3[1]:
        if mark == 'O':
            print('Spieler 2 hat gewonnen.')
            return True
        else:
            print('Spieler 1 hat gewonnen.')
            return True

    """
    
    Wenn Markierung im Feld Senkrecht ist:
    [' ',' ','X']
    [' ',' ','X']
    [' ',' ','X'] 
    
    """

    if mark in row1[2] and mark in row2[2] and mark in row3[2]:
        if mark == 'O':
            print('Spieler 2 hat gewonnen.')
            return True
        else:
            print('Spieler 1 hat gewonnen.')
            return True

    """
    
    Wenn Markierung im Feld Waagerecht ist:
    ['X','X','X']
    [' ',' ',' ']
    [' ',' ',' '] 
    
    """

    if mark in row1[0] and mark in row1[1] and mark in row1[2]:
        if mark == 'O':
            print('Spieler 2 hat gewonnen.')
            return True
        else:
            print('Spieler 1 hat gewonnen.')
            return True

    """
    
    Wenn Markierung im Feld Waagerecht ist:
    [' ',' ',' ']
    ['X','X','X']
    [' ',' ',' '] 
    
    """

    if mark in row2[0] and mark in row2[1] and mark in row2[2]:
        if mark == 'O':
            print('Spieler 2 hat gewonnen.')
            return True
        else:
            print('Spieler 1 hat gewonnen.')
            return True

    """
    
    Wenn Markierung im Feld Waagerecht ist:
    [' ',' ',' ']
    [' ',' ',' ']
    ['X','X','X'] 
    
    """

    if mark in row3[0] and mark in row3[1] and mark in row3[2]:
        if mark == 'O':
            print('Spieler 2 hat gewonnen.')
            return True
        else:
            print('Spieler 1 hat gewonnen.')
            return True

    """
    
    Wenn Markierung im Feld Diagonal ist:
    ['X',' ',' ']
    [' ','X',' ']
    [' ',' ','X'] 
    
    """

    if mark in row1[0] and mark in row2[1] and mark in row3[2]:
        if mark == 'O':
            print('Spieler 2 hat gewonnen.')
            return True
        else:
            print('Spieler 1 hat gewonnen.')
            return True

    """
    
    Wenn Markierung im Feld Diagonal ist:
    [' ',' ','X']
    [' ','X',' ']
    ['X',' ',' '] 
    
    """

    if mark in row1[2] and mark in row2[1] and mark in row3[0]:
        if mark == 'O':
            print('Spieler 2 hat gewonnen.')
            return True
        else:
            print('Spieler 1 hat gewonnen.')
            return True

    """
    
    Wenn kein Feld mehr frei ist:
    ['X','O','X']
    ['X','O','O']
    ['O','X','X'] 
    
    """

    if ' ' not in row1 and ' ' not in row2 and ' ' not in row3:
        print('Unentschieden!')
        return True
    
    # Wenn keiner der oberen Fälle eintritt.
    else:
        print('Es wurde noch kein Gewinner nach dieser Runde festgestellt.')

    
def game(mark1, mark2):
    
    # Counter um die Spieler automatisch zu wechseln.
    counter = 1

    # Anzahl der Gespielten Runden.
    round = 0

    # Damit das Spiel dauerhaft läuft eine unendliche Schleife.
    while True:

        # Countervariable ist 1.
        if counter == 1:

            # Reihe auswählen.
            player_row = int(input('Spieler 1, bitte gebe die Reihe ein: '))

            # Spalte auswählen.
            player_column = int(input('Spieler 1, bitte die Spalte ein: '))

            # Eintragen des Zeichens in Reihe und Spalte (-1, damit die Eingaben 1 - 3 bleiben können).
            action(mark1, player_row, (player_column-1))
            
            # Ausgabe des Felds nach dem Zug.
            for i in rows:
                print(i)

            # Prüfen ob nach dem Zug gewonnen wurde.
            if win_check(mark1) == True:
                print('Ergebnis nach: {} Runden'.format(round))
                break

            # Counter wird um 1 erhöht, damit Spieler 2 beim nächsten Durchlauf der Whileschleife am Zug ist.
            counter += 1

            # Rundenanzahl wird um 1 erhöht.
            round += 1
        elif counter == 2:
            player_row = int(input('Spieler 2, bitte gebe die Reihe ein: '))
            player_column = int(input('Spieler 2, bitte die Spalte ein: '))
            action(mark2, player_row, (player_column-1))
            for i in rows:
                print(i)
            if win_check(mark2) == True:
                print('Ergebnis nach: {} Runden.'.format(round))
                break

            # Counter wird um 1 verringert, damit Spieler 1 beim nächsten Durchlauf der Whileschleife am Zug ist.
            counter -= 1
            round += 1


# Startet das Spiel mit den Zeichen für Spieler 1 und Spieler 2.
game(player1, player2)

# Gibt nach dem Spiel noch einmal das Feld aus.
for element in rows:
    print(element)

# Eingabeaufforderung, damit das Spiel sich nicht direkt nach dem Sieg eines Spielers schließt.
input('Drücke Eingabe zum Beenden.')


