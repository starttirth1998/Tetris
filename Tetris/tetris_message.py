import pygame
from tetris_header import *

class Message(object):
	def __init__(self):
		self.font = pygame.font.SysFont(None, 25)

	def text_objects(self,text,color):
		textSurface = self.font.render(text,True,color)
		return textSurface,textSurface.get_rect()

	def message_to_screen(self,msg, color):
		textSurf, textRect = self.text_objects(msg,color)
		textRect.center = (self.display_width/2),(self.display_height/2)
		#self.gameDisplay.blit(textSurf,textRect)

	def message(self,msg,color,cor):
		x,y = cor
		screen_text = self.font.render(msg,True,color)
		#self.gameDisplay.blit(screen_text,[x,y])

	def side_bar(self):
		self.message("Next Block:",red,(self.display_screen+column/2,self.display_height/4))
		self.message("Score: %d" % (self.score),red,(self.display_screen+column/2,1.75*row))
		self.message("HighScore: %d" %(self.highscore),green,(self.display_screen+column/2,2.5*row))
		self.message("BestScore: %s" %(self.bestscore),blue,(self.display_screen+column/2,3.25*row))
		self.message("Level: %d" %(self.level),red,(self.display_screen+column/2,row))
		self.message("INSTRUCTION:",red,(self.display_screen+column/2,self.display_height/2))
		self.message("A : Move Left",red,(self.display_screen+column/2,self.display_height/2+block_size))
		self.message("D : Move Right",red,(self.display_screen+column/2,self.display_height/2+2*block_size))
		self.message("S : Rotate Block",red,(self.display_screen+column/2,self.display_height/2+3*block_size))
		self.message("SPACE : Fast Fall",red,(self.display_screen+column/2,self.display_height/2+4*block_size))
		self.message("ARROW KEYS:",red,(self.display_screen+column/2,self.display_height/2+7*block_size))
		self.message("LEFT : Move Left",red,(self.display_screen+column/2,self.display_height/2+8*block_size))
		self.message("RIGHT : Move Right",red,(self.display_screen+column/2,self.display_height/2+9*block_size))
		self.message("UP : Rotate",red,(self.display_screen+column/2,self.display_height/2+10*block_size))
		self.message("DOWN : Move Down",red,(self.display_screen+column/2,self.display_height/2+11*block_size))
