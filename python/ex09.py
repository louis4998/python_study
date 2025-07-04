value=int(input("정수를 입력하시오."))
res = ((value//1000) + (value%1000//100)+ (value%100//10)+ (value%10))

print(res)