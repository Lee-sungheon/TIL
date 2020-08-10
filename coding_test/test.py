class Person:

    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting
        self.greet()

    def greet(self):
        print(self.greeting)

    def __del__(self):
        print('bye')

seunghan = Person('승한', '안녕')
seunghan.greeting
seunghan.__init__('도영', '젤리')
doyung = seunghan
seunghan.__del__()
del seunghan
doyung.greet()