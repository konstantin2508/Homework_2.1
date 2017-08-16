def get_cook_book_from_file_json_ymal():
    import json
    import yaml
    import sys
    try:
        with open('dishes.json') as dishes_file:
            dishes = json.load(dishes_file)
            print('Открываем файл *.json')
    except IOError:
        try:
            with open('dishes.yml', encoding='utf-8') as dishes_file:
                dishes = yaml.load(dishes_file)
                print('Открываем файл *.yaml')
        except IOError:
            print('Нужные файлы отсутствуют')
            sys.exit()
		
    list_dishes = {}
    cook_book = {}
    for dish in dishes.values():
        list_dishes[dish['dish_name']] = dish['dish_amount']
        cook_book[dish['dish_name']] = dish['ingredients']
    return list_dishes, cook_book
	
def get_shop_list_by_dishes(dishes, cook_book):
    shop_list = {}
    for dish in list(dishes.keys()):
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= dishes[dish]
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    print('\nСписок продуктов:')        
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], 
                                shop_list_item['measure']))

def create_shop_list():
    dishes, cook_book = get_cook_book_from_file_json_ymal()
    shop_list = get_shop_list_by_dishes(dishes, cook_book)
    print_shop_list(shop_list)
    
create_shop_list()
	

	
	
