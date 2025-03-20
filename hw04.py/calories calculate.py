calories=[50,34,77] # 한라봉, 딸기, 바나나

eat_hallabong=int(input("섭취한 한라봉의 양을 입력해주세요=> "))

eat_strawberry=int(input("섭취한 딸기의 양을 입력해주세요=>"))

eat_banana=int(input("섭취한 바나나의 양을 입력해주세요=>"))

total_calories=calories[0]*eat_hallabong/100 + calories[1]*eat_strawberry/100 + calories[2]*eat_banana/100

print(f"섭취하신 칼로리의 총량은 {total_calories} kcal 입니다.")
