"""
3. 약간의 소금


아래 링크는 salt 생성기를 만들 때 도움이 될 링크입니다!
- Random 라이브러리: https://wikidocs.net/33#random
- 숫자를 문자로: https://wikidocs.net/32#chr


명세의 조건들을 만족하는 함수를 완성해주세요.
- create_salt 함수를 완성해주세요.


이 설명이 담긴 주석과,
'건들지 마세요'로 둘러싸인 공간은
말 그대로 건들지 마세요.
"""


def create_salt():
    return ""


# ----------- 건들지 마세요 ----------- #

password = "1234"
print("Password + Hash:", hash(password))

salt = create_salt()
print("Created salt is:", salt)
print("Password + Salt + Hash:", hash(password + salt))

# ----------- 건들지 마세요 ----------- #
