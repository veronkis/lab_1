import classes as cl

data = cl.JsonHandler.load_from_json()

while True:
    choice = int(input("Выберите действие: \n1-Создать фильм\n2-Создать сериал\
                       \n3-Создать пользователя \n4-Считать JSON в массив\
                       \n5-Считать XML в массив\n6-Вывести JSON\n7-Вывести XML\n"))
    if choice == 1:
        #создать фильм
        film = cl.Film()
        film.set_title()
        film.set_duration()
        film.set_rating()
        
        print("Вы ввели:", str(film))

        while True:
            xoj = int(input("Сохранить в JSON или в XML?\n1-JSON\n2-XML\n"))
            if xoj == 1:    
                data["movies"].append(film.to_dict())
                cl.JsonHandler.save_to_json(data)
                break
            elif xoj == 2:
                data['movies'].append(film.to_dict())
                cl.XmlHandler.save_to_xml(data)
                print()
                break
            else:
                print("Неверный выбор")
        break
    elif choice == 2:
        #создать сериал
        serial = cl.Serial()
        serial.set_title()
        serial.set_num_of_ep()
        serial.set_rating()
        
        print("Вы ввели: ", str(serial))

        while True:
            xoj = int(input("Сохранить в JSON или в XML?\n1-JSON\n2-XML\n"))
            if xoj == 1:    
                data["serials"].append(serial.to_dict())
                cl.JsonHandler.save_to_json(data)
                break
            elif xoj == 2:
                data['serials'].append(serial.to_dict())
                cl.XmlHandler.save_to_xml(data)
                print()
                break
            else:
                print("Неверный выбор")

        break
    elif choice == 3:
        #создать пользователя
        user = cl.User()
        user.set_username()
        user.set_browsing_history()
        
        print("Вы ввели: ", str(user))

        while True:
            xoj = int(input("Сохранить в JSON или в XML?\n1-JSON\n2-XML\n"))
            if xoj == 1:    
                data["users"].append(user.to_dict())
                cl.JsonHandler.save_to_json(data)
                break
            elif xoj == 2:
                data['users'].append(user.to_dict())
                cl.XmlHandler.save_to_xml(data)
                break
            else:
                print("Неверный выбор")
        break
    elif choice == 4:
        #json в массив
        res = cl.JsonHandler.data_to_dict(data)
        print(res)
        break
    elif choice == 5:
        #xml в массив
        res = cl.XmlHandler.data_to_dict(data)
        print(res)
        break
    elif choice == 6:
        #вывести json
        cl.JsonHandler.print_data(data)
        break
    elif choice == 7:
        #вывести xml
        cl.XmlHandler.print_data(data)
        print()
        break
    else:
        print("Неверный выбор")
    