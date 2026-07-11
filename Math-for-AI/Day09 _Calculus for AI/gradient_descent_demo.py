def loss(x):
    return x**2

def gradient(x):
    return 2*x

def one_gradient_step(x, learning_rate):
    return x-learning_rate*gradient(x)

if __name__ == "__main__":
    x = 5
    print(f"Initial x: {x}")
    print(f"Loss: {loss(x)}")
    print(f"Gradient: {gradient(x)}")
    print(f"Updated x: {one_gradient_step(x, 0.1)}")