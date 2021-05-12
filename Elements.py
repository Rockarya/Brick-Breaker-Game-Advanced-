from random import randint

# Parent class for Elements in game 
class Elements():
	def __init__(self,etype,x,y):
		self.etype = etype
		self.x = x
		self.y = y

# derived class for PowerUp
class PowerUp():
	def __init__(self,powtype,x,y):
		Elements.__init__(self,powtype,x,y)
		self.ptype = powtype
		self.previous = " "
		self.status = 0
		self.ptime = 100
		self.dirx = 0
		self.diry = 0
		# 100 secs of powerup and status will tell us that the power-up has to be kept activated or not?

# derived class for Paddle
class Paddle():
	def __init__(self,ptype):
		Elements.__init__(self,ptype,25,40)


# derived class for Ball
class Ball():
	def __init__(self,balltype,x,y):
		Elements.__init__(self,balltype,x,y)
		self.balltype = balltype
		if balltype == 'b':
			self.dirx=1
			self.diry=-1
			self.speed=1

		elif balltype == 'X':
			self.diry = 1

# derived class for Brick1
class Brick():
	def __init__(self,btype,x,y):
		Elements.__init__(self,btype,x,y)
	

# Stroing all the PowerUps in an array
def PowerUpArray(board,x,y):
	power = []
	a=0
	b=0
	# power.append(PowerUp('S',24,35))
	for i in range(8):
		while(1):
			a = randint(1,40)
			b = randint(5,7)
			if (board[b][a] == 'b1' or board[b][a] == 'b2' or board[b][a] == 'b3'):
				break
		ch = ''
		if i==0:
			ch = 'E'
		elif i==1:
			ch = 'S'
		elif i==2:
			ch = 'B'
		elif i==3:
			ch = 'F'
		elif i==4:
			ch = 'T'
		elif i==5:
			ch = 'P'
		elif i==6:
			ch = 'G'				#G: Shooting Paddle
		else:
			ch = 'A'				#A: Aaag (Fireball powerup)
		power.append(PowerUp(ch,a,b))

	return power

# Just a lazy optimization ;-)
def make_brick(a,b,bricks,board,flag):
	for i in range(1,11):
		for j in range(i):
			f = randint(1,4)
			ch = ''
			if f==1:
				ch = 'b1'
			elif f==2:
				ch = 'b2'
			elif f==3:
				ch = 'b3'
			else:
				ch = 'r'

			bricks.append(Brick(ch,a+flag*j,b-i))
			board[b-i][a+flag*j] = ch

	return bricks

# function to assign bricks to the board
def BricksArray(board,level,X,Y):
	bricks = []
	if level == 1:
		bricks = make_brick(5,15,bricks,board,1)
		bricks = make_brick(58,15,bricks,board,-1)


		a = 31
		b = 14
		for i in range(10):
			if i<5:
				for j in range(2*i+1):
					bricks.append(Brick('U',a-j+i,b-i))
					board[b-i][a-j+i] = 'U'

			elif i == 5:
				for j in range(2*i+1):
					bricks.append(Brick('$',a-j+i,b-i))
					board[b-i][a-j+i] = '$'

			else:
				for j in range(2*i+1):
					f = randint(1,4)
					ch = ''
					if f==1:
						ch = 'b1'
					elif f==2:
						ch = 'b2'
					elif f==3:
						ch = 'b3'
					else:
						ch = 'r'
					bricks.append(Brick(ch,a-j+i,b-i))
					board[b-i][a-j+i] = ch

	elif level == 2:
		a = 15
		b = 5
		num = 31
		for i in range(16):
			for j in range(num-2*i):
				f = randint(1,4)
				ch = ''
				if f==1:
					ch = 'b1'
				elif f==2:
					ch = 'b2'
				elif f==3:
					ch = 'b3'
				else:
					ch = 'r'

				if randint(1,15) == 1:
					ch = 'U'
				
				bricks.append(Brick(ch,a+j+i,b+2*i))
				board[b+2*i][a+j+i] = ch

		# Placing exploding bricks in between
		num = 7
		a = 27
		b = 6
		for i in range(4):
			for j in range(num-2*i):
				bricks.append(Brick('$',a+j+i,b+2*i))
				board[b+2*i][a+j+i] = '$'	

	else:
		# leftmost pos for ufo = 3 and rightmost pos is 41
		a = 23
		b = 3
		ufo = [['']*1000]*100
		ufo=[ 
		"    (0 0)_(0 0)",
		"      Y     Y",
		" _.-~===========~-._",
		"(__________________)",
		"______|_______|______",
		]

		for i in range(len(ufo)):
			for j in range(len(ufo[i])):
				if ufo[i][j]!=' ':
					board[b+i][a+j] = ufo[i][j]		

		b = 10
		for i in range(12):
			board[b][i] = '#'
			board[b][X-i-1] = '#'

		
	# These set of bricks are just used to test the power-ups
	# Take the right corner to explode the explode brick
	# a= 15
	# b= 35
	# for i in range(10):
	# 	bricks.append(Brick('b1',a+i,b))
	# 	board[b][a+i] = 'b1'

	return bricks