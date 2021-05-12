from Elements import Paddle

class Paddles():
	def __init__(self,x,y,orignal,bricks,power,points,level):
		self.x = x
		self.y = y
		self.orignal = orignal
		self.bricks = bricks
		self.power = power
		self.points = points
		self.level = level

		self.paddle = Paddle('p')
		self.ShortPaddle = Paddle('SP')
		self.LongPaddle = Paddle('LP')

		self.orignal[self.paddle.y][self.paddle.x] = self.paddle.etype


	def movePaddle(self,game,dirx):
		direction = dirx//abs(dirx)  

		paddle_flag = 0
		for pup in self.power:
			if pup.ptype == 'S' and pup.status == 1:
				paddle_flag = -1
			elif pup.ptype == 'E' and pup.status == 1:
				paddle_flag = 1

		if paddle_flag == 0:
			x = self.paddle.x
			y = self.paddle.y
			k = 0
			for i in range(1,1+abs(dirx)):
				if self.orignal[y][x + i*direction] == ' ': 
					k+=1
				else:
					break

			self.orignal[y][x] = ' '
			self.paddle.x = x + k*direction
			self.paddle.y = y 
			self.orignal[self.paddle.y][self.paddle.x] = 'p'

		elif paddle_flag == -1:
			x = self.ShortPaddle.x
			y = self.ShortPaddle.y
			k = 0
			for i in range(1,1+abs(dirx)):
				if self.orignal[y][x + i*direction] == ' ': 
					k+=1
				else:
					break

			self.orignal[y][x] = ' '
			self.ShortPaddle.x = x + k*direction
			self.ShortPaddle.y = y 
			self.orignal[self.ShortPaddle.y][self.ShortPaddle.x] = 'SP'

		else:
			x = self.LongPaddle.x
			y = self.LongPaddle.y
			k = 0
			for i in range(1,1+abs(dirx)):
				if self.orignal[y][x + i*direction] == ' ': 
					k+=1
				else:
					break

			self.orignal[y][x] = ' '
			self.LongPaddle.x = x + k*direction
			self.LongPaddle.y = y 
			self.orignal[self.LongPaddle.y][self.LongPaddle.x] = 'LP'