from distutils.command.build import build
from random import random
import gym
import numpy as np
import time

from gym.envs.toy_text.frozen_lake import FrozenLakeEnv


env_name = "FrozenLake-v1"
env = gym.make(env_name, is_slippery=False)


class Agent:
    def __init__(self, env) -> None:
        self.size_actions = env.action_space.n
        print("action size: ", self.size_actions)
    
    def get_action(self):
        random_action = np.random.choice(range(self.size_actions))
        # cart_pole = state[2]
        # action = 0 if cart_pole > 0 else 1 
        return random_action

class AgentQLearning(Agent):
    def __init__(self, env, learning_rate=0.1, discount_rate=0.8):
        super().__init__(env)
        self.state_size = env.observation_space.n
        self.build_q_table()

        self.exploration_rate = 1
        self.lr = learning_rate
        self.dr = discount_rate

    def build_q_table(self):
        self.q_table = np.random.random([self.state_size, self.size_actions]) * 1e-5

    def get_action(self, state):
        greedy_action = np.argmax(self.q_table[state])
        random_action = super().get_action()
        return random_action if np.random.random() < self.exploration_rate else greedy_action

    def train(self, state, action, new_state, reward, done):
        q_old = self.q_table[state, action]
        q_target = reward + self.dr * np.max(self.q_table[new_state])
        q_learned = q_target - q_old
        
        self.q_table[state, action] += self.lr * q_learned

        if done:
            self.exploration_rate *= 0.999

agent = AgentQLearning(env)

print("q_table: ", agent.q_table)

for i_episode in range(1000):
    state = env.reset()
    done = False
    total_reward = 0
    while not done:
        action = agent.get_action(state)
        new_state, reward, done, info = env.step(action)
        total_reward += reward
        agent.train(state, action, new_state, reward, done)
        state = new_state
        # env.render()
    print(f"episode {i_episode} total_reward: ", total_reward)
    # print(f"q_table: ", agent.q_table)
    # time.sleep(0.5)

print("Finish")
print("q_table: ", agent.q_table)
env.close()

# print(env.action_space)
# print(env.observation_space)

