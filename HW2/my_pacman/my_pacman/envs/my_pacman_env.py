import gym
import numpy as np

class MyPacMan(gym.Env):
	metadata = {'render.modes': ['human']}

	def __init__(self, size, num_food):
		self.size = size
		self.num_food = num_food
		self.count_food = num_food
		self.state = []
		for i in range(self.size):
			self.state += [[]]
			for j in range(self.size):
				self.state[i] += ["-"]
		temp = self.size*self.size
		self.is_over = 0
		self.reward = 0
		self.pacman = 0
		self.count_cons = 0
		self.action = [0,0]
		self.action_gh = [0,0]
		self.ghost = np.random.choice(np.arange(1,temp))
		self.state[int(self.pacman/self.size)][self.pacman%self.size] = 'P'
		self.state[int(self.ghost/self.size)][self.ghost%self.size] = 'G'
		self.food_renew()

	def food_renew(self):
		temp = self.size*self.size
		self.count_food = self.num_food
		ch = np.random.choice(np.arange(temp),replace = False, size = self.num_food)
		for i in range(ch.shape[0]):
			if(self.state[int(ch[i]/self.size)][ch[i]%self.size]=='G'):
				self.state[int(ch[i]/self.size)][ch[i]%self.size] = 'G/*'
			elif(self.state[int(ch[i]/self.size)][ch[i]%self.size]=='P'):
				self.state[int(ch[i]/self.size)][ch[i]%self.size] = 'P'
				self.reward = 10
				self.count_cons+=1
				self.count_food-=1
				if(self.count_food <= 0):
					self.food_renew()
			else:
				self.state[int(ch[i]/self.size)][ch[i]%self.size] = '*'

	def act(self, action):
		if(self.state[int(self.ghost/self.size)][self.ghost%self.size] == 'G/*'):
			self.state[int(self.ghost/self.size)][self.ghost%self.size] = '*'
		else:
			self.state[int(self.ghost/self.size)][self.ghost%self.size] = '-'
		self.state[int(self.pacman/self.size)][self.pacman%self.size] = '-'


		if(action==1):
			self.action = [1,0]
		if(action==2):
			self.action = [-1,0]
		if(action==3):
			self.action = [0,-1]
		if(action==4):
			self.action = [0,1]
		if(action==5):
			self.action = [0,0]

		if (int(self.pacman/self.size)+self.action[0] < 0 or int(self.pacman/self.size)+self.action[0] >=self.size):
			print("Collided with upper/lower wall. Game Over")
			self.reward = -100
			self.is_over = 1
			return [self.state, self.reward, self.is_over, self.count_food] 
		elif (self.pacman%self.size+self.action[1] < 0 or self.pacman%self.size+self.action[1] >=self.size):
			print("Collided with left/right wall. Game Over")
			self.reward = -100
			self.is_over = 1
			return [self.state, self.reward, self.is_over, self.count_food] 
		else:
			self.pacman = self.pacman + self.action[0]*self.size + self.action[1]


		action_gh = np.random.choice([1,2,3,4])
		if(action_gh == 1):
			self.action_gh = [1,0]
		if(action_gh == 2):
			self.action_gh = [-1,0]
		if(action_gh == 3):
			self.action_gh = [0,1]
		if(action_gh == 4):
			self.action_gh = [0,-1]
		self.ghost = self.ghost + self.action_gh[0]*self.size + self.action_gh[1]
		if(self.ghost <0):
			self.ghost = self.size**2-1
		elif(self.ghost >=self.size**2):
			self.ghost = 0


		if(self.pacman == self.ghost):
			print("Caught by ghost. Game Over")
			self.reward = -100
			self.is_over = 1
			return [self.state, self.reward, self.is_over, self.count_food] 

		if(self.state[int(self.pacman/self.size)][self.pacman%self.size] == '*'):
			self.reward = 10
			self.count_cons+=1
			self.count_food-=1
			self.state[int(self.pacman/self.size)][self.pacman%self.size] = 'P'
			if(self.count_food<=0):
				self.food_renew()			
		else:
			self.state[int(self.pacman/self.size)][self.pacman%self.size] = 'P'
			self.reward = -1

		if(self.state[int(self.ghost/self.size)][self.ghost%self.size]=='*'):
			self.state[int(self.ghost/self.size)][self.ghost%self.size] = 'G/*'
		else:
			self.state[int(self.ghost/self.size)][self.ghost%self.size] = "G"

		return [self.state, self.reward, self.is_over, self.count_food] 


	def print(self):
		for i in range(self.size):
			for j in range(self.size):
				print(self.state[i][j], end = "\t")
			print("\n")

	def reset(self):
		for i in range(self.size):
			for j in range(self.size):
				self.state[i][j] = "-"
		temp = self.size*self.size
		t1 = self.count_cons
		self.is_over = 0
		self.reward = 0
		self.pacman = 0
		self.count_cons = 0
		self.ghost = np.random.choice(np.arange(1,temp))
		self.state[int(self.pacman/self.size)][self.pacman%self.size] = 'P'
		self.state[int(self.ghost/self.size)][self.ghost%self.size] = 'G'
		self.food_renew()
		return self.state, t1

	def give_state(self):
		return self.state
