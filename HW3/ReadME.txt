Note:- Since, I am doing a project for CS5500, so, according to the information given, I have attempted only Problem 1 (5 points) and Problem 3 (25 points), giving a total of 30 points

The submitted folder contains the following files
	- CS5500_HW3.pdf (This file contains the written parts of the assignment and also the explanations of the coding part, wherever necessary)
	- Q3.ipynb (This file contains the python code for question number 3)

Instructions on runnning the code:
- Python version - 3.7.5
- Code has been implemented using jupyter notebook
- the code takes the following arguments, given in order
	*name of environment to use (type cartpole to use the CartPole environment and type lunarlander to use the LunarLander environment. The environment name to be typed is case sensitive)
	*whether to use reward to go without advantage normalisation (type True to use it, False to not use it)
	*whether to use reward to go with advantage normalisation (type True to use it, False to not use it)
	*number of epochs (type an integer)
	*batch size (type an integer)
- the following is the format of the code
	
	ipython Q3.ipynb 'name_of_env' 'reward_to_go_without_adv_norm' 'reward_to_go_with_adv_norm' 'num_epochs' 'batch_size'
	
	For example, to run CartPole environment with Reward to go without advantage normalisation for 150 epochs with batch size 20, type the following code

		ipython Q3.ipynb cartpole True False 150 20
	
	For example, to run CartPole environment with Reward to go with advantage normalisation for 150 epochs with batch size 20, type the following code
	
		ipython Q3.ipynb cartpole False True 150 20

Some tips on running the code
	-For CartPole environment using batch size of 20 for 150 epochs makes the algorithm converge when using Reward to go with or without Advantage normalisation. When not using Reward to go, increase the number of epochs to a higher number.
	-For LunarLander environment using batch size of 50 for 150 epochs makes the algorithm converge when using Reward to go with or without Advantage normalisation. When not using Reward to go, increase the number of epochs to a higher number.
	-If the algorithm doesn't converge with the above parameters for any of the environment, double the batch size. If it still doesn't converge, increase batch size further or increase number of epochs

All other details are commented in the code.