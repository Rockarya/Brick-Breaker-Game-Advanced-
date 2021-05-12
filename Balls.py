from Elements import Ball
import random, sys, os, time, copy, signal
from playsound import playsound

def wall_hit_sound():
	# Input an existing mp3 filename
	mp3File = "./sounds/brickhit.WAV"
	# Play the mp3 file
	playsound(mp3File)

class Balls():
	def __init__(self,x,y,orignal,bricks,power,points,paddle):
		self.x = x
		self.y = y
		self.orignal = orignal
		self.bricks = bricks
		self.power = power
		self.points = points
		self.paddle = paddle.paddle
		self.ShortPaddle = paddle.ShortPaddle
		self.LongPaddle = paddle.LongPaddle
	
		self.ball = Ball('b',self.paddle.x+5,self.paddle.y-1)

		self.orignal[self.ball.y][self.ball.x] = self.ball.balltype

	def Ball_on_Paddle(self,game):
		paddle_flag = 0
		for pup in self.power:
			if pup.ptype == 'S' and pup.status == 1:
				paddle_flag = -1
			elif pup.ptype == 'E' and pup.status == 1:
				paddle_flag = 1

		if paddle_flag == 0:
			if self.ball.x != self.paddle.x:
				self.orignal[self.ball.y][self.ball.x] = ' '

				self.ball.y = self.paddle.y - 1
				self.ball.x = self.paddle.x + 5
				self.orignal[self.ball.y][self.ball.x] = 'b'

		elif paddle_flag == -1:
			if self.ball.x != self.ShortPaddle.x:
				self.orignal[self.ball.y][self.ball.x] = ' '

				self.ball.y = self.ShortPaddle.y - 1
				self.ball.x = self.ShortPaddle.x + 3
				self.orignal[self.ball.y][self.ball.x] = 'b'

		else:
			if self.ball.x != self.LongPaddle.x:
				self.orignal[self.ball.y][self.ball.x] = ' '

				self.ball.y = self.LongPaddle.y - 1
				self.ball.x = self.LongPaddle.x + 8
				self.orignal[self.ball.y][self.ball.x] = 'b'


	def Update_Flag(self,game):
		paddle_flag = 0
		for pup in self.power:
			if pup.ptype == 'S' and pup.status == 1:
				paddle_flag = -1
			elif pup.ptype == 'E' and pup.status == 1:
				paddle_flag = 1

		flag = 1
		for pup in self.power:
			if (pup.ptype == 'P') and (pup.status == 1):
				if (paddle_flag == 0) and (self.ball.y+self.ball.diry == self.paddle.y):
					for i in range(10):			
						if self.paddle.x + i == self.ball.x:
							flag = 0
							break
				elif (paddle_flag == -1) and (self.ball.y+self.ball.diry == self.ShortPaddle.y):
					for i in range(5):			
						if self.ShortPaddle.x + i == self.ball.x:
							flag = 0
							break
				elif (paddle_flag == 1) and (self.ball.y+self.ball.diry == self.LongPaddle.y):
					for i in range(15):			
						if self.LongPaddle.x + i == self.ball.x:
							flag = 0
							break
		return flag


	def moveBall(self,game):
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
		paddle_flag = 0
		for pup in self.power:
			if pup.ptype == 'S' and pup.status == 1:
				paddle_flag = -1
			elif pup.ptype == 'E' and pup.status == 1:
				paddle_flag = 1		

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

			if paddle_flag == 0:	
				if y+diry == self.paddle.y:
					f=0
					for i in range(10):			#Taking width of paddle for a total of lenght 10
						if (self.paddle.x + i == x) or (self.paddle.x + i+1 == x):
							f=1
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


			elif paddle_flag == -1:
				if y+diry == self.ShortPaddle.y:
					f=0
					for i in range(5):			
						if self.ShortPaddle.x + i == x:
							f=1
							self.ball.diry*=(-1)

							if i==0 or i==4:
								flag = 3
							elif i==1 or i==3:
								flag = 2
							else:
								flag = 1

							break
					if f==0:
						self.orignal[y][x] = ' '
						self.orignal[self.ShortPaddle.y][self.ShortPaddle.x] = ' '
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

			else:
				if y+diry == self.LongPaddle.y:
					f=0
					for i in range(15):			
						if (self.LongPaddle.x + i == x) or (self.LongPaddle.x + i+1 == x) or (self.LongPaddle.x + i+2 == x):
							f=1
							self.ball.diry*=(-1)

							if i==0 or i==12:
								flag = 3
							elif i==3 or i==9:
								flag = 2
							else:
								flag = 1

							i+=2
							break;
					if f==0:
						self.orignal[y][x] = ' '
						self.orignal[self.LongPaddle.y][self.LongPaddle.x] = ' '
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


		# Power-Up enabler
		for pup in self.power:
			if pup.y + 1 == self.paddle.y:
				for i in range(10 + 5*paddle_flag):
					if self.paddle.x + i == pup.x and pup.status == 0:
						self.orignal[pup.y][pup.x] = ' '
						pup.status = 1
						# Input an existing mp3 filename
						mp3File = "./sounds/M_YEAH.WAV"
						# Play the mp3 file
						playsound(mp3File)
						break


		if IS_GAMEOVER_FLAG == 1:
			self.orignal[self.y-3][self.x-5] = ' '
			self.orignal[self.y-3][self.x - 10] = '#'
			self.orignal[self.y-3][self.x-15] = ' '
			# removing power-ups if game get's over
			for pup in self.power:
				if self.orignal[pup.y][pup.x] == pup.ptype:
					self.orignal[pup.y][pup.x] = ' '
					self.power.remove(pup)
				# removing acquired power-up after life-loss
				if pup.status == 1:
					pup.status = 0
					self.power.remove(pup)

		# Assigning ball-speed if status is 1
		for pup in self.power:
			if pup.ptype == 'F' and pup.status == 1:
				flag = 5

		if flag!=0:
			self.ball.speed = flag

		# This f value will tell that ball striked the paddle or not(falling bricks triggered if ball strikes the padlle)
		return f