# game

import pygame
pygame.init()
import random

#display setting of window
Height = 300
Width = 500
screen = pygame.display.set_mode((Width, Height));
pygame.display.set_caption('Meteor Nightmare')
clock = pygame.time.Clock()

#colors we will be using
pink = (255,192,203)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

#button interaction
mouse = pygame.mouse.get_pos()
#mouse[0] is x coordinate 

font = pygame.font.Font("C:\Windows\Fonts\comicbd.ttf", 70)

def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()
	
def WriteText(msg, color):
	text = font.render(msg, True, color)
	screen.blit(text, [0+(210/2), 0+(150/2)])

#button(x, width, y, height, text, action=name of Button)
def button(x, w, y, h, t, action=None):
		mouse = pygame.mouse.get_pos()
		#(0, 0, 0) click of a mouse
		click = pygame.mouse.get_pressed()
		
		#mouse[0] is x coordinate. first and third variable add together to equal x range
		#mouse[1] is y coordinate.
		#170+160 (x plus how wide the box is)
		#200+50 (y plus how tall the box is)
		if x+w > mouse[0] > x and y+h > mouse[1] > y:
			pygame.draw.rect(screen, black, (x, y, w, h))
			smallText = pygame.font.Font("C:\Windows\Fonts\comicbd.ttf", 25)
			#msg and size
			textSurf, textRect = text_objects(t, smallText, white)
			textRect.center = ( (x+(w/2)), (y+(h/2)) )
			screen.blit(textSurf, textRect)
			if click[0] == 1 and action != None:
				if action == "play":
					game_loop()
				if action == "play1":
					intro()
				if action == "play2":
					back()
		else:
			pygame.draw.rect(screen, red, (x, y, w, h))
			#write text in box
			smallText = pygame.font.Font("C:\Windows\Fonts\comicbd.ttf", 25)
			#msg and size
			textSurf, textRect = text_objects(t, smallText, black)
			textRect.center = ( (x+(w/2)), (y+(h/2)) )
			screen.blit(textSurf, textRect)
	

mario = pygame.mixer.Sound(r'''mario.wav''')
	
def intro():
	mouse = pygame.mouse.get_pos()
	intro = True
	
	pygame.mixer.Sound.play(mario)
	
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			
		screen.blit(sky, (0,0))
		#green surface
		pygame.draw.rect(screen, green, (0, 190, 500, 300))
		#gray road ground
		pygame.draw.polygon(screen, gray, ((0,298), (250,130), (500,298)))
		#car appears
		screen.blit(car, (155, 130))
		#blackroadside
		lineDraw(0, 291, 155, 200, 10, 0, 0, 0)
		lineDraw(500, 291, 352, 200, 10, 0, 0, 0)
		
		lineDraw(255, 252, 255, 300, 10, 255, 255, 0)
		txt("Meteor Dash XD", 150, 90, 30)
		button(170, 160, 200, 50, "PLAY", "play")
		
		smallText = pygame.font.Font("C:\Windows\Fonts\comicbd.ttf", 20)
		text = smallText.render("created by WayneRuan", True, black)
		screen.blit(text, [260, 270])
		
		pygame.display.update()

		
car = pygame.image.load(r'''1.jpg''')
sky = pygame.image.load(r'''background.jpg''')

gray = (128, 128, 128)
lavender = (135,206,235)
green = (124,252,0)
treegreen = (34,139,34)
rootgreen =(0,100,0)

def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(screen, color, [thingx, thingy])
		
