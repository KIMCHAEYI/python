information = {"고향":"경기", "취미":"웨이트", "좋아하는 음식":"그린샐러드"}
foods = ["된장찌개", "피자", "제육볶음"]
print(information.get("취미"))
information["특기"] = "피아노"
information["사는 곳"] = "서울"
del information["좋아하는 음식"]
print(information)
print(len(information))
information.clear()
print(information)
print(foods[-2])
foods.append("김밥")
del foods[1]
print(foods)   


