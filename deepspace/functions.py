from utils import *
from PIL import Image

red = (229, 124, 73)
yellow = (255, 231, 146)


def login():
    """登陆，点击进入游戏的页面 -> 主界面"""
    wait_pic("images/login/region.png")  # 等待显示进入游戏的界面
    touch_pos((550, 1550))  # 点击进入游戏
    wait_pic("images/login/main.png")  # 确认目前在主界面


def logout():
    """退出，主界面 -> 选择用户界面"""
    wait_pic("images/login/main.png")  # 确认目前在主界面
    touch_pos((127, 115))  # 点击用户等级
    wait_pic("images/login/user.png")  # 确认目前在用户界面
    touch_pos((920, 1810))  # 点击设置按钮
    ## 这里的两行，按理来说不需要等待
    touch_pos((250, 1775))  # 点击退出账户
    touch_pos((740, 1000))  # 确认退出账户
    wait_pic("images/login/privacy.png")  # 等待回到同意协议界面
    touch_pos((730, 1440))  # 同意协议
    wait_pic("images/login/logo.png")  # 等待出现选择账户界面


def get_friend_energy():
    """领取好友体力"""
    wait_pic("images/login/main.png")  # 确认目前在主界面
    touch_pos((65, 245))  # 点击好友
    if exists_pic("images/daily/friend_energy.png"):  # 领过了
        back()
    else:  # 没领过
        touch_pos((755, 1745))


def get_energy():
    """领取早晚体力"""
    wait_pic("images/login/main.png")  # 确认目前在主界面
    touch_pos((1000, 985))  # 点击日程
    touch_pos((880, 1810))  # 点击补给

    if exists_pic("images/daily/day_night_energy.png"):
        touch_pic("images/daily/day_night_energy.png")  # 点击体力
    touch_pos((925, 1535))  # 点击跳过显示领取多少体力
    back()


def daily_check():
    """领取每日签到奖励"""
    wait_pic("images/login/main.png")  # 确认目前在主界面
    touch_pos((1000, 985))  # 点击日程
    touch_pos((660, 1810))  # 点击签到
    if exists_pic("images/daily/daily_check.png"):
        touch_pic("images/daily/daily_check.png")
        bottom()
        back()


def explore():
    """星际探测"""
    wait_pic("images/login/main.png")  # 确认目前在主界面
    touch_pos((1005, 1275))  # 点击许愿
    touch_pos((995, 205))  # 点击星际探测
    if exists_pic("images/explore/exploring.png"):  # 正在探测
        back(2)
        back(2)
    elif exists_pic("images/explore/finish.png"):  # 探测完成
        touch_pos((540, 1635), sleep_time=5)  # 点击收取
        bottom(5)
        bottom(5)  # 防止有整卡
        touch_pos((360, 1605))  # 点击开始探测
        touch_pos((740, 995))  # 点击确定
        back(2)
        back(2)
    else:  # 在金砂页面
        touch_pos((330, 1545))  # 回到银砂
        touch_pos((360, 1605))  # 点击开始探测
        touch_pos((740, 995))  # 点击确定
        back(2)
        back(2)


def task(first_time: bool = True):
    """每日任务"""
    wait_pic("images/login/main.png")  # 确认目前在主界面
    get_friend_energy() # 领好友体力
    get_energy()    # 领早晚体力
    daily_check()   # 每日签到
    explore()   # 星际探测
    use_energy(first_time)
    # 商城购买，主界面互动，收每日任务奖励


