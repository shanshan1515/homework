
class calculator():
    def check_int_float(self, a, b):
        if isinstance(a, int) or isinstance(a, float):
            if isinstance(b, int) or isinstance(b, float):
                return True
            else:
                print("类型错误")
                return False
        else:
            print("类型错误")
            return False

    def add(self,a,b):
        if(self.check_int_float(a,b)):
            return round(a+b,2)
        else:
            return 0
        ###  方法一
        # if isinstance(a, int) or isinstance(a, float):
        #     if isinstance(b, int) or isinstance(b, float):
        #         # print('打印：', a + b)
        #        return a+b
        #     else:
        #         print("类型错误")
        # else:
        #     print("类型错误")
    ###  方法二：
        # try:
        #     return round(a + b,2)
        # except Exception as e:
        #     print("发生错误",e)
        #     # return 0


    def divsion(self,a,b):
        if(self.check_int_float(a,b)):
            if b!=0:
                return round(a/b,2)
            else:
                print("除数不能为零")
                return 0
        else:
            return 0
        ###   方法一：
        # if isinstance(a, int) or isinstance(a, float):
        #     if isinstance(b, int) or isinstance(b, float):
        #         if b!=0:
        #             # print('打印：', a / b)
        #             return a / b
        #         else:
        #             print("除数不能为0")
        #     else:
        #         print("类型错误")
        # else:
        #     print("类型错误")
####   方法二：
        # try:
        #     return round(a/b, 2)
        # except Exception as e:
        #     print("发生错误", e)
        #     # return 0





