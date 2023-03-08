# s = 'Welcome to python'
# # p = s.split()

# s1 = '2021.8.15'
# #p = s1.split('.')  #-> split은 공백이 두칸 이상이거나 앞뒤에 공백이 있을 결루 적용할 수 없음 -> 개별문자로 분리하기 위해서는 list() 호출

# s2 = 'Welcome, to\t,  python, and, \n  bla,  bla     '
# # p = s2.split(',')
# # p = [x.strip() for x in s2.split(',')] # 반복문을 활용하여 split된 문자열에 strip을 적용!
# # p2 = list('hello world  !!!') # list는 주어진 객체를 리스트화하는 함수


# # p = ', '.join(['apple','grape','banana'])
# # p2 = '-'.join('010.2349.6632'.split('.'))

# t = s2.split()
# p = '010.  2349.  6632'.replace('.  ','-')
# p2 = ' '.join(t)


# s = '    hello my nAME is jaeYyoo!    '
# p = s.find('o')

import re

# txt1 = 'Life is too short, you need python.'
# txt2 = 'The best moments of my life.'

# match = re.search('Life', txt1)
# match.group() # 검색의 결과가 여러개의 그룹으로 나타날 경우에 필요함
# match.start() # 문자열 시작 위치
# match.end() # 문자열 끝 위치
# match.span() # 문자열의 (시작, 끝)에 해당하는 튜플


# re.search('Life|life', txt2) # | 또는 연산자
# re.search('[Ll]ife', txt2) # [] 를 통한 범위 표현, [0-9] 가능
# re.search('^Life', txt2) # ^ 첫 단어인지 검색
# re.search('Life$', txt2) # $ 마지막에 위치하는지 검색


# p = re.search('AB*', 'CBA')
# p2 = re.search('AB+', 'CBA')

txt3 = 'My life my life my life in the sunshine'
p2 = re.findall('[Mm]y',txt3)
print(p2)


