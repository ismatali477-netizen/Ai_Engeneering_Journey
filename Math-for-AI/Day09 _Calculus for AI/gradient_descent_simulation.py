def loss(x):
    return x**2

def gradient(x):
    return 2*x

def train(start, learning_rate, steps):
    new_x=0
    for _ in range(steps):
        new_x=start-learning_rate*gradient(start)
        start=new_x
    return new_x
if __name__ == "__main__":
    final_x = train(start=5, learning_rate=0.1, steps=10)

    print(f"Final x: {final_x:.4f}")
    print(f"Final loss: {loss(final_x):.4f}")