# task 2
# формирование списка с продуктами

def get_shop_list_by_dishes(cook_book=dict(), dishes=list(), person_count=int()):
    product_list = dict()
    for dish in dishes:
        try:
            dish_list = cook_book[dish]
            for product in dish_list:
                if product["ingredient_name"] not in product_list.keys():
                    product_list[product["ingredient_name"]] = {
                        "measure": product["measure"], "quantity": (int(product["quantity"]) * person_count)}
                else:
                    product_list[product["ingredient_name"]]["quantity"] += (int(product["quantity"]) * person_count)
        except:
            print(f"\n\nБлюдо \"{dish}\" в кулинарной книге отсутствуют\n\n")
    return product_list
