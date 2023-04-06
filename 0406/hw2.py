def sol(h,w):
    if h == 0 or w == 0 :  return 0
    h = 0.01 * h
    BMI = w / h**2
    print("당신의 BMI 수치는 %.2f 입니다." %BMI)

h = int(input("당신의 키는 몇 cm인가요?"))
w = int(input("당신의 몸무게는 몇 kg인가요?"))
sol(h,w)