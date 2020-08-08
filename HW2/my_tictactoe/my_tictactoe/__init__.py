from gym.envs.registration import register

register(
    id='my_tictactoe-v0',
    entry_point='my_tictactoe.envs:MyTicTacEnv',
)