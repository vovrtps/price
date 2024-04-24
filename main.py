import re
import os
import csv

class PriceMachine():

    def __init__(self):
        self.price_list = []

    def sca_price_list_names(self, folder_price):
        self.folder_price = folder_price
        condition = r'price_\d'
        for root, dirs, files in os.walk(self.folder_price):
            for file in files:
                if re.match(condition, file):
                    way = '/'.join((self.folder_price, file))
                    self.price_list.append(way)


    def ordering_price_list(self):
        while True:
            title = input('Введите правильное название продукта: ') + ' '
            title = title.title()
            list_of_data = dict()
            result = []
            if title == "Exit ":
                print('Работа завершена')
                return
            else:
                for ways in self.price_list:
                    with open(ways, 'r', newline='', encoding='utf-8') as f:
                        data = csv.DictReader(f, delimiter=',')
                        for all_data in data:
                            for key, value in all_data.items():
                                if key == 'название' or key == 'товар' or key == 'наименование':
                                    list_of_data['продукт'] = value
                                elif key == 'розница':
                                    list_of_data['цена'] = value
                                elif key == 'фасовка' or key == 'масса':
                                    list_of_data['вес'] = value
                                else:
                                    list_of_data[key] = value

                            if list_of_data['продукт'][:4] == title[:4]:
                                price_kg = int(list_of_data['цена']) // int(list_of_data['вес'])
                                result.append([list_of_data['продукт'], list_of_data['цена'], list_of_data['вес'], ways, price_kg])
                            else:
                                continue

                result.sort(key=lambda i : i[4])
                for result_of_request in result:
                    print(result_of_request)


pm = PriceMachine()
pm.sca_price_list_names("price")
pm.ordering_price_list()

