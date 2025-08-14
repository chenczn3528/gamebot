from utils.utils import *
import numpy as np
from PIL import Image
import cv2

templates = {}
for i in range(10):
    img = Image.open(f"images/template/{i}.png").convert("L")  # 灰度
    templates[str(i)] = np.array(img)


def ocr_number(region, threshold=0.9):
    """
    从 Airtest 截图区域识别数字
    :param region: (x1, y1, x2, y2) 截图区域
    :param templates: 字典，键为数字字符，值为对应灰度模板 np.array
    :param threshold: 匹配阈值，默认0.8
    :return: 识别出的数字字符串
    """
    # 获取屏幕截图
    screenshot = device().snapshot()  # numpy.ndarray
    x1, y1, x2, y2 = region
    crop_img = screenshot[y1:y2, x1:x2]

    # 转灰度
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

    result_digits = []

    # 遍历模板，匹配每个数字
    for digit, tmpl in templates.items():
        w, h = tmpl.shape[::-1]
        res = cv2.matchTemplate(gray, tmpl, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):  # (x, y) 坐标
            result_digits.append((pt[0], digit))  # 用 x 坐标记录顺序

    # 按 x 坐标排序，得到数字顺序
    # result_digits.sort(key=lambda x: x[0])
    # digits_str = "".join([d[1] for d in result_digits])
    result_digits = nms_match_points(result_digits, min_distance=5)
    digits_str = "".join([d[1] for d in result_digits])

    return digits_str

def nms_match_points(points, min_distance=5):
    """
    非极大值抑制，去掉靠得太近的重复匹配
    points: list of (x, digit)
    min_distance: 相邻匹配最小间距
    """
    if not points:
        return []
    points = sorted(points, key=lambda x: x[0])
    filtered = [points[0]]
    for pt in points[1:]:
        if pt[0] - filtered[-1][0] >= min_distance:
            filtered.append(pt)
    return filtered


def bottom():
    touch_pos((965, 1010), sleep_time=2)

def back_bw():
    touch_pos((95, 75), sleep_time=2)


def return_home():
    """从任意有返回键的页面回到主页面（不管主页面1还是2）"""
    while True:
        if exists_pic("images/daily/go_home.png", log="判断是否有直达主界面的按钮"):
            touch_pos((210, 90), sleep_time=2, log="返回主界面")
            break
        else:
            back_bw()
        if exists_pic("images/daily/home.png", log="判断是否在主界面"):
            break


def to_page1():
    """从主页面回到主页面1（不管原先的主页面是哪个）"""
    if exists_pic("images/daily/daily.png", log="判断是不是在主界面1"):
        return
    else:
        touch_pos((60, 510), log="跳转到主界面1")


def to_page2():
    """从主页面回到主页面1（不管原先的主页面是哪个）"""
    if exists_pic("images/daily/daily.png", log="判断是不是在主界面1"):
        touch_pos((1800, 510), log="跳转到主界面2")
    else:
        return


def login():
    """登陆，从选择账户页面开始，到进入游戏主界面"""
    touch_pos((1270, 500), log="展开用户列表")
    swipe_pos((1220, 810), (1220, 520), duration=0.05, log="下滑到最下面")
    touch_pos((955, 690), sleep_time=1, log="点击最下面那个用户")
    touch_pos((965, 655), sleep_time=1, log="点击登陆")
    touch_pos((990, 835), sleep_time=1, log="点击进入游戏")
    touch_pos((990, 835), sleep_time=10, log="点击进入游戏")



def save_region(region, save_path="crop.png"):
    """
    保存 Airtest 截图裁剪区域到本地
    region: (x1, y1, x2, y2)
    save_path: 保存路径
    """
    img = device().snapshot()  # 截图，numpy.ndarray

    # 裁剪
    x1, y1, x2, y2 = region
    crop_np = img[y1:y2, x1:x2]

    # 转成 PIL Image 保存
    crop_img = Image.fromarray(crop_np)
    crop_img.save(save_path)
    print(f"区域截图已保存到: {save_path}")


def activity():
    """每日三次城市活动"""
    region1 = (475, 790, 635, 855)
    region2 = (725, 795, 885, 860)
    region3 = (975, 800, 1135, 865)
    region4 = (1225, 805, 1385, 870)
    region5 = (1475, 810, 1635, 875)
    save_region(region1, save_path="images/num/region1.png")
    save_region(region2, save_path="images/num/region2.png")
    save_region(region3, save_path="images/num/region3.png")
    save_region(region4, save_path="images/num/region4.png")
    save_region(region5, save_path="images/num/region5.png")
    print(ocr_number(region1))
    print(ocr_number(region2))
    print(ocr_number(region3))
    print(ocr_number(region4))
    print(ocr_number(region5))



def daily():
    # if exists_pic("images/daily/reward.png", threshold=0.9, log="每日签到奖励"):
    #     print("matched")
    #     bottom()
    #     return_home()
    activity()