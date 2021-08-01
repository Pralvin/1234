"""
1.写一个面向对象的例子：
    比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
    创建子类【猫】，继承【动物类】
    重写父类的__init__方法，继承父类的属性
    添加一个新的属性，毛发=短毛
    添加一个新的方法， 会捉老鼠，
    重写父类的‘【会叫】的方法，改成【喵喵叫】
    创建子类【狗】，继承【动物类】
    复写父类的__init__方法，继承父类的属性
    添加一个新的属性，毛发=长毛
    添加一个新的方法， 会看家
    复写父类的【会叫】的方法，改成【汪汪叫】
1.在入口函数中创建类的实例
    创建一个猫猫实例
    调用捉老鼠的方法
    打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】
    创建一个狗狗实例
    调用【会看家】的方法
    打印【狗狗的姓名，颜色，年龄，性别，毛发】

"""

class Animal:

    def __init__(self , name , color, age , sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    # 会跑
    def run(self):
        print(f"{self.name},是一个有着一身{self.color}毛毛的{self.sex}孩子，今年{self.age}岁了，它正在欢快的跑~")
    # 会叫
    def call(self):
        print(f"{self.name},是一个有着一身{self.color}毛毛的{self.sex}孩子，今年{self.age}岁了，它正在欢快的叫~")

"""
    创建子类【猫】，继承【动物类】
    重写父类的__init__方法，继承父类的属性
    添加一个新的属性，毛发=短毛
    添加一个新的方法， 会捉老鼠，
    重写父类的‘【会叫】的方法，改成【喵喵叫】
"""
class Cat(Animal):

    def __init__(self , name , color, age , sex ,hair):
        # 新增毛发属性
        self.hair = hair
        # 继承父类的构造函数
        super().__init__(name, color, age, sex)

    # 添加一个新的方法， 会捉老鼠
    def catching_mice(self):
        print(self.name)
        print(self.color)
        print(self.sex)
        print(self.age)
        print(self.hair)
        print(f"{self.name}是一只会捉老鼠的好猫猫,它今天又捉到了一只老鼠")

    # 重写父类的‘【会叫】的方法，改成【喵喵叫】
    def call(self):
        print(f"{self.name},是一个有着一身{self.color}毛毛的{self.sex}孩子，今年{self.age}岁了，它正在欢快的喵喵~喵喵叫")



"""
    创建子类【狗】，继承【动物类】
    复写父类的__init__方法，继承父类的属性
    添加一个新的属性，毛发=长毛
    添加一个新的方法， 会看家
    复写父类的【会叫】的方法，改成【汪汪叫】
"""

class Dog(Animal):
    #     复写构造函数
    def __init__(self, name, color, age, sex):
        # 新增毛发属性
        self.hair = "长毛"
        # 继承父类的构造函数
        super().__init__(name, color, age, sex)

    #     新增会看家的方法
    def care_home(self):
        print(self.name)
        print(self.color)
        print(self.sex)
        print(self.age)
        print(self.hair)
        print(f"{self.name}是一个会看家的好狗狗，它正在看家~")

    # 复写父类的【会叫】的方法，改成【汪汪叫】
    def call(self):
        print(f"{self.name},是一个有着一身{self.color}毛毛的{self.sex}孩子，今年{self.age}岁了，它正在欢快的旺旺叫~")


if __name__ == '__main__':
    print("---------------------父类验证---------------------------")
    animal = Animal("旺财","棕色" , 6 , "男")
    animal.run()
    animal.call()

    print("---------------------猫的子类验证---------------------------")
    # 猫的子类验证
    cat = Cat("包子","银渐色",4,"男","短毛")
    # cat.call()
    cat.catching_mice()
    # cat.run()

    # 狗的子类验证
    print("---------------------狗的子类验证---------------------------")
    dog = Dog("白雪公主" , "黑色" , 2 , "女")
    # dog.call()
    dog.care_home()