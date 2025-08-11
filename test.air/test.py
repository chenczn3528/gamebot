# -*- encoding=utf8 -*-
__author__ = "chen"

from airtest.core.api import *
from PIL import Image
import numpy as np

auto_setup(__file__)


# 左上角返回按钮
def back():
    touch((86, 140))
    sleep(1)
    
# 最底下中间
def bottom():
    touch((720, 2488))
    sleep(1)
    
    
def touch_action(position):
    touch(position)
    sleep(1)
    
    
    
def detect_color(region_coords, target_color, tag="", tolerance=30):
    """
    判断屏幕指定区域是否包含指定颜色

    :param region_coords: (x1, y1, x2, y2) 坐标元组，检测区域
    :param target_color: (R, G, B) 目标颜色元组
    :param tolerance: 颜色容差，默认30
    :return: bool，是否检测到颜色
    """
    # 截图，返回 numpy BGR 格式
    screen_np = device().snapshot()

    # 转成 RGB 格式 PIL 图像
    screen_rgb = screen_np[..., ::-1]
    screen_img = Image.fromarray(screen_rgb)

    # 裁剪区域
    region = screen_img.crop(region_coords)

    pixels = region.load()
    width, height = region.size

    def is_similar_color(c1, c2, tol):
        return all(abs(a - b) <= tol for a, b in zip(c1, c2))

    for x in range(width):
        for y in range(height):
            if is_similar_color(pixels[x, y][:3], target_color, tolerance):
                print(f"√ 在区域内找到接近 {tag} 的像素点")
                return True

    print(f"区域内未找到接近 {tag} 的像素点")
    return False


# ======= 进入游戏 ========
def enter_game():
    # 点击关闭系统公告（如有）
    touch_action((147, 2032))

    # 点击进入游戏
    touch_action((745, 2073))

    wait(Template(r"tpl1754885318678.png", record_pos=(0.428, 0.293), resolution=(1440, 2560)), timeout=60)



# ======= 体力 ========
def friend_energy():
    # 点击体力
    touch_action((83, 326))

    # 点击领取，点两次
    touch_action((1011, 2339))
    touch_action((1011, 2339))

    back()


# ======= 商城 ========
def store():
    # 点击商城
    touch_action((1331, 1900))

    # 点击礼包
    touch_action((522, 444))

    # 下滑
    swipe((1351, 2121), (1351,660), duration=0.5)
    sleep(1)

    ## 点击购买礼包
    # 每周礼包
    pos = exists(Template(r"tpl1754888171639.png", record_pos=(-0.194, 0.376), resolution=(1440, 2560), threshold=0.9))
    if pos:
        touch_action(pos)
        touch_action((716, 1833))
        bottom()

    # 每日礼包
    pos = exists(Template(r"tpl1754888258837.png", record_pos=(0.19, 0.373), resolution=(1440, 2560), threshold=0.9))
    if pos:
        touch_action(pos)
        touch_action((716, 1833))
        bottom()
    ## ......

    # 点击兑换
    touch_action((1161, 428))

    # 点击快乐小铺
    touch_action((588,538))

    ## 点击购买许愿券、磁石和金币
    # 许愿券
    pos = exists(Template(r"tpl1754888555584.png", record_pos=(-0.193, -0.251), resolution=(1440, 2560), threshold=0.9))
    if pos:
        touch_action(pos)
        touch_action((738, 1552))
        bottom()

    # 磁石
    pos = exists(Template(r"tpl1754888648319.png", record_pos=(0.19, -0.249), resolution=(1440, 2560), threshold=0.9))
    if pos:
        touch_action(pos)
        touch_action((1157, 1408))
        touch_action((707, 1674))
        bottom()

    # 金币
    pos = exists(Template(r"tpl1754888693583.png", record_pos=(-0.192, 0.001), resolution=(1440, 2560), threshold=0.9))
    if pos:
        touch_action(pos)
        touch_action((738, 1552))
        bottom()
    ## ......

    back()

# ======= 探测 ========
def explore():
    # 点击许愿
    touch_action((1348, 1702))

    # 点击星间探测
    touch_action((1326, 281))

    # 若探测完成，则点击收取
    if exists(Template(r"tpl1754889131121.png", record_pos=(0.003, 0.451), resolution=(1440, 2560))):
        pass
    elif exists(Template(r"tpl1754885959066.png", record_pos=(-0.004, 0.445), resolution=(1440, 2560))):
        touch_action((751,2171))

        # 点击两次
        bottom()
        bottom()

        # 开始探测
        touch_action((481, 2121))
        touch_action((967, 1323))

    else:
        # 点进来是金磁铁
        if exists(Template(r"tpl1754886644765.png", record_pos=(0.197, 0.518), resolution=(1440, 2560))):
            # 回到蓝磁铁
            touch_action((441, 2056))
            # 开始探测
            touch_action((481, 2121))
            touch_action((967, 1323))
    back()
    back()



# ======= 日程 ========
def daily():
    # 进入日程
    touch_action((1330, 1308))

    # 点击补给
    touch_action((1189, 2419))

    # 点击领取补给
    pos = exists(Template(r"tpl1754887071971.png", record_pos=(0.217, 0.287), resolution=(1440, 2560)))
    if pos:
        touch_action(pos)
        bottom()

    # 点击签到
    touch_action((913, 2422))

    # 点击领取签到
    pos = exists(Template(r"tpl1754887218980.png", record_pos=(-0.249, -0.107), resolution=(1440, 2560), threshold=0.5))
    if pos:
        touch_action(pos)
        bottom()

    # 点击任务
    touch_action((322, 2409))

    # 点击一键领取，点两次，收星级奖励
    touch_action((1114, 2262))
    touch_action((1114, 2262))
    bottom()

    back()

