class animal:
    def __init__(self,name,color,age,gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender
    def call(self,voice):
        print("voice")
    def run(self):
        print("can run")

class cat(animal):
    def __init__(self,name,color,age,gender,):
        self.hair ="short hair"
        super().__init__(name,color,age,gender)
    def catch_rat(self):
        print("can catch rat")
    def call(self,voice):
        print("喵喵叫")

class dog(animal):
    def __init__(self,name,color,age,gender,):
        self.hair ="long hair"
        super().__init__(name,color,age,gender)
    def caretaker(selfL):
        print("can watch home")
    def call(self,voice):
        print("汪汪叫")

if __name__ == '__main__':
    maoamo = cat("tom","red",18,"male")
    result = maoamo.catch_rat()
    res = maoamo.run()
    
