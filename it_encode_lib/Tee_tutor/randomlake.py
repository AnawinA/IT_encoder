'''pep8borntojudge'''
import random
def main():
    '''pep9'''
    print("Welcome \n1. +\n2. -\n3. *\n4. /")
    var=""
    error="0"
    while error=="0":
        mode_program=str(input("Please Select : "))
        if mode_program=="1":
            var ="+"
            error="1"
        elif mode_program=="2":
            var ="-"
            error="1"
        elif mode_program=="3":
            var ="x"
            error="1"
        elif mode_program=="4":
            var ="/"
            error="1"
        else:
            error="0"
            print("invalid key Try again . . .")
    minimum_number=int(input("minimum : "))
    maximum_number=int(input("maximum : "))
    prob_length=int(input("number ex.0-100 : "))
    for i in range(1,prob_length+1):
        proba=random.randint(minimum_number,maximum_number)
        probb=random.randint(minimum_number,maximum_number)
        print(f"{i}.) {proba} {var} {probb} = ")
main()
