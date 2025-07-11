import random 

num1=random.randrange(1,10)
num2=random.randrange(1,10)

cal=random.randint(1,4)

if  cal==1:
        answer=num1+num2
        reply=int(input("{0}+{1}의 값은?". format(num1,num2)))
        if answer==reply:
                print("맞았습니다.")
        else:
                print("틀렸습니다.")
elif    cal==2:
        answer=num1-num2
        reply=int(input("{0}-{1}의 값은?"   .format(num1,num2)))
        if answer==reply:
                print("맞았습니다.")
        else:
                print("틀렸습니다.")
elif    cal==3:
        answer=num1*num2
        reply=int(input("{0}*{1}의 값은?"   .format(num1,num2)))
        if answer==reply:
                print("맞았습니다.")
        else:
                print("틀렸습니다.")
elif   cal==4:
        answer=num1/num2
        reply=int(input("{0}/{1}의 값은?"   .format(num1,num2)))
        if answer==reply:
                print("맞았습니다.")
        else:
                print("틀렸습니다.")
else:
        print("")