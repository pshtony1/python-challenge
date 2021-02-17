"""
1. 가짜 데이터베이스


명세의 조건들을 만족하면서,
아래의 3개 함수들을 수정하여 완성하세요.


이 설명이 담긴 주석과,
'건들지 마세요'로 둘러싸인 공간은
말 그대로 건들지 마세요.


+ 클래스로 구현한다면, '건들지 마세요' 공간을
수정해도 괜찮습니다. 다만, 적절한 테스트 코드를 작성해주세요.
"""


def add_people(_db, to_add):
    pass


def read_people(_db, to_read):
    pass


def delete_people(_db, to_delete):
    pass


# 가짜 데이터베이스
db = ["Kim", "James", "Austin"]

# ----------- 건들지 마세요 ----------- #
add_people(db, "Park")
print("Added People Park.")
print("Database:", db)
print("\nRead People 'James'. Result: ", read_people(db, "James"))
print("Read People 'Faker'. Result: ", read_people(db, "Faker"))
print("\nDelete People 'Austin'. Result: ", delete_people(db, "Austin"))
print("Database:", db)
print("\nDelete People 'Lion'. Result: ", delete_people(db, "Lion"))
print("Database:", db)
# ----------- 건들지 마세요 ----------- #