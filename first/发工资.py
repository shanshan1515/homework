####
# 原有存款 1000元， 发工资之后存款变为2000元
# 定义模块
# 1、money.py saved_money = 1000
# 2、定义发工资模块 send_money，用来增加收入计算
# 3、定义工资查询模块 select_money，用来展示工资数额
# 4、定义一个start.py ，启动文件展示最终存款金额
####
saved_money = 1000
def send_money():
    global saved_money
    saved_money= saved_money+1000
    print("发工资啦！")
def select_money():
    print("本月工资：",saved_money,"元")

if __name__ == '__main__':
    send_money()
    select_money()
