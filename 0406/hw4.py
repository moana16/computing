def sol(year) :
    if year % 400 == 0 : print(year,"년은 윤년입니다.")
    elif year % 100 == 0 : print(year,"년은 윤년이 아닙니다.")
    elif year % 4 == 0 :print(year,"년은 윤년입니다.")
    else :print(year,"년은 윤년이 아닙니다.")
    
def main() :
    while True :
        year = int(input("연도를 입력해주세요.")) 
        if year == 0:  
            print("프로그램을 종료합니다")
            break
        sol(year)

main()