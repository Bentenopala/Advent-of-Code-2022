import itertools

def same_letters(data):
	'''
	Preprocess data from input file using the same letters for same gestures regardless of the player.
	'''
	return data.replace(" ","").strip().replace("X","A").replace("Y","B").replace("Z","C").split('\n')

def diff_letters(data):
	'''
	Preprocess data from input file using different letters for same gestures made by different players.
	'''
	return data.replace(" ","").strip().split('\n')

def outcomes_dict(data_same):
	'''
	Creates a dictionary containing each possible outcome and the score the player would get.
	data_same: data needs to have the same letters for both players, use same_letters().
	'''
	gesture = ['A','B','C']
	gesture_score = {'A': 1, 'B': 2, 'C': 3}
	outcome_code = "360"	# scores are obtained using this string ("draw-win-lose")
	outcomes = dict()
	for out in itertools.product(gesture, gesture):
		possible_outcome = out[0] + out[1] 
		# Next, the sum of oponent's contribution (opc) and player's contribution (plc)
		# will give the position on the outcome_code string that represents the game score.
		opc = (gesture_score.get(out[0])-1)*(-1)	# A: 0, B: -1, C: -2
		plc = gesture_score.get(out[1])-1			# A: 0, B: 1, C: 2
		round_score  = int(outcome_code[opc+plc]) 
		final_score = round_score + gesture_score.get(out[1])
		outcomes.update({possible_outcome: final_score})	
	return outcomes

def calculate_score(data_same):
	'''
	Calculates the strategy score using outcomes_dict().
	data_same: data needs to have the same letters for both players, use same_letters().
	'''
	outcomes = outcomes_dict(data_same)
	total_score = 0
	for rs in data_same: 	# Getting each round score form the outcomes dict
		total_score += outcomes.get(rs)
	return total_score

def interpret_strategy(data):
	'''
	Interprets the gestures needed by the player to satisfy the strategy.
	Returns the strategy using same letters for same gestures.
	'''
	strategy = diff_letters(data)
	outcomes = outcomes_dict(same_letters(data))
	round_score = {'X': 0, 'Y': 3, 'Z': 6}
	new_strategy = []
	for g in strategy: 		
		op, me = g[0], g[1]
		rs = round_score.get(me) 
		# From the opponent's gesture (op) and the round score (rs), the player's gesture is obtained 
		# using the outcomes dict. The value of the outcome (v) must be v > rs 
		# and at most equal to rs + 3 (player gestures adds +1, +2, or +3 to the rs).
		gesture = [k for k,v in outcomes.items() if (k.startswith(op) and v > rs and v < rs+4)]
		new_strategy.extend(gesture) 
	return new_strategy

def strategy_score1(data):
	'''
	Calculates the score of the strategy defined as it was in part 1.
	'''
	strategy = same_letters(data)
	return calculate_score(strategy)

def strategy_score2(data):
	'''
	Calculates the score of the strategy defined as it was in part 2.
	'''
	strategy = interpret_strategy(data)
	return calculate_score(strategy)

with open("day02.txt", "rt") as myfile:
	data = myfile.read()
	
	print(strategy_score1(data))
	print(strategy_score2(data))
