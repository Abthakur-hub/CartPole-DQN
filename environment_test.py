import gymnasium as gym

# Create the CartPole environment
env = gym.make("CartPole-v1", render_mode="human")

# Reset the environment
observation, info = env.reset()

print("Initial Observation:", observation)

done = False

while not done:
    # Randomly choose an action
    action = env.action_space.sample()

    # Take the action
    observation, reward, terminated, truncated, info = env.step(action)

    print("Observation:", observation)
    print("Reward:", reward)

    done = terminated or truncated

env.close()