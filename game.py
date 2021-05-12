from Board import Board 
from Paddles import Paddles
from Balls import Balls
from Bricks import Bricks
from PowerUps import PowerUps 
from Bombs import Bombs
from Elements import BricksArray, PowerUpArray
from drawings import instructions , thankyou, trophy
from termcolor import *
import colorama
colorama.init()
import random, sys, os, time, copy, signal
from playsound import playsound

try:
	import tty, termios
except ImportError:
	try:
		import msvcrt
	except ImportError:
		raise ImportError('getch not available')
	else:
		getch = msvcrt.getch
else:
	def getch():
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

def alarmHandler(signum, frame):
	raise AlarmException

class AlarmException(Exception):
	pass

class Game():
	# __init__ is a constructor and is used to initalize the attributes of the class.
	def __init__(self,f,hit_paddle,TIME,X,Y,orignal,BRICK,POWER,points,level,level_time,ufo_x,ufo_y,ufo_health):
		# Thses all written below are instance variables
		# methods are the functions which are defined in the class to manipulate these attributes
		# self is an object
		self.x = X
		self.y = Y
		self.f = f
		self.hit_paddle = hit_paddle
		self.orignal = orignal
		self.bricks = BRICK
		self.power = POWER
		self.points = points
		self.level = level
		self.level_time = level_time
		self.ufo_x = ufo_x
		self.ufo_y = ufo_y
		self.ufo_health = ufo_health
		self.paddle = Paddles(self.x,self.y,self.orignal,self.bricks,self.power,self.points,self.level)
		self.ball = Balls(self.x,self.y,self.orignal,self.bricks,self.power,self.points,self.paddle)
		self.bomb = Bombs(self.x,self.y,self.orignal,self.bricks,self.power,self.paddle,self.ball,self.level,self.ufo_x,self.ufo_y,self.ufo_health)
		self.brick = Bricks(self.x,self.y,self.orignal,self.bricks,self.power,self.points,self.paddle,self.ball)
		self.powerup = PowerUps(self.x,self.y,self.orignal,self.bricks,self.power,self.points,self.paddle,self.ball,self.brick)
		self.board = Board(self.x,self.y,self.orignal,self.bricks,self.power,self.points,self.paddle,self.ball,self.brick,self.powerup)
		self.time = TIME
		self.GAMEOVER = False


	def input(self,timeout=1):
		signal.signal(signal.SIGALRM, alarmHandler)
		signal.alarm(timeout)	
		
		try:
			inp = getch()
			signal.alarm(0)

			if inp == 'q':
				sys.exit()

			# Level-Up
			if inp == 'l':
				return 'l'

			if inp == 'p':
				getch()	
	
			if inp == 'a':			
				self.paddle.movePaddle(self,-2)
				if self.level == 3:
					self.bomb.moveUFO(self,-1)

			elif inp == 'd':		
				self.paddle.movePaddle(self,2)
				if self.level == 3:
					self.bomb.moveUFO(self,1)			

			elif inp == 's':		
				self.f=1	

			else:
				pass 

			return ''	

		except AlarmException:
			signal.signal(signal.SIGALRM, signal.SIG_IGN)
			return ''

	def update(self):
		self.time += 1
		self.level_time += 1

		# Sound for hitting the paddle is already in bombs.py file
		if self.level == 3:
			self.bomb.savage_bricks(self)
			self.bomb.bombfall(self)
			if self.f == 1:
				self.hit_paddle = self.bomb.ball_ufo_collision(self)
			else:
				self.ball.Ball_on_Paddle(self)

		else:
			self.brick.Ball_Brick_Collision(self)
			self.powerup.Update_PowerUp(self)
			self.powerup.Remove_PowerUp(self)

			if self.f == 1:
				self.hit_paddle =self.ball.moveBall(self)
				self.f = self.ball.Update_Flag(self)
			else:
				self.ball.Ball_on_Paddle(self)

			if self.hit_paddle == 1:
				# Input an existing mp3 filename
				mp3File = "./sounds/hit.WAV"
				# Play the mp3 file
				playsound(mp3File)

				# Falling bricks
				if self.level_time > 500:
					for i in reversed(range(self.y-4)):
						for j in range(1, self.x-2):
							if (self.orignal[i][j] == 'b1') or (self.orignal[i][j] == 'b2') or (self.orignal[i][j] == 'b3') or (self.orignal[i][j] == 'U') or (self.orignal[i][j] == '$') or (self.orignal[i][j] == 'r'):
								# self.y -5 is 1 level above of ball(here games get over)
								if i == self.y - 5:
									thankyou()
									sys.exit()

								self.orignal[i+1][j] = self.orignal[i][j]
								self.orignal[i][j] = ' '

		os.system("clear")

	def updatedboard(self):
		return self.board.Updated_org_Array(self)


	def updatedbricks(self):
		return self.board.Updated_Bricks_Array(self)

	def updatedpoints(self):
		return self.brick.Updated_Points(self)


	def updatedpower(self):
		return self.board.Updated_Power_Array(self)

	def updatedhealth(self):
		return self.bomb.updatedhealth(self)

	def gameOver(self):
		os.system("clear")
		self.board.display()
		# Input an existing mp3 filename
		mp3File = "./sounds/Gameover.mp3"
		# Play the mp3 file
		playsound(mp3File)
		if self.level == 3:
			print("Bomb exploded on you :-(")
		else:
			print("Ball missed the paddle :-(")

		self.GAMEOVER = True
		print("Press any key to continue")
		getch()
	

	def gameWon(self):
		print("Congrats you won the game")
		trophy()	
		# Input an existing mp3 filename
		mp3File = "./sounds/game_won.WAV"
		# Play the mp3 file
		playsound(mp3File)
		getch()

	def scoreboard(self):
		print("Lives:",end='')
		for _ in range(lives):
			cprint("\u2764 ",'red',attrs=['bold'],end='')
		
		points=self.brick.Updated_Points(self)
		print("     Level:",self.level,"     SCORE:",points,"     time:",self.time)

		if self.level == 3:
			ufo_health = self.bomb.updatedhealth(self)
			maxHealth = 200    # Max Health
			healthDashes = 37  # Max Displayed dashes

			
			dashConvert = int(maxHealth/healthDashes)            # Get the number to divide by to convert health to dashes (being 10)
			currentDashes = int(ufo_health/dashConvert)              # Convert health to dash count: 80/10 => 8 dashes
			remainingHealth = healthDashes - currentDashes       # Get the health remaining to fill as space => 12 spaces

			healthDisplay = '-' * currentDashes                  # Convert 8 to 8 dashes as a string:   "--------"
			remainingDisplay = ' ' * remainingHealth             # Convert 12 to 12 spaces as a string: "            "
			percent = str(int((ufo_health/maxHealth)*100)) + "%"     # Get the percent as a whole number:   40%

			print("UFO Health:  ",end='')
			print("|" + healthDisplay + remainingDisplay + "|")  # Print out textbased healthbar
			print("                             " + percent)                    


