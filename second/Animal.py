"""
1、直接调用return不会打印
2、私有属性不能直接调用，需要调用对应的方法访问
3、复写父类的__init__方法
    重写__init_-方法，继承时不需要将私有属性放在init参数中
    对父类属性使用super()
4、私有的属性和方法不能被子类继承和访问，可通过访问父类的公有方法间接的访问私有方法。（或者使用_类名+私有属性）
5、私有属性和私有方法定义，名称前加__。
6、dir（实例）查看可被调用的属性和方法
7、调用父类的参数
super(Cat, self).__init__(name,colour,age,gender)
        super().__init__(name,colour,age,gender)
8、类名可以直接调用属性，类方法（需要在方法上面写 @classmethod）
9、类内的额每一个方法都需要有self，类外的方法不需要self
10、yaml文档中有中文，需要使用encoding=‘utf-8’。（例子：  with open("./data.yml",encoding='utf-8') as f: ）
11、yaml键与值需要空格

"""
import yaml


class Animal:

    def __init__(self,name,colour,age,gender):
        self.name =name
        self.colour = colour
        self.age = age
        self.gender = gender

    def call(self):
        print("calling")
    def run(self):
        print(f"{self.name}running")


class Cat(Animal):
    def __init__(self,name,colour,age,gender,hair):
        self.hair = '短毛'
        # self.__cat_private ='88捉老鼠'    # 私有属性不用写在__init__传的参数中，只需添加新增的公共属性
        # super(Cat, self).__init__(name,colour,age,gender)
        super().__init__(name,colour,age,gender)
    # def cat_private(self):
    #     return self.__cat_private  #直接return 私有属性
    def Catching_Mice(self):
        # print("ss")
        return f"{self.name}捉到了老鼠"

    def call(self):
        print(f"{self.name}喵喵叫")
        ##私有方法的定义及调用
    # def __cat_private(self):
    #     self.name='老鼠'
    #     print(self.name)
    # def cat_private(self):
    #     self.__cat_private()

class Dog(Animal):
    def __init__(self,name,colour,age,gender,hair):
        self.hair = '长毛'
        super(Dog, self).__init__(name,colour,age,gender)

    def Watches_over(self):
        print(f"{self.name}会看家")
    def call(self):
        print(f"{self.name}汪汪叫")

if __name__ == '__main__':


    cat1=Cat('小花','white','1','female','短毛')
    print(cat1.Catching_Mice())
    # print(f"猫猫的名字是{cat1.name},颜色是{cat1.colour},年龄是{cat1.age}岁,性别是{cat1.gender},毛发是{cat1.hair},{cat1.Catching_Mice()}")
    dog1=Dog('旺财','yellow','9个月','male','长毛')
    dog1.Watches_over()
    # print(f"狗狗的名字是{dog1.name},颜色是{dog1.colour},年龄是{dog1.age},性别是{dog1.gender},毛发是{dog1.hair}")
    # print(cat1.cat_private())
    # cat1.cat_private()
    # print(dir(cat1))
    with open("data.yml", encoding='utf-8') as f:  ###  yaml文档中有中文，需要使用encoding=‘utf-8’
        datas = yaml.safe_load(f)
        data=datas['default']
        print(f"名字是{data['name']},颜色是{data['colour']},年龄是{data['age']},性别是{data['gender']},毛发是{data['hair']}")



