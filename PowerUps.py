from Elements import PowerUp
from playsound import playsound

def wall_hit_sound():
	# Input an existing mp3 filename
	mp3File = "./sounds/brickhit.WAV"
	# Play the mp3 file
	playsound(mp3File)

class PowerUps():
	def __init__(self,x,y,orignal,bricks,power,points,paddle,ball,brick):
		self.x = x
		self.y = y
		self.orignal = orignal
		self.bricks = bricks
		self.power = power
		self.points = points
		self.paddle = paddle.paddle
		self.ball = ball.ball
		self.brick = brick

		self.ShortPaddle = paddle.ShortPaddle
		self.LongPaddle = paddle.LongPaddle


	def Update_PowerUp(self,game):
		UP = 0
		DOWN = self.y -1
		LEFT = 0
		RIGHT = self.x-1	
		for pup in self.power:
			if self.orignal[pup.y][pup.x] == pup.ptype:

				if pup.y + 1 == self.y-1:
					self.orignal[pup.y][pup.x] = ' '
					self.power.remove(pup)

				# Only obstacle which will hinder is the ball only in path	
				elif self.orignal[pup.y + pup.diry][pup.x + pup.dirx] != 'b':
					if pup.y+pup.diry==DOWN or pup.y+pup.diry==UP:
						pup.diry*=(-1)
						wall_hit_sound()

					elif pup.x+pup.dirx==LEFT or pup.x+pup.dirx==RIGHT:
						pup.dirx*=(-1)
						wall_hit_sound()
						
					self.orignal[pup.y][pup.x] = pup.previous
					pup.previous = self.orignal[pup.y + pup.diry][pup.x + pup.dirx]
					self.orignal[pup.y + pup.diry][pup.x + pup.dirx] = pup.ptype
					pup.x += pup.dirx
					pup.y += pup.diry


	def Remove_PowerUp(self,game):
		for pup in self.power:
			if pup.status == 1:

				if pup.ptype == 'S' and pup.ptime == 100:
					self.orignal[self.LongPaddle.y][self.LongPaddle.x] = ' '
					self.orignal[self.paddle.y][self.paddle.x] = 'SP'
					self.orignal[self.ShortPaddle.y][self.ShortPaddle.x] = ' '
					self.ShortPaddle.y = self.paddle.y
					self.ShortPaddle.x = self.paddle.x
					self.orignal[self.y-3][self.x-5] = '#'
					self.orignal[self.y-3][self.x-10] = ' '
					self.orignal[self.y-3][self.x-15] = ' '

				if pup.ptype == 'E' and pup.ptime == 100:
					self.orignal[self.ShortPaddle.y][self.ShortPaddle.x] = ' '
					self.orignal[self.paddle.y][self.paddle.x] = 'LP'
					self.orignal[self.LongPaddle.y][self.LongPaddle.x] = ' '
					self.LongPaddle.y = self.paddle.y
					self.LongPaddle.x = self.paddle.x
					self.orignal[self.y-3][self.x-5] = ' '
					self.orignal[self.y-3][self.x-10] = ' '
					self.orignal[self.y-3][self.x-15] = '#'

				if pup.ptime == 0:
					if pup.ptype == 'S' or pup.ptype == 'E':
						if pup.ptype == 'S':
							self.orignal[self.ShortPaddle.y][self.ShortPaddle.x] = 'p'
							self.paddle.y = self.ShortPaddle.y
							self.paddle.x = self.ShortPaddle.x
							
						if pup.ptype == 'E':
							self.orignal[self.LongPaddle.y][self.LongPaddle.x] = 'p'
							self.paddle.y = self.LongPaddle.y
							self.paddle.x = self.LongPaddle.x

						self.orignal[self.y-3][self.x-5] = ' '
						self.orignal[self.y-3][self.x-10] = '#'
						self.orignal[self.y-3][self.x-15] = ' '

					pup.status = 0
					self.power.remove(pup)
				else:
					pup.ptime -= 1