# This function is used to create the raw board for each new level  
def create_raw_board(X, Y, orignal):
    orignal = [ [' ' for j in range(X)] for i in range(Y)]
    orignal[0] = ['#']*X
    orignal[Y-1] = ['#']*X
    
    for j in range(1, Y-1):
        for i in range(X):
            if j==Y-3:
                if i==0 or i==X-10:
                    orignal[j][i] = '#'
                else:
                    orignal[j][i] = ' '
            else:
                if i==0 or i==X-1:
                    orignal[j][i] = '#'
                else:
                    orignal[j][i] = ' '
    return orignal
       
     

if __name__ == "__main__":

	# Input an existing mp3 filename
	mp3File = "./sounds/Logo.mp3"
	# Play the mp3 file
	playsound(mp3File)
	instructions()
	getch()

	points = 0 
	lives = 3 
	TIME = 0
	level_time = 0		#The time spent in each level(will be used for handling falling bricks)
	level = 1
	new_level_flag = 0

	# position of ufo
	ufo_x = 32
	ufo_y = 8
	ufo_health = 200

	# BOARD SIZE
	X = 65
	Y = 43
	orignal = [[' ']*100]*100
	orignal = create_raw_board(X, Y, orignal)


	BRICK=BricksArray(orignal,level,X,Y)
	POWER=PowerUpArray(orignal,X,Y)


	while lives > 0:
	 	# hard coding to remove ball from the scene(not able to remove)
		if level == 3:
			for i in range(Y):
				for j in range(X):
					if orignal[i][j] == 'b' or orignal[i][j]=='X':
						orignal[i][j] = ' '


		os.system("clear")
		# Flag f=0 indicates that ball should be on paddle.When f is rasised to 1 then it means that ball can move freely now
		f=0
		# This hit_paddle will determine if ball hits the paddle or not
		hit_paddle = 0
		if new_level_flag == 1:
			new_level_flag = 0
			level += 1
			if level == 4:
				game.gameWon()
				break
			else:
				level_time = 0		#New level is getting started so make it's level time to be 0
				orignal = create_raw_board(X, Y, orignal)
				BRICK=BricksArray(orignal,level,X,Y)
				if level != 3:
					POWER=PowerUpArray(orignal,X,Y)


		game = Game(f,hit_paddle,TIME,X,Y,orignal,BRICK,POWER,points,level,level_time,ufo_x,ufo_y,ufo_health)
		while(1):
			game.update()	
			TIME+=1

			os.system("clear")
			game.board.display()		
			game.scoreboard()

			if game.input() == 'l':
				points = game.updatedpoints()
				new_level_flag = 1
				break

			if game.GAMEOVER == True:
				break

			
		if game.GAMEOVER == True:		
			lives = lives -1	
			# We need to update the orginal array and Brick' array because both of them have changed over time so in next life u have to transfer the updated one
			orignal = game.updatedboard()
			BRICK = game.updatedbricks()
			points = game.updatedpoints()
			POWER = game.updatedpower()
			ufo_health = game.updatedhealth()

	thankyou()		