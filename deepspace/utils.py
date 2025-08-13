from airtest.core.api import *
from typing import Tuple, Optional


# ---------------- 图片模板方式 ----------------
def touch_pic(pic: str, sleep_time: float = 2, threshold: float = 0.7):
    """点击图片模板"""
    touch(Template(pic, threshold=threshold))
    sleep(sleep_time)


def swipe_pic(pic1: str, pic2: str, duration: float = 0.5, sleep_time: float = 2, threshold: float = 0.7):
    """滑动，从图片1到图片2"""
    swipe(Template(pic1, threshold=threshold), Template(pic2, threshold=threshold), duration=duration)
    sleep(sleep_time)


def exists_pic(pic: str, sleep_time: float = 2, threshold: float = 0.7) -> bool:
    """判断图片是否存在"""
    result = exists(Template(pic, threshold=threshold))
    sleep(sleep_time)
    return bool(result)


def wait_pic(pic: str, timeout: float = 60, sleep_time: float = 2, threshold: float = 0.7):
    """等待图片出现"""
    wait(Template(pic, threshold=threshold), timeout=timeout)
    sleep(sleep_time)


# ---------------- 固定坐标方式 ----------------
def touch_pos(pos: Tuple[int, int], sleep_time: float = 2):
    """点击固定坐标"""
    touch(pos)
    sleep(sleep_time)


def swipe_pos(pos1: Tuple[int, int], pos2: Tuple[int, int], duration: float = 0.5, sleep_time: float = 2):
    """滑动，从坐标1到坐标2"""
    swipe(pos1, pos2, duration=duration)
    sleep(sleep_time)


def back(sleep_time: float = 2):
    """左上角返回键"""
    touch_pos((55, 105), sleep_time=sleep_time)


def bottom(sleep_time: float = 2):
    """最底下中间"""
    touch_pos((720, 2488), sleep_time=sleep_time)