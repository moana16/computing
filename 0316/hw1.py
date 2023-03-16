name = input('당신의 이름은 무엇인가요? ')
year = int(input('%s 씨 안녕하세요. 몇년도에 태어났나요?'%name))
age = 2023 - year + 1
print('그러면 당신은 지금 %d살이군요.' %age)
print('5년 후에는',age+5 ,'살이 되겠군요. ')