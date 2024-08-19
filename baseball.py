import random
while True:
    print('숫자 야구 게임을 시작합니다.\nGame Start')
    X= random.randrange(1,10)
    while True:
        Y=random.randrange(1,10)
        if Y!=X:
            break
    while True:
        Z=random.randrange(1,10)
        if Z!=Y and Z!=X:
            break
    while True:
        num=input('숫자를 입력해주세요 :  ')
        
        S=0
        B=0
        for i in range(3):
            cmp=int(num[i])
                 
            if i==0:
                if cmp==X:
                    S+=1
                elif cmp==Y or cmp==Z:
                    B+=1
            elif i==1:
                if cmp==Y:
                    S+=1
                elif cmp==X or cmp==Z:
                    B+=1
            else:
                if cmp==Z:
                    S+=1
                elif cmp==Y or cmp==X:
                    B+=1
        if B>0:
            print(f'{B}B',end=' ')
        if S>0:
            print(f'{S}S',end='')
        if B==0 and S==0:
            print('OUT')
        else:
            print('')
        if S==3:
            break
    print('3개의 숫자를 모두 맞히셨습니다! 게임 종료\n게임을 새로 시작하려면 Y, 종료하려면 N을 입력하세요.')
    cnt11=0
    while True:
        if cnt11==3:
            print('제대로 좀 입력해라 에휴 난 간다ㅂㅂ')
            break
        re=input()
        if re=='N':
            print('종료!')
            break
        elif re=='Y':
            continue
        else:
            cnt11+=1
            print('잘못된 입력입니다. 다시입력해주세요')
        
    

        

        