class Person:
    def __init__ (self,name):
        self.name = name


    def sayhello(self, to):
        print(f"hello {to}, i'm {self.name}")


jong = Person("jongha")
jong.sayhello("minju")
