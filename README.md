The Brick-Breaker Game :-)

About the Game:-	
	-> The Game is fairly simple one.
	-> You are given a Paddle and a Ball and a set of Bricks.
	-> Your goal is to break all the bricks and attain high scores in minimum time.
	-> You will be given some Power_Ups which may help to achieve high scores faster.



Rules:-
1) After each new life the player will be given option to shoot the ball at his will.

2) Try to catch the ball by moving the paddle left(use key 'A') and right(use key 'D'). You will lose a life if ball misses the paddle

3) Make the ball collide at appropiate position of paddle to attain high speeds.

4) Power-Ups will be provided on breaking some specific bricks. 

5) A Power-Up will only be active if you catches it with the paddle and will be lost after 100 ticks.

6) All Power-Ups will be lost at a new life.

7) Can have multiple Power-Ups at a time.

8) Some bricks can be broken on first hit while some can take more than one hit and some bricks(unbreakable ones) can be broken by having a "Thuru-Ball" power-up only.

9) A Game_Guide will be given before the start of the game



Functionality:-
-> MODULARITY:- 
  The code is written in 9 different python files making it a modular one and is build by following the priciples of OOPS.
	-> game.py is the main file of the code(starter code)
	-> Paddles.py file contain Paddles class and functions associated with paddle
	-> Balls.py file contain Balls class and functions associated with ball
	-> Bricks.py file contain functions associated with bricks
	-> PowerUps.py file contain the functions associated with the powerups.
	-> Elements.py file contain the shape of all elements involved and their color
	-> Blocks.py file contain the display features
	-> Board.py file contain the display function and call some functions to store the last left positions.
	-> drawings.py file contain functions for game-guide(to be shown at the start of the game) leaving comment(thankyou function) and a trophy function if you win!

-> OOPS:-
	INHERITANCE :-
	In Elements.py file contains the Elements class(Parent class) and rest all other classes Paddle,Brick,Ball,PowerUp etc. (Child class) are inherited from it.

	POLYMORPHISM :-
	All the child classes have the x,y co-ordinates attributes inherited from the parent. In Paddle class these are stroring the co-ordinates of Paddle and in case of Ball class they are stroing the co-ordinates of ball.Similarly for other classes too.

	ENCAPSULATION :- All the functionality implemented whether it's ball,paddle,brick,power-up or anything everything is either a base class or a derived class.(Everthing implemented is mostly class or object only) Also the objects are passed from one file to another to be used and updated.

	ABSTRACTION :- 
	game.py file contains abstracted functions like move_paddle,
	update_powerUp, gamewon etc. whose names clearly shows what they actually does hiding the inner details of the function.

-> Followed DRY(Do Not Repeat Yourself) principle to make code non-redundant.The code is modular and extensible to new features.



Power-Ups:-
1) Expand Paddle: Increases the size of the paddle by a certain amount.

2) Shrink Paddle: Reduce the size of the paddle by a certain amount.

3) Fast Ball: Increases the speed of the ball.

4) Thru-ball: This enables the ball to destroy and go through any brick it touches, irrespective of the strength of the wall.(Even the unbreakable ones which you couldn’t previously destroy)

5) Paddle Grab:Allows the paddle to grab the ball on contact and relaunch the ball at will. The ball will follow the same expected trajectory after release, similar to the movement expected without the grab.



How to run?
-> pip3 install termcolor
-> pip3 install colorama
-> pip3 install playsound
-> python3 game.py
	
	HOPEFULLY YOU ENJOY PLAYING IT! 
	WILL TRY TO GIVE YOU ANOTHER FANTASTIC GAME SHORTLY ;-)
	

GAME TIP :- "Choose the rightmmost side to have a score-rich move for the game ;-)"

NEW FUNCTIONALITIES:-
-> Implemented levels(use 'l' to skip levels)

-> Bricks starts falling after a particular time in a level whenever ball hits the paddle(buggy!) 

-> Rainbow Bricks:- Bricks keep changing colors until first hit

-> Power-Ups attain the ball velocity after hitting and follows elastic collision

-> Level3 is Boss Enemy where your task is to destroy the UFO

-> Added Power Up of Fireball('A') which after enabled will destroy all the bricks horizontally/vertically/diagonally from a given brick when ball hits this brick.

-> Added sounds to make game more enjoyable.