def game_loop():
	loop = True
	
	#left tree
	thing_startx = random.randrange(0, 50)
	g = random.randrange(70, 100)
	e = random.randrange(120, 150)
	# right tree
	a = random.randrange(383, 483)
	b = random.randrange(383, 400)
	thing_starty = random.randrange(85, 90)
	
	#message
	m1 = True
	m2 = False
	m3 = False
	m4 = False
	
	on = True
	
	while loop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		
		
		x = False
		#background
		screen.blit(sky, (0,0))
		#green surface
		pygame.draw.rect(screen, green, (0, 190, 500, 300))
		#gray road ground
		pygame.draw.polygon(screen, gray, ((0,298), (250,130), (500,298)))
		#car appears
		screen.blit(car, (155, 130))
		#blackroadside
		lineDraw(0, 291, 155, 200, 10, 0, 0, 0)
		lineDraw(500, 291, 352, 200, 10, 0, 0, 0)
		
		lineDraw(255, 252, 255, 300, 10, 255, 255, 0)
		
		bigTree(thing_startx, thing_starty)
		thing_startx -= 2
		bigTree(g, thing_starty)
		g -= 2
		bigTree(a, thing_starty)
		a += 2
		bigTree(e, thing_starty)
		e -= 2
		bigTree(b, thing_starty)
		b += 2
		thing_starty += 1
		
		# left side
		if thing_starty > 220 :
			thing_starty = random.randrange(85, 90)
			thing_startx = random.randrange(0, 50)
			g = random.randrange(60, 100)
			e = random.randrange(120, 150)
			a = random.randrange(383, 483)	
			b = random.randrange(383, 400)
		
		click = pygame.mouse.get_pressed()
		#Message(msg, color, x, y):
		
		#MESSAGES FOR USER
		if click[2] == 0 and m1 == True:
				Message("It's summer time", black, 162, 103)	
		elif click[2] == 1 and m1 == True:
				m2 = True
				Message("Time to go relax at the beach", black, 124, 100)
				m1 = False
		elif click[2] == 0 and m2 == True:
				m3 = True
				Message("Time to go relax at the beach", black, 124, 100)
		elif click[2] == 1 and m3 == True:
				m2 = False
				m3 = True
				Message("What could possibly go wrong, right?", black, 100, 100)
		elif click[2] == 0 and m3 == True:
				Message("What could possibly go wrong, right?", black, 100, 100)
				m4 = True
		if click[2] == 1 and m4 == True:
				m3 = False
				Message("", black, 124, 100)
				return game_loop1()
		if click[2] == 0 and m4 == True:
				Message("", black, 124, 100)
				return game_loop1()
			
					
		mouse = pygame.mouse.get_pos()
		print(mouse)
		
		pygame.display.update()
		


sky1 = pygame.image.load(r'''background1.jpg''')
car1 = pygame.image.load(r'''s1.jpg''')
sun = pygame.image.load(r'''sun.jpg''')
meteor = pygame.image.load(r'''meteor.jpg''')


		
def game_loop1():
	loop = True
	
	x = 600
	x1 = 600
	x2 = 600
	
	y = random.randrange(180, 200)
	y1 = random.randrange(180, 201)
	y2 = random.randrange(179, 202)
	
	m = -50
	n = 550
	
	while loop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		
		#background
		screen.blit(sky1, (0,0))
		#green surface
		pygame.draw.rect(screen, green, (0, 190, 500, 300))
		#gray road ground
		pygame.draw.rect(screen, gray, (0, 200, 500, 60))
		#car appears
		#blackroadside
		lineDraw(0, 200, 500, 200, 10, 0, 0, 0)
		lineDraw(0, 260, 500, 260, 10, 0, 0, 0)
		
		#yellowmark
		lineDraw(0, 230, 500, 230, 3, 255, 255, 0)
		
		screen.blit(car1, (0,155))
		
		Message("What could possibly go wrong, right?", black, 100, 100)

		bigTree(x, y)
		x -= 2
		
		bigTree(x1, y1)
		x -= 2
		
		bigTree(x2, y2)
		x -= 2
		
		if x < 0 :
			x = 600
			x1 = 550
			x2 = 550
			y = random.randrange(180, 200)
			y1 = random.randrange(180, 201)
			y2 = random.randrange(179, 202)	
		
		click = pygame.mouse.get_pressed()
		#Message(msg, color, x, y):
		

		screen.blit(sun, (375, 15))
		
		screen.blit(meteor, (m, 15))
		m += 1
		
		if m == 300:
			blank()
		
		mouse = pygame.mouse.get_pos()
		print(mouse)
		
		pygame.display.update()
		
def blank():
	loop2 = True
	
	x = False
	
	
	while loop2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()	

		screen.fill(white)
		
		smallText = pygame.font.Font("C:\Windows\Fonts\comicbd.ttf", 15)
		text = smallText.render("Your vacation has just been ruined by a frickin' meteor..", True, black)
		screen.blit(text, [60, 80])
		txt("SURVIVE WHILE YOU CAN...", 130, 100, 20)
		txt("AVOID ALL METEORS BY USING YOUR ARROW KEY...", 80, 140, 15)
		button(150, 250, 200, 50, "CONTINUE", "play2")

		pygame.display.update()

sil = pygame.image.load(r'''silverado.jpg''')	
m17 = pygame.image.load(r'''met.jpg''')
m18 = pygame.image.load(r'''met1.jpg''')
pool = pygame.image.load(r'''pool.jpg''')

life1 = True
life2 = False
life3 = False


pygame.mixer.music.load(r'''dance.wav''')
explode = pygame.mixer.Sound(r'''explode.wav''')
screech = pygame.mixer.Sound(r'''screech.wav''')
		
