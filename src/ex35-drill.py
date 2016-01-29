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

------------------------------------------------------------

"""
doors = [
'Boring Door', 
'Door of Asingrath - \n\tHold secrets that must be revealed',
'Door of protection - For every thing we get, we pay for it !!!',
"Exit Door - Empty your pockets here and live free of materialistic benefits"]

questions = {
"0": 
	{
	 "question": "Is spock a vulcan ?",
	 "answer" : True
	},	
"1":
	{
	 "question": "Voyager was driven was not driven by kirk ?",
	 "answer" : False
	},
"2":
	{
	"question": "The needs of the many, outweigh the needs of the few",
	"answer" : True
	}
}

player_name = ""

enemies = {
"0" : {

"intro" : "Enemy : Koloss \t Attack : Heavy Hammer - Causes immediate skull damage followed by pee in the pants \nTakes : Coins, Godly prayers and PJ's only once"
},

"1" : {

"intro" : "Enemy : Allomancer \t Attack: Sharp lightining attack - Causes blindness and immediate death \nTakes: Coins and Godly prayers"
}

}
waiting_messages = [
"Fine!!!, Just don't pee outside we have a place for it inside this door.\n Ill reconfirm after 5 seconds.", 
"Rot in hell for 5 seconds", 
"Here is puzzle for the next 5 seconds...\n EAR UYO ZRACY"
]

coins = 10

coin_incr = 5

doors_crossed = 0

player_info_txt = """
======================================
PLAYER-NAME -> %s
COINS -> %d
DOORS-CROSSED -> %d
======================================
"""

def start_game():
	"""Starts the game, initialises everything needed"""
	print intro_msg
	player_name = raw_input("What' do they call you son ? ")
	end = False		
	while not end :
		choice,door = show_options()
		if choice == 'yes':
			#Enter the door chosen
			proceed = proceed_in_door(door)
			if proceed:
				print "Proceeding...."
				time.sleep(3)
				os.system('clear')
				continue	
			else :
				end = True

		elif choice == 'no' :
			#Show the random waiting message
			print random.randint(0,len(waiting_messages))
			time.sleep(5) #wait

		elif choice == 'info':
			#shows the player info
			show_player_info()
		else :
			print "Whaaaaaaaat the heck is that ?, Just YES or no"
		

def show_player_info():
	print player_info_txt %(player_name, coins, doors_crossed)


def incr_doors():
	global doors_crossed
	doors_crossed += 1


def show_options():
	"""Show options..."""
	idx = random.randint(0,len(doors)-1)
	print "You are presented with a", doors[idx]
	print "Do you enter ?"
	choice = raw_input("Enter yes or no")
	return choice, idx


def proceed_in_door(type):
	print "[TEST] Type of door is :",type
	puzzles = {
	"0": 
	{
		"puzzle" : "What shines and not dims, but when it does, everyone knows about it", 
		"answer":"STAR"
	}, 
	"1":
	{
		"puzzle":"Round but flat at the poles, they call me ?",
		"answer":"EARTH"
	}
	}
	success = False

	if type == 0 :
		print "Lucky you!!! , Please proceed"
		incr_doors()
		success = True

	elif type == 1 :
		print "Let's see your witt %s" %player_name
		print "Answer this and i shall let you go, else you must die in this pit"
		idx = random.randint(0,len(puzzles)-1)
		print "Puzzle index ",idx
		os.system('clear')
		print puzzles[str(idx)].get("puzzle")
		answer = raw_input("Tell what it is or prepare to die")
		if answer.upper() == puzzles[str(idx)].get("answer") :
			increment_coins()
			print "Witty, you, proceed further and see what awaits you"
			incr_doors()
			success = True
		else :
			success = False
			print "You die..."
			sys.exit(1)	

	elif type == 2:
		print "Answer the question that follow, if not you shall taste death by the enemy that stands infront"
		idx = random.randint(0, len(enemies)-1)
		show_enemy(enemies[str(idx)].get("intro"))
		idx = random.randint(0,len(questions))
		print questions[idx].question
		answer = raw_input("True or False ?")
		success = (answer == questions[idx].get("answer"))
		
	else:
		sys.exit(1)
	return success
	
def create_enemy(enemy):
	"""Creates enemies to kill the user"""
	print "-----------------------------------------------------------"
	print enemy
	print "------------------------------------------------------------"


def start_timer():
	"""This timer shall tell if the exit gate awaits the user or has vanished"""
	pass


def increment_coins():
	"""Increments coins on every door that user crosses"""
	global coins
	coins += coin_incr 
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

