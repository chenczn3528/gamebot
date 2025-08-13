from deepspace.functions import __detect_color__
from functions import *
from airtest.core.api import connect_device

# 连接模拟器
connect_device("Android:///127.0.0.1:5555")


# # 目前的功能
# login()
# logout()
# get_friend_energy()
# get_energy()
# daily_check()
# explore()



# # 需要位于选择账户界面
# for i in range(4):
#     touch_pos((875, 930))   # 展开用户列表
#     touch_pos((450, 1275), sleep_time=5)  # 点击最下面那个用户
#     touch_pos((545, 1140))  # 点击登陆
#     touch_pos((545, 1140))  # 点击登陆
#
#     login()
#
#     get_friend_energy()
#     explore()
#     daily_check()
#     get_energy()



    # s = input(f"logout? i={i} ")
    # if s.lower() == "y":
    #     logout()