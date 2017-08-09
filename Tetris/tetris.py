import pygame
import random
import time
import sys
from pygame import font
from tetris_header import *
from tetris_message import *
from tetris_block import *
from tetris_board import *

class GamePlay(Message,Block,Board):
    	def __init__(self):
		Message.__init__(self)
		Block.__init__(self)
		Board.__init__(self)

		f = open('bestscore.txt','r')
		self.bestscore = f.read()
		f.close()
		if self.bestscore[-1] == '\n':
			self.bestscore = self.bestscore[:-1]

		#pygame.key.set_repeat(250,25)
		self.next_block = shapes[random.randrange(0,len(shapes))]
		self.selectPiece()

		pygame.time.set_timer(pygame.USEREVENT+1,1000)

	def selectPiece(self):
		self.block = self.next_block[:]
		self.next_block = shapes[random.randrange(0,len(shapes))]
		self.block_x = int(column/ 2 - len(self.block[0])/2)
		self.block_y = 0

		if checkPiecePos(self.board,self.block,(self.block_x, self.block_y)):
			self.gameOver = True

	def updateScore(self, val):
		self.score += val

	def start(self):
        	self.gameOver = False
        	clock = pygame.time.Clock()

        	while True:
            		#self.gameDisplay.fill(black)
            		if self.gameOver:
				#self.gameDisplay.fill(black)
				self.message("GAME OVER",red,(self.display_width/2-2*block_size,self.display_height/4))
				self.message("SCORE: %d"%(self.score),red,(self.display_width/2-2*block_size,self.display_height/4+2*block_size))

				if self.highscore < self.score:
					self.highscore = self.score

				if self.bestscore < str(self.score):
					self.bestscore = str(self.score)

					z = open('bestscore.txt','w')
					z.write(self.bestscore)

				self.message_to_screen("Press C to Play Again or Q to quit" ,red)
				for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_c:
							self.gameOver = False
							self.board = newBoard()
							self.selectPiece()
							self.level = 1
							self.score = 0
						elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
							self.Exit()


		    	for event in pygame.event.get():
				if event.type == pygame.USEREVENT+1:
					self.fall()
		        	elif event.type == pygame.QUIT:
					self.Exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
						self.Exit()

					if event.key == pygame.K_a or event.key == pygame.K_LEFT:
						self.moveLeft()

					if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
						self.moveRight()

					if event.key == pygame.K_s or event.key == pygame.K_UP:
						self.rotate(self.block)

					if event.key == pygame.K_SPACE:
						self.fastFall()

					if event.key == pygame.K_DOWN:
						self.fall()


		    	clock.tick(FPS)

pygame.init()
#pygame.mixer.music.load("sound.ogg")
#pygame.mixer.music.play(-1)
Game = GamePlay()
#Game.start()
