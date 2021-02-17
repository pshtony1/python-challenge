"""
2. 모르는 사이에 완성된 계산기


명세의 조건들을 만족하는 함수들을
추가적으로 작성해주세요.


- factorial: 인자로 받는 N에 대한 팩토리얼의 결과를 리턴해주세요.
- root_formula: 인자 a, b, c는 각각 이차 방정식에서 ax^2+bx+c 에 해당하는 값들입니다. 이 값을 토대로 근의 공식에 대입한 결과를 리턴해주세요.
- between_sum: 인자 a, b 사이(a 이상 b 이하)에 존재하는 모든 정수의 합을 리턴해주세요.


이 설명이 담긴 주석과,
'건들지 마세요'로 둘러싸인 공간은
말 그대로 건들지 마세요.


+ 클래스로 구현한다면, '건들지 마세요' 공간을
수정해도 괜찮습니다. 다만, 적절한 테스트 코드를 작성해주세요.
"""


def add(a, b):
    result = a + b
    return result


def sub(a, b):
    result = a - b
    return result


def mul(a, b):
    result = a * b
    return result


def div(a, b):
    result = a / b
    return result


def factorial(n):
    pass


def root_formula(a, b, c):
    pass


def between_sum(a, b):
    pass


# ----------- 건들지 마세요 ----------- #

print("< 계산기 >\n")
print("1. 덧셈\n2. 뺄셈\n3. 곱셈\n4. 나눗셈\n5. 팩토리얼\n6. 근의 공식\n7. a와 b사이의 합\n8. 종료")

while True:
    try:
        menu = int(input("\n수행할 기능을 숫자로 입력해주세요 >> "))
        break

    except:
        print("입력한 값은 정수가 아닙니다.\n")

print()

# ----------- 건들지 마세요 ----------- #

if menu == 1:
    a = int(input("첫 번째 숫자: "))
    b = int(input("두 번째 숫자: "))
    print(add(a, b))

elif menu == 2:
    a = int(input("첫 번째 숫자: "))
    b = int(input("두 번째 숫자: "))
    print(sub(a, b))

elif menu == 3:
    a = int(input("첫 번째 숫자: "))
    b = int(input("두 번째 숫자: "))
    print(mul(a, b))

elif menu == 4:
    a = int(input("첫 번째 숫자: "))
    b = int(input("두 번째 숫자: "))
    print(div(a, b))

# 팩토리얼 계산 기능을 완성해주세요.
elif menu == 5:
    print("기능이 아직 구현되지 않았습니다.")

# 근의 공식 계산 기능을 완성해주세요.
elif menu == 6:
    print("기능이 아직 구현되지 않았습니다.")

# 특정 범위의 합 계산 기능을 완성해주세요.
elif menu == 7:
    print("기능이 아직 구현되지 않았습니다.")

elif menu == 8:
    print("계산기를 종료합니다.")

else:
    print("잘못된 값을 입력했습니다.\n")
