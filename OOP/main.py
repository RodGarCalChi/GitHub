class Dog:
    def __init__(self,name,breed):
        self.name=name
    def bark(self):
        print("Whoof whoof")
    def get_Name(self):
        return self.name


dog1=Dog("Bruce","Scottish Terrier")
dog1.name="Auri"
dog1.bark()
print(dog1.get_Name())

dog2=Dog("Lucas","Pastor Aleman")
dog2.name="Maffi"
dog2.bark()
print(dog2.get_Name())
