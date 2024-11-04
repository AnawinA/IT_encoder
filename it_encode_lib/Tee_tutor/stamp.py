'''pep8'''
""" import random
def main():
    '''fwedscx'''
    a = random.randint(0,19)
    b = random.randint(0,29)
    c = random.randint(10,29)
    d = random.randint(10,19)
    num = 1
    heart = 5
    score = 0
    while heart>0:
        a = random.randint(0,9)
        b = random.randint(0,9)
        c = random.randint(0,9)
        d = random.randint(0,9)
        print("\n\n-------------score =",score,"-------- heart =",heart,"-----------------")
        print(f"{num}.) {a} + {b} + {c} + {d} = ")
        x = int(input())
        if x != a+b+c+d:
            heart -= 1
            if score >= 0.25:
                score -= 0.25
            print("incorrect")
        else:
            score += 1
            print("correct")
        num += 1
    print("Game Over your score is",score)
main()
 """