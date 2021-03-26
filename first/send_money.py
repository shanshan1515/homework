import money
import is_send

def send_money():
    is_send.is_send = True

    if is_send.is_send == True:
        money.saved_money = money.saved_money + 1000
    else:
        print("还没发工资")



