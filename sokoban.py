'''
    Author: Salvador Hernandez Mendoza
    Date: 11/07/2019
    Description: Demo template for sokoban game

    Game simboles:
    0 - Character
    1 - floor
    2 - Wall
    3 - Box
    4 - Target
    5 - Box/Target
'''
class Sokoban:

    '''
        Global variables
    '''
    def __init__(self):
        self.map = [] # Game map
        self.position_x = 0 # Character position

    '''
        Create game level
    '''
    def createMap(self):
        self.map = [2,1,1,1,0,1,1,1,2] # Create the map

    '''
        Print the play map
    '''
    def printMap(self):
        print self.map # Print de map

    '''
        Search for the character position
    '''
    def foundCharacter(self):
        for i in range(len(self.map)): # Get the size of the map
            if self.map[i] == 0: # Evaluate if there is a character
                self.position_x = i # Save the character position

    '''
        Left movement rules
    '''
    def moveLeft(self):
        if self.map[self.position_x - 1] == 1: # Evaluate if the next character position is a floor
            tem_x = self.position_x # save the character position
            self.position_x = self.position_x -1 # update the character position
            self.map[tem_x] = 1 # put a floor
            self.map[self.position_x] = 0 # move the character to next position

    '''
        Right movement rules
    '''
    def moveRight(self):
        if self.map[self.position_x + 1] == 1: # Evaluate if the next character position is a floor
            tem_x = self.position_x # save the character position
            self.position_x = self.position_x + 1 # update the character position
            self.map[tem_x] = 1 # put a floor
            self.map[self.position_x] = 0 # move the character to next position

    '''
        Play the game - Main method of sokoban
    '''
    def play(self):
        self.createMap() # Call the map
        self.foundCharacter() # Update the character position
        while True: # Infinite loop
            self.printMap() # Call the printMap method
            move = raw_input("Move [a-left, d-right]")
            if move == 'a':
                self.moveLeft() # Call moveLeft rules
            elif move == 'd':
                self.moveRight() # Call moveRight rules
            elif move == 'q':
                break # Game quit

sax = Sokoban() # Create a object from Sokoban class
sax.play() # Fun Fun Fun ;)
