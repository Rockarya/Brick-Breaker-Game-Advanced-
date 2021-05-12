from random import randint
from Elements import Brick
from playsound import playsound

def wall_hit_sound():
	# Input an existing mp3 filename
	mp3File = "./sounds/brickhit.WAV"
	# Play the mp3 file
	playsound(mp3File)

class Bricks():
	def __init__(self,x,y,orignal,bricks,power,points,paddle,ball):
		self.x = x
		self.y = y
		self.orignal = orignal
		self.bricks = bricks
		self.power = power
		self.points = points
		self.paddle = paddle.paddle
		self.ball = ball.ball


	def Updated_Points(self,game):
		return self.points

	def Ball_Brick_Collision(self,game):
		x = self.ball.x
		y = self.ball.y
		dirx = self.ball.dirx
		diry = self.ball.diry
		
		flag = 0
		for pup in self.power:
			if pup.status == 1:
				if pup.ptype == 'T':
					flag = 1
				elif pup.ptype == 'A':
					flag = 2
					break

		for bri in self.bricks:
			if flag == 2:
				if (x + dirx == bri.x) and (y + diry == bri.y):
					# Break all the bricks surronding this brick and this brick too
					for i in range(-1,2):
						for j in range(-1,2):
							# Power-Up in any of the brick
							f = 0
							for pup in self.power:
								if pup.x == bri.x+j and pup.y == bri.y+i:
									f=1
									self.orignal[bri.y + i][bri.x + j] = pup.ptype
									pup.dirx = dirx
									pup.diry = diry
									break
							if f == 0:
								self.orignal[bri.y + i][bri.x + j] = ' '
					self.points += 50

					if diry == 1:	
						self.ball.diry*=(-1)
						self.ball.dirx*=(-1)
					else:
						self.ball.diry*=(-1)
					wall_hit_sound()

			else:
				# Unbreakable bricks
				if self.orignal[bri.y][bri.x] == 'U':
					if (x + dirx == bri.x) and (y + diry == bri.y):
						if flag == 1:
							self.orignal[bri.y][bri.x] = ' '
							self.points += 10

						if diry == 1:	
							self.ball.diry*=(-1)
							self.ball.dirx*=(-1)
						else:
							self.ball.diry*=(-1)
						wall_hit_sound()

				else:
					if (((x == bri.x) and (y + diry == bri.y)) or ((x + dirx == bri.x) and (y == bri.y)) or ((x + dirx == bri.x) and (y + diry == bri.y))) and self.orignal[bri.y][bri.x]!=' ':
						if self.orignal[bri.y][bri.x] == 'b3':
							if flag == 0:
								self.orignal[bri.y][bri.x]='b2'
								self.points += 3
							else:
								self.orignal[bri.y][bri.x]=' '
								self.points += 6

						elif self.orignal[bri.y][bri.x] == 'b2':
							if flag == 0:
								self.orignal[bri.y][bri.x]='b1'
								self.points +=2
							else:
								self.orignal[bri.y][bri.x]=' '
								self.points += 3

						elif self.orignal[bri.y][bri.x] == 'b1':
							f=0
							for pup in self.power:
								if pup.x == bri.x and pup.y == bri.y:
									f=1
									self.orignal[bri.y][bri.x] = pup.ptype
									pup.dirx = dirx
									pup.diry = diry

							if f==0:
								self.orignal[bri.y][bri.x] = ' '
							self.points +=1

						elif self.orignal[bri.y][bri.x] == 'r':
							if flag == 0:
								f = randint(1,3)
								if f==1:
									self.orignal[bri.y][bri.x] = 'b1'
									bri.btype = 'b1'
								elif f==2:
									self.orignal[bri.y][bri.x] = 'b2'
									bri.btype = 'b2'
								else:
									self.orignal[bri.y][bri.x] = 'b3'
									bri.btype = 'b3'
								self.points +=5
							else:
								self.orignal[bri.y][bri.x]=' '
								self.points += 10

						elif self.orignal[bri.y][bri.x] == '$':
							self.points += 50

							rx = 0
							while(self.orignal[bri.y][bri.x + rx] == '$'):
								self.orignal[bri.y][bri.x + rx] = ' '
								self.orignal[bri.y+1][bri.x + rx] = ' '
								self.orignal[bri.y-1][bri.x + rx] = ' '
								self.orignal[bri.y-1][bri.x + rx+1] = ' '
								self.orignal[bri.y-1][bri.x + rx-1] = ' '
								self.orignal[bri.y+1][bri.x + rx-1] = ' '
								self.orignal[bri.y+1][bri.x + rx+1] = ' '
								rx += 1

							# Input an existing mp3 filename
							mp3File = "./sounds/CRASHHAR.WAV"
							# Play the mp3 file
							playsound(mp3File)

							rx = -1
							while(self.orignal[bri.y][bri.x + rx] == '$'):
								self.orignal[bri.y][bri.x + rx] = ' '
								self.orignal[bri.y+1][bri.x + rx] = ' '
								self.orignal[bri.y-1][bri.x + rx] = ' '
								self.orignal[bri.y-1][bri.x + rx+1] = ' '
								self.orignal[bri.y-1][bri.x + rx-1] = ' '
								self.orignal[bri.y+1][bri.x + rx-1] = ' '
								self.orignal[bri.y+1][bri.x + rx+1] = ' '
								rx -= 1

						if (x == bri.x) and (y + diry == bri.y):
							self.ball.dirx*=(-1)
						elif (x + dirx == bri.x) and (y == bri.y):
							self.ball.diry*=(-1)
						else:
							self.ball.diry*=(-1)
							self.ball.dirx*=(-1)
						wall_hit_sound()