# ======= 作战 ========
def fight():
    
    right_region = (569, 1896, 754, 1946)
    
    # 点击作战
    touch_action((679, 2378))

    # 点击零点追踪
    touch_action((525, 629))

    # 点击哈特
    touch_action((441, 870))

    # 点击关卡，从高往低
    fight_pos_list = [(920,726), (1132,973), (982,1251), (707,1486), (381,1289), 
                      (679,1048), (353,801), (638,591), (441,413)]
    for i in range(len(fight_pos_list)):
        # 点进关卡（或没点进）
        touch(fight_pos_list[i])
        sleep(1)
        # 检测是否有通关
        if detect_color(region_coords=right_region, target_color=(255,231,146), tag="黄色"): 
            while True:
                isRed = detect_color(region_coords=right_region, target_color=(229,124,73), tag="红色")
                isYellow = detect_color(region_coords=right_region, target_color=(255,231,146), tag="黄色")
                # 没有黄的，说明剩16以下，只点一次自动追击1
                if not isYellow:
                    touch_action((376,1927))
                    touch_action((822, 1875))
                    bottom()
                    break
                # 有黄的，没有红的，可以继续点
                if not isRed:
                    # 消耗体力
                    touch_action((656, 1926))
                    # 快速跳过
                    touch_action((822, 1875))
                    touch_action((822, 1875))
                # 有黄的，有红的
                else:
                    bottom()
                    break
            break
        # 未通关，点前一个关卡
        else:
            bottom()
            continue
    back()
    back()
    back()
    
    
    
    
# ======= 每周任务 ========
def photos():
    # 点击约会
    touch_action((472,2371))
    
    # 点击拍照
    touch_action((412,1729))
    
    # 点击第一个人拍照
    touch_action((479,500))
    sleep(1)
    
    # 点击大头贴
    touch_action((954,789))
    
    # 进入大头贴，点击下一步
    wait(Template(r"tpl1754895476385.png", record_pos=(0.015, 0.637), resolution=(1440, 2560)), timeout=60)
    touch_action((759, 2195))
    # 点击准备好了
    touch_action((1012,2195))
    sleep(1)
    # 点击拍照
    touch_action((712,1363))
    sleep(1)
    # 退出大头贴，确定
    back()
    touch_action((1063,1316))
    
    # 回到拍照类型页
    wait(Template(r"tpl1754895677941.png", record_pos=(0.151, -0.295), resolution=(1440, 2560)), timeout=60)
    # 点击写真
    touch_action((806,1967))
    wait(Template(r"tpl1754900900894.png", record_pos=(-0.412, -0.794), resolution=(1440, 2560)))

    # 点击拍照
    touch_action((1318,1507))
    sleep(1)
    
    back()
    
    # 回到拍照类型页
    wait(Template(r"tpl1754895677941.png", record_pos=(0.151, -0.295), resolution=(1440, 2560)), timeout=60)
    back()
    back()



def miaomiao():
    
    character_pos_list = [(479,500), (873,940), (443,1370), (965,1750), (493,2085)]
    
    wait(Template(r"tpl1754901195392.png", record_pos=(-0.172, 0.766), resolution=(1440, 2560)))

    
    # 点击约会
    touch_action((472,2371))
    
    # 点击快乐出游
    touch_action((422, 1259))
    for i in range(len(character_pos_list)):
        touch_action((character_pos_list[i]))
        sleep(1)
        # 娃娃机
        touch_action((934, 808))
        
        for i in range(3):
            # 点击出发
            touch_action((779, 2241))
            if exists(Template(r"tpl1754898232463.png", record_pos=(0.034, -0.187), resolution=(1440, 2560))):
                bottom()
                break
            else:
                
                # 进入页面，等返回按钮
                wait(Template(r"tpl1754897467789.png", record_pos=(-0.444, -0.792), resolution=(1440, 2560)), timeout=60)
                back()
                wait(Template(r"tpl1754898164580.png", record_pos=(0.169, 0.029), resolution=(1440, 2560)))

                # 确定
                touch_action((952,1320))
                wait(Template(r"tpl1754897467789.png", record_pos=(-0.444, -0.792), resolution=(1440, 2560)), timeout=60)
                back()
                # 等出现出发按钮并点击
                wait(Template(r"tpl1754897562193.png", record_pos=(0.019, 0.69), resolution=(1440, 2560)))
        back()
        # 喵喵牌
        touch_action((458,1158))
        
        for i in range(3):
            # 点击出发
            touch_action((1125,2161))
            if exists(Template(r"tpl1754898232463.png", record_pos=(0.034, -0.187), resolution=(1440, 2560))):
                bottom()
                break
            wait(Template(r"tpl1754897744749.png", record_pos=(-0.404, -0.792), resolution=(1440, 2560)))
            back()
            # 确定
            touch_action((952,1320))
            back()
            # 等出现出发按钮并点击
            wait(Template(r"tpl1754897796148.png", record_pos=(0.267, 0.615), resolution=(1440, 2560)))
        back()
        touch_action((1392,336))
    back()
    back()
    back()
        
        
        
def workflow():
    enter_game()    # 进入游戏
    friend_energy() # 领取好友体力
    store()         # 买免费礼包、兑换商店
    explore()       # 星际探测
    daily()         # 每日任务
    fight()         # 作战
    
    
def week():
    photos()        # 拍照
    miaomiao()      # 抓娃娃、喵喵牌
    
workflow()

week()

