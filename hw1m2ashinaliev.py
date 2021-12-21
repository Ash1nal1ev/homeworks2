class Animals:
    def _init_(self,species,lifespan,color,habitat,lifestyle,body):
        if isinstance(species,str):
            self.species=species
        else:
            raise ValueError("kind  should be str")
        if isinstance(lifespan,int):
            self.lifespan = lifespan
        else:
            raise ValueError("lifespan should be int")
        if isinstance(color,str):
            self.color = color
        else:
            raise ValueError("coloration should be str")
        if isinstance(habitat,str):
            self.habitat = habitat
        else:
            raise ValueError("habitat should be str")
        if isinstance(lifestyle,str):
            self.lifestyle = lifestyle
        else:
            raise ValueError("lifestyle should be str")
        if isinstance(body,str):
            self.body=body
        else:
            raise ValueError("body should be str")
    def  _str_(self):
        return f"Species: {self.species}\n"\
            f"Lifespan: {self.lifespan} \n"\
            f"Color: {self.color}\n"\
            f"Habitat:{self.habitat}\n"\
            f"Lifestyle:{self.lifestyle}\n"\
            f"Body:{self.body}"
Dog = Animals(species = "dog",lifespan = 10,color = "black",habitat = "with a person",lifestyle = "active",body= "Ноги,уши,хвост,когти")
print(Dog)
class Aquatic_animal(Animals):
    def _init_(self,species,lifespan,color,habitat,lifestyle,body,sceleton):
        super()._init_(species,lifespan,color,habitat,lifestyle,body)
        if isinstance(sceleton,str):
            self.sceleton=sceleton
        else:
            raise ValueError("sceleton should be str")
    def _str_(self):
        return super()._str_()+ f"\nSceleton:{self.sceleton}"
Trout = Aquatic_animal("Trout",2,"white","water","active","хвост,жабры,рот,нос","vertebrate")
print(Trout)
class Birds(Animals):
    def _init_(self,species,lifespan,color,habitat,lifestyle,body,speed):
        super()._init_(species,lifespan,color,habitat,lifestyle,body)
        if isinstance(speed,int):
            self.speed=speed
        else:
            raise ValueError("speed should be int")
    def _str_(self):
        return super()._str_()+ f"\nSpeed:{self.speed}"
Falcon = Birds("Falcon",5,"Brown","Air","active","хвост,клюв,нос,крылья,когти",390)
print(Falcon)
class Snakes(Animals):
    def _init_(self,species,lifespan,color,habitat,lifestyle,body,lenght):
        super()._init_(species,lifespan,color,habitat,lifestyle,body)
        if isinstance(lenght,int):
            self.lenght=lenght
        else:
            raise ValueError("lenght should be int")
    def _str_(self):
        return super()._str_()+ f"\nLenght:{self.lenght}"
Anaconda = Snakes("Anaconda",5,"Black","Tropic","active","хвост,рот,нос",3)
class Zoo_show:
    def _str_(self):
        return f" На сегодня есть 3 вида шоу \n"\
                f"1.Шоу 'Пять мартышек'\n"\
                f"2.Удивительные дельфины\n"\
                f"3.Львы\n"
    def coose(self,x):
        if isinstance(x,int):
            if x == 1:
                return f"Пять мартышек покажут интересные фокусы,а так же они умеют кататься на велосипедах .\nСтоимость билета: 500 сом"
            if x == 2:
                return f"Удивитильные дельфины покажут вам ,что человек и дельфины могут быть отличной командой ,а также танцы с дельфинами! \nСтоимость билета: 600 сом"
            elif x ==3:
                return f"Львы в команде с человеком могут на многое.Львы покажут на что способны их тело!\nСтоимость билета: 700 сом"
            else:
                print("Такого билета нету!")
        else:
            raise ValueError("x should be int")
bilet = Zoo_show()
print(bilet)
print(bilet.coose(3))