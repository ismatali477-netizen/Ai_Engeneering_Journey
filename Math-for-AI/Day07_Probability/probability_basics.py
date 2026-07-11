def probability(favorable, total):
    if total==0:
        raise ZeroDivisionError("Total condition of a probability cannot be zero")
    return favorable/total

def complement(prob):
    return 1-prob

def independent_probability(p1, p2):
    return p1*p2

if __name__=="__main__":
    print(f"Probability of rolling a 6: {probability(1, 6):.3f}")
    print(f"Complement: {complement(probability(1, 6)):.3f}")
    print(f"Probability of Heads AND rolling a 6: {independent_probability(1/2, 1/6):.3f}")
