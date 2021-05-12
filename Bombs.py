from Elements import Ball
from playsound import playsound
import random, sys, os, time, copy, signal


def wall_hit_sound():
	# Input an existing mp3 filename
	mp3File = "./sounds/brickhit.WAV"
	# Play the mp3 file
	playsound(mp3File)

class Bombs():
	def __init__(self,x,y,orignal,bricks,power,paddle,ball,level,ufo_x,ufo_y,ufo_health):
		self.x = x
		self.y = y
		self.orignal = orignal
		self.bricks = bricks
		self.power = power
		self.paddle = paddle.paddle
		self.ball = ball.ball
		self.level = level
		self.ufo_x = ufo_x
		self.ufo_y = ufo_y
		self.ufo_health = ufo_health
		self.SAVAGE_FLAG1 = 0
		self.SAVAGE_FLAG2 = 0


		self.bomb = Ball('X',self.ufo_x,self.ufo_y)

		if self.level == 3:
			self.orignal[self.bomb.y][self.bomb.x] = self.bomb.balltype


	def updatedhealth(self,game):
		return self.ufo_health

	def savage_bricks(self,game):
		# Adding a new sign of +
		if self.ufo_health == 150 and self.SAVAGE_FLAG1 == 0:
			# Putting the defensive bricks at y = 9
			self.SAVAGE_FLAG1 = 1
			for i in range(1,self.x-1):
				self.orignal[9][i] = '+'

		if self.ufo_health == 100 and self.SAVAGE_FLAG2 == 0:
			# Putting the defensive bricks at y = 9
			self.SAVAGE_FLAG2 = 1
			for i in range(1,self.x-1):
				self.orignal[9][i] = '+'


	def bombfall(self,game):
		y = self.bomb.y
		x = self.bomb.x
		diry = self.bomb.diry

		if y + diry == self.paddle.y:
			f = 0
			for i in range(10):		
				if self.paddle.x + i == x:
					f = 1
					break

			self.orignal[y][x] = ' '
			if f==1:
				self.orignal[self.paddle.y][self.paddle.x] = ' '
				self.orignal[self.ball.y][self.ball.x] = ' '
				self.orignal[self.y-3][self.x-5] = ' '
				self.orignal[self.y-3][self.x - 10] = '#'
				self.orignal[self.y-3][self.x-15] = ' '		
				game.gameOver()

			else:
				self.bomb.y = self.ufo_y
				self.bomb.x = self.ufo_x
				self.orignal[self.bomb.y][self.bomb.x] = 'X'

		elif self.orignal[y+diry][x] == '+':
			self.orignal[y][x] = ' '
			self.orignal[y+diry+1][x] = 'X'
			self.bomb.y = y + diry +1

		else:
			self.orignal[y][x] = ' '
			self.orignal[y+diry][x] = 'X'
			self.bomb.y = y + diry


	def ball_ufo_collision(self,game):
		x = self.ball.x
		y = self.ball.y
		UP = 0
		DOWN = self.y -1
		LEFT = 0
		RIGHT = self.x-1	

		dirx = self.ball.dirx
		diry = self.ball.diry
		speed = self.ball.speed

		IS_GAMEOVER_FLAG = 0
		f = 0
		k=0
		# flag will be non-zero if ball collides the paddle.On colliding paddle we need to change the ball speed and if flag is 0 that means ball is in air
		flag=0
		for i in range(1,speed+1):
			# No need to make a change here as y co=ordinate of all types of paddle will remain same
			if self.orignal[y+i*diry][x+i*dirx] == ' ' and y+i*diry < self.paddle.y:
				k+=1
			else:
				break

		self.orignal[y][x] = ' '
		self.orignal[y+k*diry][x+k*dirx] = 'b'
		self.ball.x = x + k*dirx
		self.ball.y = y + k*diry

		for _ in range(k+1,speed+1):

			x = self.ball.x
			y = self.ball.y
			dirx = self.ball.dirx
			diry = self.ball.diry
	
			if y+diry == self.paddle.y:
				f=0
				for i in range(10):			#Taking width of paddle for a total of lenght 10
					if (self.paddle.x + i == x) or (self.paddle.x + i+1 == x):
						f=1
						# Input an existing mp3 filename
						mp3File = "./sounds/hit.WAV"
						# Play the mp3 file
						playsound(mp3File)

						self.ball.diry*=(-1)

						# Only 5 values of i are possible that's why skipped other positions(see the i+=1 thing)
						if i==0 or i==8:
							flag = 3
						elif i==2 or i==6:
							flag = 2
						else:
							flag = 1

						i+=1
						break
				if f==0:
					self.orignal[y][x] = ' '
					self.orignal[self.paddle.y][self.paddle.x] = ' '
					IS_GAMEOVER_FLAG = 1
					game.gameOver()		


			elif self.orignal[y + diry][x + dirx] == ' ':
				self.orignal[y][x] = ' '
				self.ball.x = x + dirx
				self.ball.y = y + diry
				self.orignal[y + diry][x + dirx] = 'b'

			elif y+diry==DOWN or y+diry==UP:
				self.ball.diry*=(-1)
				wall_hit_sound()

			elif x+dirx==LEFT or x+dirx==RIGHT:
				self.ball.dirx*=(-1)
				wall_hit_sound()

			elif self.orignal[y+diry][x+dirx] == '+':
				self.orignal[y+diry][x+dirx] = ' '
				self.ball.diry*=(-1)
				wall_hit_sound()

			elif self.orignal[y][x+dirx] == '+':
				self.orignal[y][x+dirx] = ' '
				self.ball.dirx*=(-1)
				wall_hit_sound()

			elif self.orignal[y+diry][x] == '+':
				self.orignal[y+diry][x] = ' '
				self.ball.diry*=(-1)
				wall_hit_sound()
				
			else:
				if diry == 1:	
					self.ball.diry*=(-1)
					self.ball.dirx*=(-1)
				else:
					self.ball.diry*=(-1)
				wall_hit_sound()

		# upper than position of unbreakable bricks
		if self.ball.y < 10:
			self.ufo_health = self.ufo_health - 1
			if self.ufo_health == 0:
				game.gameWon()
				sys.exit()

		if flag!=0:
			self.ball.speed = flag
		
		return f

	def moveUFO(self,game,dirx):
		# UFO height is from y=3 to y=7  
		for i in range(3,8):
			for j in range(2,self.x-1):
				if self.orignal[i][j] != 'b':
					if dirx == -1 and self.paddle.x > 1:
						self.orignal[i][j + dirx] = self.orignal[i][j]
					elif dirx == 1 and self.paddle.x < self.x - 11:
						self.orignal[i][self.x -j] = self.orignal[i][self.x - j -1]

		if dirx == -1 and self.paddle.x > 1:
			self.ufo_x -= 1
		elif dirx == 1 and self.paddle.x < self.x - 11:
			self.ufo_x += 1
