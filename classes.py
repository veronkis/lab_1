import json 
import xml.etree.ElementTree as et

#-----------------------------------------------

filenamexml = "data.xml"
filenamejson = "data.json"

#-----------------------------------------------

class XmlHandler:

    # Функция для красивых отступов 
    def indent(elem, level = 0) -> None:
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for subelem in elem:
                XmlHandler.indent(subelem, level + 1)
            if not subelem.tail or not subelem.tail.strip():
                subelem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
        pass

    # Функция сохранения информации в xml
    def save_to_xml(data) -> None:
        root = et.Element('data')

        movies = et.SubElement(root, 'movies')
        for movie in data['movies']:
            movie_element = et.SubElement(movies, 'movie')
            for key, value in movie.items():
                child = et.SubElement(movie_element, key)
                child.text = str(value)  

        tvseries = et.SubElement(root, 'serials')
        for series in data['serials']:
            series_element = et.SubElement(tvseries, 'serial')
            for key, value in series.items():
                child = et.SubElement(series_element, key)
                child.text = str(value)  

        # Добавляем отступы для красивого форматирования
        XmlHandler.indent(root)

        # Создаем дерево XML и записываем его в файл
        tree = et.ElementTree(root)
        tree.write(filenamexml, encoding='utf-8', xml_declaration=True)

        print(f"Данные успешно сохранены в файл '{filenamexml}'")
        pass

    # Функция чтения информации из xml
    def load_from_xml() -> dict:
        try:
            tree = et.parse(filenamexml)
            root = tree.getroot()
        except FileExistsError:
            return {"movies" : [], "serials" : []}
        
        data = {"movies" : [], "serials" : []}

        for movie in root.find("movies"):
            movie_data = {}
            for child in movie:
                movie_data[child.tag] = child.text
            data["movies"].append(movie_data)

        for serial in root.find("serials"):
            serial_data = {}
            for child in serial:
                serial_data[child.tag] = child.text
            data["serials"].append(serial_data)

        return data
    
    def print_data(data):
        print("\nДанные из XML:")

        print("\nФильмы:")
        for movie in data['movies']:
            print(f"Название: {movie['title']}, Длительность: {movie['duration']} мин, \
Рейтинг: {movie['rating']}")

        print("\nСериалы:")
        for series in data['serials']:
            print(f"Название: {series['title']}, Эпизодов: {series['num_of_ep']}, \
Рейтинг: {series['rating']}")
        
        pass

    def data_to_dict(data) -> dict:
        while True:
            choice = int(input("Что записать в массив?\n1-Фильмы\n2-Сериалы\n"))
            if choice == 1:
                res = []
                for movie in data['movies']:
                    res.append(movie)
                print("Данные успешно сохранены в массив \n")
                return res
            elif choice == 2:
                res = []
                for movie in data['serials']:
                    res.append(movie)
                print("Данные успешно сохранены в массив \n")
                return res
            else:
                print("Неверный выбор")

#-----------------------------------------------

class JsonHandler:

    # Функция сохранения информации в json
    def save_to_json(data) -> None:
        with open(filenamejson, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            print("Данные успешно сохранены")
        pass

    # Функция для чения информации из json
    def load_from_json() -> dict:
        try:
            with open(filenamejson, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"movies": [], "serials": []}

    # Функция вывода ниформации из json
    def print_data(data) -> None:
        print("\nДанные из JSON:")
    
        print("\nФильмы:")
        for movie in data['movies']:
            print(f"Название: {movie['title']}, Длительность: {movie['duration']} мин, \
Рейтинг: {movie['rating']}")

        print("\nСериалы:")
        for series in data['serials']:
            print(f"Название: {series['title']}, Эпизодов: {series['num_of_ep']}, \
Рейтинг: {series['rating']}")
        
        pass

    # Функция записи информации в массив
    def data_to_dict(data) -> dict:
        while True:
            choice = int(input("Что записать в массив?\n1-Фильмы\n2-Сериалы\n"))
            if choice == 1:
                res = []
                for movie in data['movies']:
                    res.append(movie)
                print("Данные успешно сохранены в массив \n")
                return res
            elif choice == 2:
                res = []
                for movie in data['serials']:
                    res.append(movie)
                print("Данные успешно сохранены в массив \n")
                return res
            else:
                print("Неверный выбор")


#-----------------------------------------------

class Media:
    title = ""
    rating = 0

    def __init__(self, inp_title = "", inp_rating = 0) -> None:
        self.title = inp_title
        self.rating = inp_rating
        pass

#-----------------------------------------------

class Serial(Media):
    title = ""
    num_of_ep = 0
    rating = 0

    def __init__(self, inp_title = "", inp_num_of_ep = 0, inp_rating = 0) -> None:
        super().__init__(inp_title, inp_rating)
        self.num_of_ep = inp_num_of_ep
        pass

    def set_title(self) -> None:
        self.title = input("Введите название сериала: ")
        pass
  
    def set_rating(self) -> None:
        while True:
            try:
                rating = float(input("Введите рейтинг фильма: "))
                if rating < 0 or rating > 5:
                    print("Рейтинг фильма может быть только от 0 до 5")
                else:
                    self.rating = rating
                    break
            except ValueError:
                print("Рейтинг фильма может быть только вещественным числом")
        pass

    def set_num_of_ep(self) -> None:
        while True:
            try:
                eps = int(input("Введите количество серий в сериале: "))
                if eps <= 0:
                    print("Количество серий должно быть положительным")
                else:
                    self.num_of_ep = eps
                    break
            except ValueError:
                print("Количество серий может быть только целым числом")
        pass

    def get_title(self) -> str:
        return self.title

    def get_num_of_ep(self) -> int:
        return self.num_of_ep
    
    def get_rating(self) -> float:
        return self.rating

    def to_dict(self) -> dict:
            return {
            "title": self.title,
            "num_of_ep": self.num_of_ep,
            "rating": self.rating
        }

    def __str__(self) -> str:
        return f"Сериал: {self.title}, количество эпизодов: {self.num_of_ep}, рейтинг: {self.rating}"

#-----------------------------------------------

class Film(Media):
    title = ""
    duration = 0
    rating = 0

    def __init__(self, inp_title = "", inp_duratoin = 0, inp_rating = 0) -> None:
        super().__init__(inp_title, inp_rating)
        self.duration = inp_duratoin
        pass

    def set_title(self) -> None:
        self.title = input("Введите название фильма: ")
        pass

    def set_duration(self) -> None:
        while True:
            try:
                duration = int(input("Введите хронометраж фильма в минутах: "))
                if duration <= 0:
                    print("Хронометраж должно быть быть положительным")
                else:
                    self.duration = duration
                    break
            except ValueError:
                print("Хронометраж фильма может быть только целым числом")
        pass

    def set_rating(self) -> None:

        while True:
            try:
                rating = float(input("Введите рейтинг фильма: "))
                if rating < 0 or rating > 5:
                    print("Рейтинг фильма может быть только от 0 до 5")
                else:
                    self.rating = rating
                    break
            except ValueError:
                print("Рейтинг фильма может быть только вещественным числом")
        pass

    def get_title(self) -> str:
        return self.title

    def get_duration(self) -> int:
        return self.duration
    
    def get_rating(self) -> float:
        return self.rating
    
    def to_dict(self) -> dict:
            return {
            "title": self.title,
            "duration": self.duration,
            "rating": self.rating
        }

    def __str__(self) -> str:
        return f"Фильм: {self.title}, хронометраж: {self.duration}, рейтинг: {self.rating}"