class Employee:
    def __init__(self,name,address,code,salary):
        self.name = name
        self.address = address
        self.code = code
        self.salary = salary

    def __str__(self):
        return f'{self.name},{self.address},{self.code},{self.salary}'
    

hemasai = Employee('Hemasai','3/192,Pallamkurru','PYABC1021',200000)
print(hemasai)