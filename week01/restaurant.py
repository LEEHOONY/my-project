# 맛집 고르기
# 한식, 중식, 일식 중 한 가지를 고르라는 내용이 나옵니다
# 그 중 한가지를 고르면 식당이름을 하나 임의로 추천해줍니다.

restaurant = input("한식, 중식, 일식 중 한 가지를 고르세요.")

import random
List_a = ["비빔밥", "불고기", "김치찌개", "된장찌개", "순두부"]
List_b = ["짜장면", "짬뽕", "탕수육", "깐풍새우", "팔보채"]
List_c = ["초밥", "돈가스", "우동", "라면"]

if restaurant == "한식":
    print(random.choice(List_a))
elif restaurant == "중식":
    print(random.choice(List_b))
elif restaurant == "일식":
    print(random.choice(List_c))
else:
    print("한식, 중식, 일식 중에서만 선택하실 수 있습니다.")