def use_energy(first_time: bool = True):
    """刷材料的规划，需要收藏两张卡，一张用来升级一次卡面，另一张用来刷完体力，也可以都是第一张，第二张主要是升级不了的话备选"""
    isUpgrade = True
    wait_pic("images/login/main.png")  # 确认目前在主界面
    if first_time:  # 第一次收体力，需要完成日常任务-升级一次
        touch_pos((530, 1785), sleep_time=5)  # 点击作战
        touch_pos((390, 490), sleep_time=10)    # 点击零点追踪
        touch_pos((330, 660), sleep_time=5) # 点击哈特
        __material__(multiple=False)    # 刷一次瓶子，完成后回到主界面
    touch_pos((680, 1785), sleep_time=5)    # 点击思念
    touch_pos((280, 700), sleep_time=10)    # 点击第一张卡
    if not exists_pic("images/fight/show_info.png"): # 如果界面不小心被点掉了，只剩图
        bottom(3)
    touch_pos((285, 1700), sleep_time=5)    # 点击第一个圈
    if exists_pic("images/fight/upgrade.png"):  # 是升级，回作战界面
        isUpgrade = True
        back(5)
        back(5)
        back(5) # 回到主界面
        touch_pos((530, 1785), sleep_time=5)  # 点击作战
        touch_pos((390, 490), sleep_time=10)  # 点击零点追踪
        touch_pos((330, 660), sleep_time=5)  # 点击哈特
        __material__(multiple=True)  # 刷瓶子
    else:   # 是突破，需要先刷材料，再到第二张卡去升级
        isUpgrade = False
        touch_pos((200, 1750), sleep_time=5)  # 点击最低等级材料
        touch_pic("images/fight/go.png")    # 跳转到对应材料
        __material__(multiple=True)     # 刷材料
    # 升级一下
    wait_pic("images/login/main.png")  # 确认目前在主界面
    touch_pos((680, 1785), sleep_time=5)  # 点击思念
    if isUpgrade:
        touch_pos((280, 700), sleep_time=10)  # 点击第一张卡
    else:
        touch_pos((550, 700), sleep_time=5) # 点击第二张卡
    if not exists_pic("images/fight/show_info.png"): # 如果界面不小心被点掉了，只剩图
        bottom(3)
    touch_pos((285, 1700), sleep_time=5)    # 点击第一个圈
    touch_pos((840, 1765), sleep_time=5)    # 点击提升一级
    touch_pos((200, 1750), sleep_time=5)    # 升级最小单位瓶子


def __material__(multiple: bool = True):
    """刷材料的逻辑，multiple为true指刷十次，false指刷一次，从显示等级的页面开始运行，刷什么材料要在调用之前写好"""
    material_list = [(695, 535), (870, 735), (745, 930), (530, 1115), (310, 975), (515, 790),
                     (260, 600), (475, 450), (345, 315)]
    region1 = (210, 1420, 370, 1470)  # 自动追击一次
    region2 = (420, 1420, 580, 1470)  # 自动追击十次
    for i in range(len(material_list)):
        touch_pos(material_list[i])  # 点击等级，接下来判断这关有没有打过
        if not exists_pic("images/fight/success.png"):  # 判断是不是锁着
            continue
        elif exists_pic("images/fight/lock.png"):  # 没锁，但是没通关
            bottom(3)
            continue
        else:  # 能刷材料
            if __detect_color__(region1, red, "红色"):  # 自动追击一次是红的，说明没体力
                bottom(3)
                back(3)
                back(3)
                back(3)  # 回到主界面
            else:
                if not multiple:  # 只想刷一次，用在豆佬哈特每日任务上
                    touch_pos((290, 1445), sleep_time=5)  # 追击一次
                    bottom(3)   # 关掉追击结果
                    bottom(3)
                    back(3)
                    back(3)
                    back(3)  # 回到主界面
                else:   # 追击多次
                    while True:
                        if not __detect_color__(region1, red, "红色"):    # 自动追击一次没有红的，说明有体力，体力>=8
                            if __detect_color__(region2, yellow, "黄色"): # 体力>=16
                                touch_pos((510, 1445), sleep_time=15)
                                bottom(3)  # 关掉追击结果
                            else:   # 自动追击十次那里是黑的，体力<16，只能追击一次
                                touch_pos((290, 1445), sleep_time=5)  # 追击一次
                                bottom(3)  # 关掉追击结果
                        else:
                            bottom(3)
                            back(3)
                            back(3)
                            back(3)  # 回到主界面
                            break
            break


def __detect_color__(
        region_coords: Tuple[float, float, float, float],
        target_color: Tuple,
        tag: str = "",
        tolerance: int = 30
) -> bool:
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
