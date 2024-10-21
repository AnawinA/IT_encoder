'''pep8borntojudge'''
import random
def main():
    '''pep9'''
    error=24
    score=41
    while score <=72 :
        proba=random.randint(100,999)
        print(f"{score}.) {proba} * 999 = ")
        
        answer_user=int(input("your answer : "))
        if answer_user != proba * 999 :
            error-=1
            print("wrong answer, heart = ",error,", score = ", score)
        else:
            score+=1
            print("correct answer, heart = ",error, ", score = ", score)
    print("game over")
    
        score += 1
main()
