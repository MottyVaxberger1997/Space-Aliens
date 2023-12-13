import matplotlib as plt
import random
import tqdm
# from scratch.gradient_descent import gradient_step
num_epochs = 10000
random.seed(0)
guess = [random.random(), random.random()]
# choose random value to start
learning_rate = 0.00001
with tqdm.trange(num_epochs) as t:


# for _ in t:
#     alpha, beta = guess
# # Partial derivative of loss with respect to alpha
# grad_a = sum(2 * error(alpha, beta, x_i, y_i)
# for x_i, y_i in zip(num_friends_good, daily_minutes_good)):
# # Partial derivative of loss with respect to beta
# grad_b = sum(2 * error(alpha, beta, x_i, y_i) * x_i
# for x_i, y_i in zip(num_friends_good, daily_minutes_good)):
# # Compute loss to stick in the tqdm description
# loss = sum_of_sqerrors(alpha, beta, num_friends_good, daily_minutes_good)
# t.set_description(f"loss: {loss:.3f}")
# # Finally, update the guess
# guess1 = gradient_step(guess, [grad_a, grad_b], -learning_rate)
# alpha, beta = guess
# assert 22.9 < alpha < 23.0
# assert 0.9 < beta < 0.905