# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# Set the number of data points
n = 10

# Generate data of the form y = m(x + e) + b
slope = np.random.randint(0, 5)
bias = np.random.randint(-10, 10)
noise = np.random.rand(n)

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
def model(x, w, b):
    return w * x + b


# Mean-squared error loss function
def loss(hx, y):
    return np.sum((hx - y) ** 2) / (2 * n)


# Gradient of model parameters given loss function
def gradient(x, w, b, y):
    hx = model(x, w, b)
    dw = np.dot(x, hx - y) / n
    db = np.sum(hx - y) / n
    return dw, db


# Utility function to plot model
def plot_model(x, w, b, y):
    plt.scatter(x, y)
    plt.plot(x, model(x, w, b))
    plt.title("Plot of linear regression line given parameters (w, b).")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


# Set hyperparameters
LEARNING_RATE = 0.01
EPOCHS = 1000

# Initialize weights and biases
w = np.random.randn(1)
b = np.random.rand(1)

# Initial random parameters
print(f"Initial random parameters: w = {w}, b = {b}")
# >> w = [0.02222183], b = [0.39986097]

# Plot initial model.
plot_model(x, w, b, y)
print(f"Initial loss: {loss(model(x, w, b), y)}.")
# >> Initial loss: 52.26399596665648.

for e in range(EPOCHS):
    # forward pass
    hx = model(x, w, b)
    # compute loss
    l = loss(hx, y)
    # print loss every 100 epochs
    if e % 100 == 0:
        print(f"Epoch {e} loss: {l}")
    # compute gradient
    dw, db = gradient(x, w, b, y)
    # update weight and bias
    w = w - LEARNING_RATE * dw
    b = b - LEARNING_RATE * db

# Plot final learned model.
plot_model(x, w, b, y)
print(f"Final loss: {loss(model(x, w, b), y)}.")
# >> Final loss: 0.4368929979980659.

# Final learned parameters
print(f"Learned parameters: w = {w}, b = {b}")
# >> Learned paramters: w = [2.91661742], b = [-6.92948815]
