from tasks.task_1 import create_cook_book
from tasks.task_2 import get_shop_list_by_dishes

cook_book = create_cook_book("recipes.txt")

# представление списка с рецептами блюд
# Задача 1
for cook in cook_book.keys():
    print(cook, cook_book[cook])

first_dishes = ["Омлет", "Фахитос"]
second_dishes = ["Утка по-пекински", "Запеченный картофель", "Фахитос"]
third_dishes = ["Стейк из говвядины", "Омлет", "Фахитос"]

product_list = get_shop_list_by_dishes(cook_book=cook_book,
                                       dishes=third_dishes,
                                       person_count=3)

# представление списка с необходимыми продуктами
# Задача 2
for product in product_list.keys():
    print(product, product_list[product])