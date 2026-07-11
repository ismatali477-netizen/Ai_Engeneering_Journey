from random import randint
def simulate_dice_rolls(num_rolls):
    count_six=0
    for _ in range(num_rolls):
        roll=randint(1,6)
        if roll==6:
            count_six+=1
    return count_six/num_rolls
if __name__=="__main__":
    print(f"Probability of getting 6 in 10000 roll is: {simulate_dice_rolls(10000):.3f}")