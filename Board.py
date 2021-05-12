import random, sys, os, time, copy 
from random import randint
from Block import Block
from termcolor import *
import colorama
colorama.init()


class Board():
	def __init__(self,x,y,orignal,bricks,power,points,paddle,ball,brick,powerup):
		self.x = x
		self.y = y
		self.orignal = orignal
		self.bricks = bricks
		self.power = power
		self.points = points
		self.paddle = paddle.paddle
		self.ball = ball.ball
		self.brick = brick
		self.powerup = powerup

		self.block = Block()
		
	def Updated_Power_Array(self,game):
		return self.power

	def Updated_org_Array(self,game):
		return self.orignal

	def Updated_Bricks_Array(self,game):
		return self.bricks
	
	def display(self):
		for i in range(self.y):
			for j in range(self.x):
				cprint(self.block.getBlock(self.orignal[i][j]),self.block.getColor(self.orignal[i][j]),attrs=['bold'],end='')		
			print(" ")	