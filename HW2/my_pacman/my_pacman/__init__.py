from gym.envs.registration import register

register(
    id='my_pacman-v0',
    entry_point='my_pacman.envs:MyPacMan',
)