import random
from builtins import range

scrt_code = '2315'

def random_number():
    return random.randint(0, 9)

def check_number_exist(limit):
    rn = []
    i = 0
    while i < limit:
        num = random_number()
        if rn.count(num) == 0:
            rn.append(num)
            i += 1
    return rn
def check_number(pGuess):
    checkValue=True
    i=0
    while i < 4:
        if pGuess.count(pGuess[i]) == 1:
            checkValue=True
            i += 1
        else:
            checkValue=False
            return False
            break
    return checkValue

#print(check_number_exist(4))
def start():
    bull = 0
    cow = 0
    pw=0
    cw=0
    player=''
    while bull <= 4 and cw==0 and pw==0:
        pGuess=input('Enter your guess : ')
        bull = 0
        cow = 0
        #print(check_number(pGuess))
        if len(pGuess)==4 and check_number(pGuess):
            j=0
            x=0
            for j in pGuess:
                cow += scrt_code.count(j)
                if j==scrt_code[x]:
                    bull+=1
                    cow-=1
                    x += 1
                else:
                    x += 1
            print('bull =',bull,', cow =',cow,'\n')
            if bull==4:
                print("!!! You Win !!!")
                pw=1
                break
        else:
            print("Enter the corrct Number ! \n")
        cGuess=check_number_exist(4)
        bull = 0
        cow = 0
        print('Computer guess :',*cGuess)
        if len(cGuess)==4:
            j=0
            x=0
            for j in cGuess:
                cow += scrt_code.count(str(j))
                if j==scrt_code[x]:
                    bull+=1
                    cow-=1
                    x += 1
                else:
                    x += 1
            print('bull =',bull,', cow =',cow,'\n')
            if bull==4:
                print("!!!!! Computer win win!!!!!")
                cw=1
                break

start()

