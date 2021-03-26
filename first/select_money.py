import money
import is_send


def select_money():
    if is_send.is_send == True:
        print("发工资啦")
        print("存款为：", money.saved_money, "元")
    else:
        print("等待中...当前存款为：", money.saved_money)
