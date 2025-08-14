from airtest.core.api import *
from typing import Tuple, Optional


# ---------------- 图片模板方式 ----------------
def touch_pic(pic: str, sleep_time: float = 3, threshold: float = 0.7, log: str = ""):
    """点击图片模板"""
    if log != "":
        print(log)
    print(f"点击图片：{pic}")
    touch(Template(pic, threshold=threshold))
    sleep(sleep_time)


def swipe_pic(pic1: str, pic2: str, duration: float = 0.5, sleep_time: float = 3, threshold: float = 0.7):
    """滑动，从图片1到图片2"""
    swipe(Template(pic1, threshold=threshold), Template(pic2, threshold=threshold), duration=duration)
    sleep(sleep_time)


def exists_pic(pic: str, sleep_time: float = 3, threshold: float = 0.7, log: str = "") -> bool:
    """判断图片是否存在"""
    if log != "":
        print(log)
    print(f"判断图片是否存在：{pic}")
    result = exists(Template(pic, threshold=threshold))
    sleep(sleep_time)
    return bool(result)


def exists_pic_pos(
    pic: str,
    sleep_time: float = 3,
    threshold: float = 0.7,
    log: str = ""
) -> Tuple:
    """查找图片在屏幕中的位置，并返回左上/右下坐标(x1,y1,x2,y2)"""
    if log:
        print(log)
    print(f"判断图片是否存在：{pic}")

    result = exists(Template(pic, threshold=threshold))
    print(result)
    sleep(sleep_time)

    if result:
        return result
    return None


def wait_pic(pic: str, timeout: float = 60, sleep_time: float = 3, threshold: float = 0.7, log: str = ""):
    """等待图片出现"""
    if log != "":
        print(log)
    print(f"寻找图片：{pic}")
    wait(Template(pic, threshold=threshold), timeout=timeout)
    sleep(sleep_time)


# ---------------- 固定坐标方式 ----------------
def touch_pos(pos: Tuple[int, int], sleep_time: float = 3, log: str = ""):
    """点击固定坐标"""
    if log != "":
        print(log)
    touch(pos)
    sleep(sleep_time)


def swipe_pos(pos1: Tuple[int, int], pos2: Tuple[int, int], duration: float = 0.5, sleep_time: float = 3, log: str = ""):
    """滑动，从坐标1到坐标2"""
    if log != "":
        print(log)
    swipe(pos1, pos2, duration=duration)
    sleep(sleep_time)


def back(sleep_time: float = 3):
    """左上角返回键"""
    touch_pos((55, 105), sleep_time=sleep_time)