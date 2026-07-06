import torch
from models.dqn import DQN

model = DQN(4, 2)

sample = torch.randn(1, 4)

output = model(sample)

print(output)