def back():

	pygame.mixer.Sound.stop(mario)
	pygame.mixer.Sound.stop(explode)
	
	pygame.mixer.music.set_volume(.5)
	pygame.mixer.music.play(1)

	
	loop2 = True
	l = True
	x = 0
	y = 100
	x_change = 0
	y_change = 0
	x_change1 = .1
	
	thing_startx = 560
	thing_startx1 = 560
	thing_pit = 560
	
	#meteor
	thing_startym = random.randrange(0, 450)
	thing_startym1 = random.randrange(0, 450)
	
	carr = True
	slow = False

	thing_speed = .1
	thing_speed1 = .1
	
	f1 = 560
	f11 = random.randrange(0, 40)
	f111 = .5
	f33 = random.randrange(200, 240)
	
	#sideway meteor
	thing_starty1 = -300
	thing_startx = random.randrange(0, 500)
	thing_startside = random.randrange(0, 400)
	
	ran = random.randrange(1, 2)
	
	end = False
	
	zero = 0
	
	ay = False
	
	while loop2:	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			
			if event.type == pygame.KEYDOWN and carr == True and end == False:
					if event.key == pygame.K_LEFT:
						l = False
						x_change = -.4
						# f111 = .5
						# thing_speed1 = .1
						# thing_speed = .1
					if event.key == pygame.K_RIGHT:
						l = False
						x_change = .4
						# f111 = .9
						# thing_speed1 = .5
						# thing_speed = .2
					if event.key == pygame.K_UP:
						l = False
						y_change = -.4
					if event.key == pygame.K_DOWN:
						l = False
						y_change = .4
						
			if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
						x_change = 0
					if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
						y_change = 0
		
		
		screen.fill(black)
		

		
		neo = pygame.mixer.music.get_busy()
		if neo == False:
			end = True
			x_change = 1
			
		if x >= 500:
			blancc()
			
		tom = pygame.mixer.music.get_pos()
		print(tom)
		
		if tom == 0:
			thing_speed1 = .1
			f111 = .1
			thing_speed = .1
			zero = .1
		elif tom == 6800:
			thing_speed1 = .3
			f111 = .3
			thing_speed = .3
			zero = .2
		elif tom == 13300:
			thing_speed1 = .6
			f111 = .6
			thing_speed = .6
			zero = .3
		elif tom == 25200:
			thing_speed1 = .9
			f111 = .5
			thing_speed = .9
			zero = .3
			ay = True
		
		
		
		# if l == True:
			# smallText = pygame.font.Font("C:\Windows\Fonts\comicbd.ttf", 15)
			# text = smallText.render("Your vacation has been ruined by a frickin' meteor strike.", True, black)
			# text1 = smallText.render("so...umm...have a fun summer :)", True, black)
			# screen.blit(text, [50, 150])
			# screen.blit(text1, [50, 170])
		
		# pygame.draw.rect(screen, rootgreen, (100, 0, 100, 300))
		lineDraw(0, 100, 500, 100, 1, 211, 211, 211)
		lineDraw(0, 200, 500, 200, 1, 211, 211, 211)
		
		x += x_change	
		y += y_change
		
		if end == False:
			if y > 265:
				y = 265
			elif y < -2:
				y = -2
			elif x < 0:
				x = 0
			elif x > 425:
				x = 425
		
		screen.blit(pool, [f1, f11])
		screen.blit(pool, [f1, f33])
		
		
		k = screen.blit(sil, [x, y])
		
		screen.blit(m17, [thing_startx1, thing_startym])
		screen.blit(m17, [thing_startx1, thing_startym1])
		
		#side meteor
		screen.blit(m18, [thing_startx, thing_starty1])
		
		if ay == True:
			screen.blit(m18, [thing_startside, thing_starty1])

		thing_startx1 -= thing_speed1
		f1 -= f111
		thing_starty1 += thing_speed
		
		thing_startx -= zero
		
		thing_startside -= zero

		#big meteor
		if thing_startx1 < -105:
			thing_startx1 = 560
			thing_startym = random.randrange(0, 450)
			thing_startym1 = random.randrange(0, 450)
			
		#pit(slows people down)
		if f1 <= -111:
			f1 = 560
			f11 = random.randrange(0, 40)
			# f22 = random.randrange(100, 140)
			f33 = random.randrange(200, 240)
			
		if thing_starty1 >= 450:
			thing_starty1 = -300
			thing_startx = random.randrange(300, 500)
			thing_startside = random.randrange(300, 500)
				
		# #crash mechanics for METEOR
		
		if thing_startym < y < thing_startym+62 or thing_startym1 < y < thing_startym1+62:
			if x <= thing_startx1 < x+70:
				carr = False
				thing_speed = 0
				thing_speed1 = 0
				blanc()
				
		# # if thing_startx1 < x < thing_startx1+101:
			# # if y+36 == thing_startym:
				# # blanc()
				
		if f11 < y < f11+58 or f33 < y < f33+58:
			if x <= f1 < x+58:
				thing_speed1 += .01
				thing_startx -= .001
				zero += .01
		
		
		
		# #bottom hitbox
		# if thing_startx < x < thing_startx+62 or thing_startside < x < thing_startside+62:
		if thing_startx < x < thing_startx+62:
			print("nice")
			# if y <= thing_starty1 < y+50:
			if thing_starty1 < y < thing_starty1+101:
				blanc()		
		# if thing_startx < x+74 < thing_startx+62 or thing_startside < x+74 < thing_startside+62:	
		if thing_startx < x+74 < thing_startx+62:		
			print("nice1111")
			# if y <= thing_starty1 < y+50:
			if thing_starty1 < y < thing_starty1+101:
				blanc()	
				
		if thing_startside < x+74 < thing_startside+62 and ay == True:		
			print("nice1111")
			# if y <= thing_starty1 < y+50:
			if thing_starty1 < y < thing_starty1+101:
				blanc()	

		# if thing_startx < x < thing_startx+36 or thing_startside < x < thing_startside+36:
			# print("nice122222")
			# if y <= thing_starty1 < y+74:
				# blanc()				
			
		
		pygame.display.update()

				
		
		# mouse = pygame.mouse.get_pos()
		# print(mouse)	

