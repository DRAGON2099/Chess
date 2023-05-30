'''
Main Driver File,responsible for handling user input and displaying current GameState object. 
'''

import pygame as p
import chess_engine

WIDTH = HEIGHT = 512
DIMENSION = 8 #8x8 Grid 
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #For animations 
IMAGES = {}

'''
Initializing a global dictionary of images. This will be called exactly once in the main.
'''
def load_images():
    pieces = ["wp","wR","wN","wB","wQ","wK","bp","bR","bN","bB","bQ","bK"]
    for piece in pieces:
        IMAGES['piece'] = p.transform.scale(p.image.load("images/" + piece + ".png"),(SQ_SIZE,SQ_SIZE)) 
        #we access an image by IMAGES['piece']

'''
#The main driver for our code. This will handle user input and the graphics.
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = chess_engine.game_state()
    load_images() #only do this once before the while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT():
                running = False

        draw_game_state(screen, gs)
        clock.tips(MAX_FPS)
        p.display.flip()

#Resposible for drawing the graphics within current game state
def draw_game_state(screen, gs):
    draw_board(screen) #draws squares on the board
    draw_pieces(screen, gs.board) #draw pieces on top of these squares

'''Draw the squares on the board'''
def draw_board(screen):
    pass
'''Draw the pieces on the board using the current game_state.board'''
def draw_pieces(screen, board):
    pass

if __name__ == "__main__":
    main()











