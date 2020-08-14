from setuptools import setup

setup(
    name='gym_walk',
    version='0.0.1',
    description='Gym walk environment - useful to replicate Random Walk experiments',
    url='https://github.com/ercosv/gym-walk',
    packages=['gym_walk', 'gym_walk.envs'],
    install_requires=['gym'],
)
