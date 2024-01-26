# Задача 1.
# Чтение файла
# Формирование книги рецептов

def create_cook_book(path_to_cook_book):
    with(open(path_to_cook_book, 'r', encoding="utf-8") as f):
        recipes = f.read().splitlines()

    sort_recipe = list()
    temp_recipe = list()

    for i in range(len(recipes)):
        if recipes[i] != "":
            temp_recipe.append(recipes[i])
            if i == (len(recipes) - 1):
                sort_recipe.append(temp_recipe)
                temp_recipe = []
        else:
            sort_recipe.append(temp_recipe)
            temp_recipe = []

    cook_book = dict()

    for recipe in sort_recipe:
        food_name = ""
        for i in range(len(recipe)):
            if i == 0:
                food_name = recipe[0]
                cook_book[food_name] = []

            if i > 1:
                ingredient = recipe[i].split(" | ")
                ingredient_dict = dict()

                ingredient_dict["ingredient_name"] = ingredient[0]
                ingredient_dict["quantity"] = ingredient[1]
                ingredient_dict["measure"] = ingredient[2]

                cook_book[food_name].append(ingredient_dict)

    return cook_book
