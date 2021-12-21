class Bed:
    def __init__(self, brand, weight, material, color, cost):
        if isinstance(brand, str):
            self.brand = brand
        else:
            raise ValueError('Brand should be string')
        if isinstance(weight, int):
            self.weight = weight
        else:
            raise ValueError('Weight should be int')
        if isinstance(material, str):
            self.material = material
        else:
            raise ValueError('Material should be str')
        if isinstance(color, str):
            self.color = color
        else:
            raise ValueError('Color should be str')
        if isinstance(cost, int):
            self.cost = cost
        else:
            raise ValueError('Cost should be int')


    def __str__(self):
        return f'Brand: {self.brand}\n' \
               f'Max weight: {self.weight}\n' \
               f'Beds material: {self.material}\n' \
               f'color: {self.color}\n' \
               f'Cost: {self.cost}$'
class Transformer(Bed):
    def __init__(self, brand, weight, material, color, cost):
        super().__init__(brand, weight, material, color, cost)

    def comfortable(self, something):
        return f'This bed is {something}'

    def __str__(self):
        return super(Transformer, self).__str__()

transformerbed_1 = Transformer(brand = 'Lavisa',weight=200, material = 'ironwood',
            color='red',cost = 70000)

print(transformerbed_1)
print(transformerbed_1.comfortable('can transform into sofa'))



class BunkBed(Bed):
    def __init__(self, brand, weight, material, color, cost):
        super().__init__(brand, weight, material, color, cost)

    def fit(self, something):
        return f'This bed is {something}'

    def __str__(self):
        return super(BunkBed, self).__str__()

bunkbed_1 = BunkBed(brand = 'Cosilia',weight=150, material = 'wood',
            color='black',cost = 21000)

print(bunkbed_1)
print(bunkbed_1.fit('roomy'))

class Hybrid(Transformer, BunkBed):
    def __init__(self, brand, weight, material, color, cost):
        super().__init__(brand, weight, material, color, cost)

    def __str__(self):
        return super(Hybrid, self).__str__()

hybrid_1 = Hybrid(brand = 'Luisianna',weight=360, material = 'blacksteel',
            color='beige',cost = 90000)

print(hybrid_1)
print(hybrid_1.comfortable('can transform into sofa'))
print(hybrid_1.fit('roomy'))
