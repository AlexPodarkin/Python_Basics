print("map")
text = ["ПриВет,", "аЛекСанДр", "пОдаРкиN"]
res1 = map(lambda x: x.title(), text)
print(*res1)
# map возвращает map объект (* распаковывает объект)

print("\nfilter")
numbers = [42, -73, 2014]
res3 = tuple(filter(lambda x: x > 0, numbers))
print(res3)

print("\nzip")
names = ["Иван", "Николай", "Пётр"]
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99]
for name, salary, award in zip(names, salaries, awards):
    print(f'{name} заработал {salary:.2f} денег и премию {salary * award:.2f}')

my_list = [1, 2, 2]
print(sum(my_list))
# прибавит 10 к результату (или начнет суммирование с 10-ки)
print(sum(my_list, start=10))
