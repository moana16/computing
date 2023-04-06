def sol(h,w):
    if h == 0 or w == 0 :  return 0
    h = 0.01 * h
    BMI = w / h**2
    if BMI <= 18.5 : print("당신은 저체중 입니다.")
    elif BMI > 18.5 and BMI <= 22.9 : print("당신은 정상 입니다.")
    elif BMI >= 23.0 and BMI <= 24.9 : print("당신은 과체중 입니다.")
    elif BMI >= 25.0  : print("당신은 비만 입니다.")


h = int(input("당신의 키는 몇 cm인가요?"))
w = int(input("당신의 몸무게는 몇 kg인가요?"))
sol(h,w)