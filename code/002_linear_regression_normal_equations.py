# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Set the number of data points
n = 10

# Generate data of the form y = m(x + e) + b
noise = np.random.rand(n)
bias = np.random.randint(-10, 10)
slope = np.random.randint(0, 5)

# Print the slope, bias, and noise used to generate data
print(f"slope: {slope}, bias: {bias}")
# >> slope: 3, bias: -9

x = np.arange(n)
y = slope * (x + noise) + bias

# Plot the data
plt.scatter(x, y)
plt.title("Randomly generated linear regression task")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# Model function
def model(X, theta):
    return np.dot(X, theta)


# Mean-squared error loss function
def loss(hx, y):
    return np.sum((hx - y) ** 2) / (2 * n)


# Add bias column to X
X = np.concatenate([np.ones((n, 1)), x.reshape((n, 1))], axis=1)

# Solve for theta
theta = np.linalg.inv(X.T @ X) @ (X.T @ y)

# The optimal theta parameters found
print(f"Optimal theta paramter: {theta}")
# >> Optimal theta paramter: [-7.4071701   2.99279562]

# The final loss
print(f"Final loss: {loss(model(X, theta), y)}")
# >> Final loss: 0.4038588210616574

plt.scatter(x, y)
plt.plot(x, model(X, theta))
plt.title("Plot of linear regression line given parameters theta.")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
