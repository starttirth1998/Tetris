import pygame
from tetris_header import *

def newBoard():
	board = [ [ 0 for x in range(column) ] for y in range(row) ]
	board += [[ 1 for x in range(column)]]
	return board

def checkPiecePos(board, shape, cor):
	x, y = cor
	for shape_y, row in enumerate(shape):
		for shape_x, val in enumerate(row):
			if val and board[shape_y+y][shape_x+x]:
				return True
	return False

def removeRow(board, row):
	del board[row]
	return [[0 for i in range(column)]] + board

def fillPiecePos(board, shape, cor):
	x, y = cor
	for shape_y, row in enumerate(shape):
		for shape_x, val in enumerate(row):
			board[shape_y+y-1][shape_x+x] += val
	return board

class Board(object):
	def __init__(self):

		self.background = [ [ 9 if x%2 == y%2 else 10 for x in range(column)] for y in range(row)]
		self.level = 1
		self.score = 0
		self.highscore = 0

		self.display_width = block_size*(column+10)
		self.display_height = block_size*row
		#self.gameDisplay = pygame.display.set_mode((self.display_width,self.display_height))

		pygame.display.set_caption('Tetris')

		self.display_screen = block_size*column

		self.board = newBoard()
