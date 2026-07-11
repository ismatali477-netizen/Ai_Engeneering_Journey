def square(x):
    return x**2
def numerical_derivative(function, x, h):
    return (function(x+h)-function(x))/h
if __name__ == "__main__":
    print(f"Estimated derivative: {numerical_derivative(square, 5, 0.0001):.2f}")