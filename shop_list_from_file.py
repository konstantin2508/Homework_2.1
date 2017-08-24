def get_cook_book_from_file():
    with open('dishes.txt') as f:
        cook_book = {}
        for line in f:
            dish_name = line.lower().strip()
            dish_amount = f.readline().strip()
            list_ingredient = []
            while True:
                ingredient = f.readline().strip()
                dict_ingredient = {}
                if '|' in ingredient:
                    ingredient = ingredient.split(' | ')
                    dict_ingredient['ingredient_name'] = ingredient[0]
                    dict_ingredient['quantity'] = int(ingredient[1])
                    dict_ingredient['measure'] = ingredient[2]
                    list_ingredient.append(dict_ingredient)
                else:
                    break
            cook_book[dish_name] = list_ingredient
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], 
                                shop_list_item['measure']))

def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    cook_book = get_cook_book_from_file()
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print_shop_list(shop_list)

create_shop_list()
