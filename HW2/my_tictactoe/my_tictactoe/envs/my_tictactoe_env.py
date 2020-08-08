import gym
from gym import error, spaces, utils
from gym.utils import seeding

class MyTicTacEnv(gym.Env):
	metadata = {'render.modes': ['human']}


	def __init__(self):
		self.state = []
		for i in range(3):
			self.state += [[]]
			for j in range(3):
				self.state[i] += ["_"]
		self.counter = 0
		self.is_over = 0
		self.tally = [0, 0]
		self.reward = 0

	def is_won(self):

		if(self.counter<5):
			return 0
		for i in range(3):
			if(self.state[i][0] != "_" and self.state[i][1] == self.state[i][0] and self.state[i][1] == self.state[i][2]):
				if(self.state[i][0] == "x"):
					return 1
				else:
					return 2
			if(self.state[0][i] != "_" and self.state[1][i] == self.state[0][i] and self.state[1][i] == self.state[2][i]):
				if(self.state[0][i] == "x"):
					return 1
				else:
					return 2
		if(self.state[0][0] != "_" and self.state[1][1] == self.state[0][0] and self.state[1][1] == self.state[2][2]):
			if(self.state[0][0] == "x"):
				return 1
			else:
				return 2
		if(self.state[0][2] != "_" and self.state[0][2] == self.state[1][1] and self.state[1][1] == self.state[2][0]):
			if(self.state[1][1] == "x"):
				return 1
			else:
				return 2

	def act(self, move):
		i = int(move/3)
		j = move%3
		if self.is_over == 1:
			print("Game Over")
			return [self.state, self.reward, self.is_over, self.tally]
		elif self.state[int(move/3)][move%3] != "_":
			print("Invalid Step, Try Again")
			return [self.state, self.reward, self.is_over, self.tally]
		else:
			if(self.counter%2 == 0):
				self.state[i][j] = "x"
			else:
				self.state[i][j] = "o"
			self.counter += 1
			if(self.counter == 9):
				self.is_over = 1;

		winnner = self.is_won()
		if(winnner):
			self.is_over = 1;
			print("Player ", winnner, " wins the round")
			self.tally[winnner-1] = self.tally[winnner-1] + 1;
			if winnner == 1:
				self.reward = 100
			else:
				self.reward = -100

		return [self.state, self.reward, self.is_over, self.tally]

	def reset(self):
		for i in range(3):
			for j in range(3):
				self.state[i][j] = "_"
		self.counter = 0
		self.is_over = 0
		self.reward = 0
		return self.state

	def print(self):
		for i in range(3):
			for j in range(3):
				print(self.state[i][j], end = "\t")
			print("\n")

	def print_tally(self):
		return(self.tally)

	def reset_tally(self):
		self.tally = [0,0]
