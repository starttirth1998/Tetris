import pygame
import time,sys
from tetris_header import *
from tetris_board import *

class Block(object):
	def addLines(self):
		self.updateScore(10)
		if self.score >= self.level*100:
			self.level += 1
			speed_up = 1000-100*(self.level-1)
			if speed_up < 100:
				speed_up = 100
			pygame.time.set_timer(pygame.USEREVENT+1,speed_up)

	def fall(self):
		if not self.gameOver:
			self.block_y += 1
			if checkPiecePos(self.board,self.block,(self.block_x,self.block_y)):
				self.board = fillPiecePos(self.board,self.block,(self.block_x,self.block_y))
				self.selectPiece()
				while True:
					for i,rows in enumerate(self.board[:-1]):
						if 0 not in rows:
							self.board = removeRow(self.board,i)
							self.updateScore(100)
							break
					else:
						break
				self.addLines()
				return True
		return False

	def Exit(self):
		#self.gameDisplay.fill(white)
		self.message_to_screen("Thanks for playing",red)
		pygame.display.update()
		time.sleep(0.5)
		sys.exit()

	def fastFall(self):
		while(not self.fall()):
			a=1

	def rotate(self,piece):
		selectPiece = [ [ piece[y][x] for y in range(len(piece)) ] for x in range(len(piece[0]) - 1, -1, -1) ]
		if not checkPiecePos(self.board,selectPiece,(self.block_x,self.block_y)):
			self.block = selectPiece

	def moveLeft(self):
		check_x = self.block_x - 1
		if check_x < 0:
			check_x = 0
		if not checkPiecePos(self.board,self.block,(check_x,self.block_y)):
			self.block_x = check_x

	def moveRight(self):
		check_x = self.block_x + 1
		if check_x > column - len(self.block[0]):
			check_x = column - len(self.block[0])
		if not checkPiecePos(self.board,self.block,(check_x,self.block_y)):
			self.block_x = check_x

	def draw(self, matrix, cor):
		cor_x, cor_y  = cor
		for y, row in enumerate(matrix):
			for x, val in enumerate(row):
				if val:
					pygame.draw.rect(self.gameDisplay,colors[val],pygame.Rect((cor_x+x)*block_size,(cor_y+y)*block_size,block_size,block_size),0)
