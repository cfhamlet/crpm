import numpy as np

lambdas = np.array([1.0, 2.0, 3.0], dtype=float)  # lambda
lambdas = lambdas.reshape(-1, 1)

print(lambdas)

players = np.array([3,4,10,8], dtype=float)

print(players)

print(lambdas * players)
