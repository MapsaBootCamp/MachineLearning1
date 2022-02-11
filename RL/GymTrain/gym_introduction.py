from distutils.command.build import build
import gym
import numpy as np
import time

env_name = "FrozenLake8x8-v1"
env = gym.make(env_name)


class Agent:
    def __init__(self, env) -> None:
        self.size_actions = env.action_space.n
        print("action size: ", self.size_actions)
    
    def get_action(self, state):
        random_action = np.random.choice(range(self.size_actions))
        # cart_pole = state[2]
        # action = 0 if cart_pole > 0 else 1 
        return random_action

class AgentQLearning(Agent):
    def __init__(self, env, learning_rate=0.1, discount_rate=0.01):
        super().__init__(env)
        self.state_size = env.observation_space.n
        self.build_q_table()


        self.lr = learning_rate
        self.dr = discount_rate

    def build_q_table(self):
        self.q_table = np.random.randn((self.state_size, self.size_actions)) * 1e-5

    def get_action(self, state):
        greedy_action = np.argmax(self.q_table[state])
        return greedy_action

    def train(self):
        pass

agent = AgentQLearning(env)

for i_episode in range(10):
    state = env.reset()
    done = False
    total_reward = 0
    while not done:
        action = agent.get_action(state)
        state, reward, done, info = env.step(action)
        total_reward += reward
        # env.render()
    print(f"episode {i_episode} total_reward: ", total_reward)
    time.sleep(1)

env.close()

print(env.action_space)
print(env.observation_space)

