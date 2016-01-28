import random, os , time, sys
#Creating a game

"""
This game is a naive game of doors,with every door being one of the type mentioned below

1. Normal door to enter
2. Secret puzzle involved to enter
3. Killer door - Behind which lies an enemy which can only be killed in 
three ways 
	1. By telling a poor joke
	2. By bribing with coins - Coins get accumulated by entering in the normal doors and secret puzzle doors.
	3. By using a "Save me" - which can be attained only after answering the questions about spock.
	
4. The exit door shall await you only for a while, after which you will forever lie in this door maze...

Play only if you must,
for its a game of trust
"""
intro_msg = """
------------------------------------------------------------
		Game Of Doors
------------------------------------------------------------

Welcome player to the dauting world of doors.We hope
you have enjoyed your life before coming here for the
phase of continuos wrath and bloodshed is about to begin.

May the force be with you...

"""
doors = ['Boring Door', 'Door of Asingrath - \n\tHold secrets that must be revealed', 'Door of protection - For every thing we get, we pay for it !!!',"Exit Door - Empty your pockets here and live free of materialistic benefits"]

player_name = ""

enemies = {
"0" : {"intro" : "Enemy : Koloss \t Attack : Heavy Hammer - Causes immediate skull damage followed by pee in the pants \nTakes : Coins, Godly prayers and PJ's only once"},
"1" : {"intro" : "Enemy : Allomancer \t Attack: Sharp lightining attack - Causes blindness and immediate death \nTakes: Coins and Godly prayers"}
}

coins = 10

def start_game():
	"""Starts the game, initialises everything needed"""
	print intro_msg
	player_name = raw_input("What' do they call you son ? ")
	show_options()

def show_player_info():
	pass

def show_options():
	"""Show options..."""
	idx = random.randint(0,len(doors)-1)
	print "You are presented with a", doors[idx]
	print "Do you enter ?"
	choice = raw_input("Enter yes or no")
	if choice == "yes" or choice == "YES":
		proceed_in_door(idx)
	else:
		print "Fine!!!, Just don't pee outside we have a place for inside this door.\n Ill reconfirm after 5 seconds."
		time.sleep(5)
		show_options()

def proceed_in_door(type):
	puzzles = {"0": {"puzzle" : "What shines and not dims, but when it does, everyone knows about it", "answer":"STAR"}, "1":{"puzzle":"Round but flat at the poles, they call me ?","answer":"EARTH"}}

	if type == 0 :
		print "Lucky you!!! , Please proceed"
		show_options()

	elif type == 1 :
		print "Let's see your witt %s" %player_name
		print "Answer this and i shall let you go, else you must die in this pit"
		idx = random.randint(0,2)
		os.system('clear')
		print puzzles[str(idx)].puzzle
		answer = raw_input("Tell what it is or prepare to die")
		if answer.upper() == puzzles[str(idx)].answer :
			increment_coins()
			print "Witty, you, proceed further and see what awaits you"
			show_options()
		else :
			print "You die..."
			sys.exit(1)	

	elif type == 2:
		print "Answer the questions that, if not you shall taste death by the enemy that stands infront"
		print enemies[random.randint[0,2]]['intro']

	else:
		sys.exit(1)
		
def create_enemy():
	"""Creates enemies to kill the user"""
	pass

def start_timer():
	"""This timer shall tell if the exit gate awaits the user or has vanished"""
	pass

def increment_coins():
	"""Increments coins on every door that user crosses"""
	coins +=1 
	pass

def poor_joke_validator(joke):
	"""Responds with a 'HAHA' which means the user's wish wasn't grantedor else says 'Granted' """
	pass

def bribe_validator(bribe):
	"""Responds with a 'YES' if bribed successfully or says 'PUT SOME MORE WEIGHT!!! BRO' but consumes the coins which were given to him earlier and asks only for the difference now."""
	pass

def old_jedi_validator(prayer):
	"""Answers a 'GRANTED' or 'ABUSES' for good and bad praters respectively"""
	pass

start_game()

