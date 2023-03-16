import time
height = float(input('당신의 키는 몇 cm인가요?'))
print('인치 단위로 변환해서 알려줄께요.')
height_inch = height / 2.54
time.sleep(1.5)
print('당신의 키는 %.2f inch입니다.' %height_inch)
