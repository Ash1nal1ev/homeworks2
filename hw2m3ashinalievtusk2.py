# Задача №1 Наследование
# 1. Создать трехступенчатую концепцию (дед-отец-ребенок) любого примера который вам ближе
# 2. Все три класса должны иметь свои особенные методы и атрибуты как минимум два доп метода у каждого класса
# 3. Также создать хотя бы по одному объекту к каждому классу
class Gradfather:
    def _init_(self, name, age, hobby):
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('Age should be int')
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('name should be string')
        if isinstance(hobby, str):
            self.hobby = hobby
        else:
            raise ValueError('hobby input should be boolean')

    def _str_(self):
        return f'Name: {self.name}\n' \
                f'Age: {self.age}\n' \
                f'Hobby: {self.hobby}'
Gradfather_1 = Gradfather(name="Tolik", age=72, hobby="Regbi")
print(Gradfather_1)
class Father(Gradfather):
    def _init_(self,name, age, hobby,work ):
        super()._init_(name, age, hobby)
        if isinstance(work, str):
            self.work = work
        else:
            raise ValueError('Work shouldbe str')
    def _str_(self):
        return super()._str_() + f'\nWork: {self.work}'
Father_1 = Father(name = "Kesha", age=43, hobby="Basketball",work="Dentist" )
print(Father_1)
class Boyfrend(Father):
    def _init_(self,name, age, hobby,work,girlfrend):
        super()._init_(name, age, hobby,work)
        if isinstance(girlfrend, str):
            self.girlfrend = girlfrend
        else:
            raise ValueError('girlfrend should be string')
    def _str_(self):
        return super(Father, self)._str_() + f'\nGirlfrend: {self.girlfrend}'
Boyfrend_1=Boyfrend(name = "Gena",age=23,hobby="Football",work="proger",girlfrend="Anjelika")
print(Boyfrend_1)
class Phone:
    def _init_(self,number,email,password):
        if isinstance(number, int):
            self.number = number
        else:
            raise ValueError('Number should be int')
        if isinstance(email, str):
            self.email = email
        else:
            raise ValueError('email should be str')
        if isinstance(password, str):
            self.__password = password
        else:
            raise ValueError('Password should be string')
    def __photo(self, private_video):
        return f'Photo: {private_video}'
    def _video(self, private_contacts):
        return f'Contact: {private_contacts}'
    def _str_(self):
        return f'Number: {self.number}\n' \
                f'Email: {self.email}\n' \
                f'Password: {self.password}'
Phone_1=Phone(number=555555,email="aktan@gmail.com",password="geektech_")
print(Phone_1)
class Proger:
    def _init_(self, proces):
        self.proces = proces
    def work(self):
        return f'Work with computer'
class Taxit:
    def _init_(self, proces):
        self.proces = proces
    def work(self):
        return f'Work with car'
class Dentist:
    def _init_(self, proces):
        self.proces = proces
    def work(self):
        return f'Work with teeth'
#print(Proger.work(),Taxit.work(),Dentist.work())
class Optometrist:
    def _init_(self, treat):
        self.treat = treat
    def treat_(self):
        return f'Treat eyes'
class Dentist2(Optometrist):
    def _init_(self, treat):
        super()._init_(treat)
    def treat(self):
        return f'Treat teeth  '
class Terapepht(Dentist2):
    def _init_(self, treat):
        super()._init_(treat)
    def _treat_(self):
        return f'Treat belly '





# Задача №2 Инкапсуляция
# 1. Создать один класс в котором вы пропишете по одному методу (внутреннего и защищенного)
# 2. В этом классе должно быть также по одному атрибуту (внутреннего и защищенного)
# Задача № 3 Полиморфизм без наследования
# 1. Создать три разных класса в котором будут одинаковые методы по названию например (attack)
# 2. Но логика этого самого метода будут разные как в случае примера с мечником , лучником и волшебником

# Задача № 4 Полиморфизм с наследованием
# 1. Все тоже самое как в случае с Полиморфизмом без наследование , единственное различие здесь присутствует наследование
# трехступенчатой концепций (дед-отец-ребенок)