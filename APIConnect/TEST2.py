import re

S = "안암건강랜드 앞 3층에 2017년 준공 신축 풀옵션 원룸 보500만/월65만"
numbers = re.findall("\d+", S)
print(numbers)