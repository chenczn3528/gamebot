from airtest.core.api import connect_device
from time import time
from utils.utils import *
from functions import *

# 连接模拟器
connect_device("Android:///127.0.0.1:5555")

# 需要位于选择账户界面
for i in range(8):

    start_time = time.time()

    if i != 0:
        login() # 从选择账户页面开始
    daily()

    s = input("next")

    end_time = time.time()
    elapsed_minutes = (end_time - start_time) / 60
    print(f"耗时: {elapsed_minutes:.2f} 分钟")