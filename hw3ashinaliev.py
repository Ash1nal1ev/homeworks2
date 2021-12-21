class Person():
    def __init__(self, name, work, address, age, hobby):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("name should be str")
        if isinstance(work, str):
            self.work = work
        else:
            raise ValueError("work should be str")
        if isinstance(address, str):
            self.address = address
        else:
            raise ValueError("address should be str")
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError("age should be str")
        if isinstance(hobby, str):
            self.hobby = hobby
        else:
            raise ValueError("hobby should be str")
    def hi(self):
        return f'Hi my name is {self.name}'
    def working(self):
        return f'My work is {self.work}'
    def __str__(self):
        return f'Name:{self.name}\n'\
        f'Work:{self.work}\n'\
        f'Address:{self.address}\n'\
        f'Age:{self.age}\n'\
        f'Hobby:{self.hobby}'
Dentist = Person(name="Kesha",work="Dentist",address="Shopokova 145", age=23,hobby="Regbi")
print(Dentist)
print(Dentist.hi())
print(Dentist.working())
class Driver(Person):
    def _init_(self,name,work,address,age,hobby):
        super()._init_(name,work,address,age,hobby)
    def car(self,car):
        return f'I have a {car} '
    def Lexus(self,cost):
        return f'My car is standing:{cost}$'
    def _str_(self):
        return super(Driver,self)._str_()
driver1= Driver(name="Lesha",work="Driver",address="Isanova 205", age=33,hobby="Read books")
print(driver1)
print(driver1.car("Lexus 475"))
print(driver1.Lexus(10000))
class Businessmen(Person):
    def _init_(self,name,work,address,age,hobby):
        super()._init_(name,work,address,age,hobby)
    def account(self,account):
        return f'In my account {account}$ '
    def Golf(self):
        return f'We play in {self.hobby} in USE'
    def _str_(self):
        return super(Businessmen,self)._str_()
Businessmen1= Businessmen(name="Erik",work="Businessmen",address="Chuy 156", age=44,hobby="Golf")
print(Businessmen1)
print(Businessmen1.account(100000))
print(Businessmen1.Golf())
class Proger(Driver,Businessmen):
    def _init_(self,name,work,address,age,hobby):
        super()._init_(name,work,address,age,hobby)
    def salary(self,salary):
        return f'My salary is {salary}$ '
    def experience(self,experience):
        return f'My work experience {experience} old'
    def _str_(self):
        return super(Proger,self)._str_()
Proger1= Proger(name="Serik",work="Proger",address="Jibek 156", age=27,hobby="Football")
print(Proger1)
print(Proger1.salary(4000))
print(Proger1.experience(5))
class Laptop:
    def __init__(self,name,cost,color,memory,ram,camera):
        if isinstance(name,str):
            self.name = name
        else:
            raise ValueError("name should be str")
        if isinstance(color,str):
            self.color = color
        else:
            raise ValueError("color should be str")
        if isinstance(cost,int):
            self.cost = cost
        else:
            raise ValueError("cost should be int")
        if isinstance(memory,int):
            self.memory = memory
        else:
            raise ValueError("memory should be int")
        if isinstance(ram,int):
            self.ram = ram
        else:
            raise ValueError("ram should be int")
        if isinstance(camera,bool):
            self.camera = camera
        else:
            raise ValueError("camera should be bool")
    def name(self,x):
        return f'Manufacturer {self.name} {x} '
    def _camera(self):
        return f'The {self.name} has a camera'
    def __str__(self):
        return f'Name:{self.name}\n'\
        f'Cost:{self.cost}$\n'\
        f'Color:{self.color}\n'\
        f'Memory:{self.memory}\n'\
        f'Ram:{self.ram}\n'\
        f'Camera:{self.camera}\n'
Laptop1 = Laptop(name="Acer",cost=700,color="Black",memory=400,ram=16,camera=True)
print(Laptop1)
class Macbook(Laptop):
    def _init_(self,name,cost,color,memory,ram,camera):
        super()._init_(name,cost,color,memory,ram,camera)
    def cost(self):
        return f'{self.name} very expensive '
    def apple(self):
        return f'Apple cares about its customers'
    def _str_(self):
        return super(Macbook,self)._str_()
Macbook1=Macbook(name="Macbook Air 1",cost=2000,color="Grey",memory=500,ram=16,camera=True)
print(Macbook1)
class Asus(Laptop):
    def _init_(self,name,cost,color,memory,ram,camera):
        super()._init_(name,cost,color,memory,ram,camera)
    def asus(self):
        return f'Asus laptops are little known but they do it with high quality'
    def _asus(self):
        return f'Asus has a beautiful design'
    def _str_(self):
        return super(Asus,self)._str_()
Asus1=Asus(name="Asus",cost=1000,color="Black",memory=800,ram=16,camera=True)
print(Asus1)
class Hp(Laptop):
    def _init_(self,name,cost,color,memory,ram,camera):
        super()._init_(name,cost,color,memory,ram,camera)
    def hp(self):
        return f' Hp company - supplier of hardware and software for organizations and consumers'
    def _asus(self):
        return f'HP founder Hewlett-Packard'
    def _str_(self):
        return super(Hp,self)._str_()
Hp1=Hp(name="Hp",cost=700,color="White",memory=800,ram=36,camera=True)
print(Hp1)
class Kino:
    def __init__(self,bill):
        if isinstance(bill,int):
            self.bill = bill
        else:
            raise ValueError("Bill should be int")
    def __str__(self):
        return f'На сегодня есть фильмы\n1:Золушка-250сом\n2:Django-300сом\n3:Lion-300сом\nВыберите номер билета'
    def _eq_(self,x):
        if 1==x :
            return f' \nПодойдите к кассе для оплаты\nНа счету осталось {self.bill-250}сом'
        if 2==x:
            return f'Подойдите к кассе для оплаты\nНа счету осталось {self.bill-300}сом'
        if 3==x :
            return f'Подойдите к кассе для оплаты\nНа счету осталось {self.bill-300}сом '
        else:
            return f'Выберите правильный номер билета!'
Kino1 = Kino(500)
print(Kino1)
print(Kino1._eq_(2))
class Starbucks:
    def __init__(self, money):
        self.money = money
    def _it_(self, other):
        if isinstance(other, str):
            if len(other) < 5:
                return other
            else:
                return other[0:5]
        else:
            raise ValueError("Name should be str")
name = Starbucks(1000)
print(name._it_("Дастан"))