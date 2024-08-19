
def comma(x):
    result=''
    change=False
    if x[0]=='-':
        x1=x[1:]
        change=True
    else: 
        x1=x
    cnt=len(x1)
    for i in x1:
        result+=i
        if cnt%3==1 and cnt!=1:
            result+=','
        cnt-=1
    if change:
        result='-'+result
    return result
print("숫자 콤마 찍어주는 프로그램 시작하겠습니다!! :>")
cnt = 0

while True :
    if cnt == 3 :
        print("3번 틀렸습니다")
        break
    X = input("20자리 이하의 수를 입력해주세요: ")

    if X[0]!='-' and not X.isdigit() :
        print("숫자를 입력해주세요")
        cnt+=1
        continue

    if len(X) > 20 :
        print("20자리 이하의 숫자를 입력하시오")
        cnt += 1
        continue
    print(comma(X))
    break