def txt(msg, x, y, size):
		smallText = pygame.font.Font("C:\Windows\Fonts\comicbd.ttf", size)
		text = smallText.render(msg, True, red)
		screen.blit(text, [x, y])
		
def blanc():
	loop2 = True
	
	pygame.mixer.music.stop()
	pygame.mixer.Sound.play(explode)
	
	while loop2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()	

		screen.fill(white)
		
		txt("You are knocked out...by a METEOR", 130, 100, 20)
		button(150, 250, 200, 50, "PLAY AGAIN!", "play2")	
			

		pygame.display.update()
		

win = pygame.image.load(r'''gameoverscreen.jpg''')
c4 = pygame.image.load(r'''tesla.png''')
		
#YOU WIN		
def blancc():
	loop2 = True
	
	x = -200
	speed = 1
	
	pygame.mixer.Sound.play(screech)
	
	while loop2:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()	

		screen.blit(win, [0, 0])
		
		screen.blit(c4, [x, 110])
		
		x += speed
		
		if x == 240:
			speed = 0
			
		mouse = pygame.mouse.get_pos()
		print(mouse)
		
		button(350, 160, 200, 50, "Play again!", "play1")

		
		pygame.display.update()
		
# def text_objects(text, font, color):
	# textSurface = font.render(text, True, color)
	# return textSurface, textSurface.get_rect()
		
def rec(x, y):
	pygame.draw.rect(screen, yellow, ((x, y, 20, 20)))
	
		
def Message(msg, color, x, y):
	smallText = pygame.font.Font("C:\Windows\Fonts\comicbd.ttf", 20)
	text = smallText.render(msg, True, color)
	screen.blit(text, [x, y])

		
def tree(a1, a2, b1, b2):
	c1 = a1+(a1-b1)
	c2 = b2
	#top
	pygame.draw.polygon(screen, treegreen, [(a1, a2), (b1, b2), (c1, c2)])
	#root
	pygame.draw.rect(screen, rootgreen, ((a1-1), b2, (c1-a1)/2, (b2-a2)))

def bigTree(a1, a2):
	b1 = a1 - 10
	b2 = a2 + 53
	c1 = a1+(a1-b1)
	c2 = b2
	#top
	pygame.draw.polygon(screen, treegreen, [(a1, a2), (b1, b2), (c1, c2)])
	#root
	pygame.draw.rect(screen, rootgreen, ((a1-3), b2, (c1-a1)/2, (b2-a2)))
	
def bigTree(a1, a2):
	b1 = a1 - 10
	b2 = a2 + 53
	c1 = a1+(a1-b1)
	c2 = b2
	#top
	pygame.draw.polygon(screen, treegreen, [(a1, a2), (b1, b2), (c1, c2)])
	#root
	pygame.draw.rect(screen, rootgreen, ((a1-3), b2, (c1-a1)/2, (b2-a2)))

def lineDraw(x, y, z, zx, w, a, b, c):
	blue = a, b, c
	point1 = x, y
	point2 = z, zx
	width = w
	pygame.draw.line(screen, blue, point1, point2, width)
		
			
			

intro()
pygame.quit()
quit()
