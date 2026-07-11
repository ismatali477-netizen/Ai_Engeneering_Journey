def probability_two_red(red, blue):
    total=red+blue
    return (red/total)*((red-1)/(total-1))

if __name__=="__main__":
    print(f"Probability of drawing two red balls:{probability_two_red(3,2):.3f}")
