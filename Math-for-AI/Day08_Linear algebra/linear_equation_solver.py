import numpy as np
def solve_system(coefficients, answers):
    return np.linalg.solve(coefficients,answers)
if __name__ == "__main__":
    coefficients = np.array([
        [2, 1],
        [1, 1]
    ])

    answers = np.array([5, 3])

    x, y = solve_system(coefficients, answers)

    print(f"x = {x:.2f}")
    print(f"y = {y:.2f}")