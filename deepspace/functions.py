from utils.utils import *
from PIL import Image

red = (229, 124, 73)
yellow = (255, 231, 146)


def login():
    """登陆，点击进入游戏的页面 -> 主界面"""
    print("----------- login -----------")
    wait_pic("images/login/region.png", log="等待显示进入游戏的界面")
    back()
    touch_pos((550, 1550), log="点击进入游戏")
    wait_pic("images/login/main.png", log="确认目前在主界面")


def logout():
    """退出，主界面 -> 选择用户界面"""
    print("----------- logout -----------")
    return_home()
    touch_pos((127, 115), log="点击用户等级")
    wait_pic("images/login/user.png", log="确认目前在用户界面")
    touch_pos((920, 1810), log="点击设置按钮")
    ## 这里的两行，按理来说不需要等待
    touch_pos((250, 1775), log="点击退出账户")
    touch_pos((740, 1000), log="确认退出账户")
    wait_pic("images/login/privacy.png", log="等待回到同意协议界面")
    touch_pos((730, 1440), log="同意协议")
    wait_pic("images/login/logo.png", log="等待出现选择账户界面")


def return_home():
    while True:
        if exists_pic("images/login/main.png", threshold=0.9, log="判断是否在主界面"):
            break
        else:
            back(sleep_time=1)


def get_friend_energy():
    """领取好友体力"""
    print("----------- get_friend_energy -----------")
    return_home()
    touch_pos((65, 245), log="点击好友")
    if exists_pic("images/daily/friend_energy.png", threshold=0.9, log="判断是否领过体力"):
        back()
    else:  # 没领过
        touch_pos((755, 1745), log="领一下体力")
        back()


def get_energy():
    """领取早晚体力"""
    print("----------- get_energy -----------")
    return_home()
    touch_pos((1000, 985), log="点击日程")
    touch_pos((880, 1810), log="点击补给")

    if exists_pic("images/daily/day_night_energy.png", log="判断是否领过补给体力"):
        touch_pic("images/daily/day_night_energy.png", log="点击体力")
    touch_pos((925, 1535), log="点击跳过显示领取多少体力")
    back()


def daily_check():
    """领取每日签到奖励"""
    print("----------- daily_check -----------")
    return_home()
    touch_pos((1000, 985), log="点击日程")
    touch_pos((660, 1810), log="点击签到")
    if exists_pic("images/daily/daily_check.png", threshold=0.8, log="判断是否领过每日签到奖励"):
        touch_pic("images/daily/daily_check.png", log="领取签到奖励")
    return_home()


def explore():
    """星际探测"""
    print("----------- explore -----------")
    return_home()
    touch_pos((1005, 1275), log="点击许愿")
    touch_pos((995, 205), log="点击星际探测")
    if exists_pic("images/explore/exploring.png", log="判断是否正在探测"):
        return_home()
    elif exists_pic("images/explore/finish.png", log="判断是否探测完成"):
        touch_pos((540, 1635), sleep_time=5, log="点击收取")
        back()
        back()  # 防止有整卡
        touch_pos((360, 1605), log="点击开始探测")
        touch_pos((740, 995), log="点击确定")
        return_home()
    else:  # 在金砂页面
        touch_pos((330, 1545), log="回到银砂")
        touch_pos((360, 1605), log="点击开始探测")
        touch_pos((740, 995), log="点击确定")
        return_home()


def task(first_time: bool = True):
    """每日任务"""
    print("----------- task -----------")
    return_home()

    if first_time:
        store(week=False) # 商店购买
        daily_check()  # 每日签到
        get_friend_energy() # 领好友体力
    get_energy()    # 领早晚体力
    explore()   # 星际探测
    use_energy(first_time)
    get_daily_reward()
    # 主界面互动


def get_daily_reward():
    """领取任务奖励"""
    print("----------- get_daily_reward -----------")
    return_home()
    touch_pos((1000, 985), log="点击日程")
    touch_pos((840, 1700), log="点击一键领取（完成任务）")
    touch_pos((840, 1700), log="点击一键领取（领奖励）")
    return_home()


def store(week=False):
    """商店购买"""
    print("----------- store -----------")
    return_home()
    touch_pos((1000, 1420), log="点击商店")
    touch_pos((375, 320), log="点击礼包")
    swipe_pos((1010, 1635), (1010, 550), duration=0.3, log="下滑到免费礼包")
    if exists_pic("images/daily/free_day.png", threshold=0.95, log="判断每日礼包有没有领到"):
        touch_pic("images/daily/free_day.png", threshold=0.95, log="点击礼包")
        touch_pos((560, 1385), log="点击购买")
    if week and exists_pic("images/daily/free_week.png", threshold=0.95, log="判断每周礼包有没有领到"):
        touch_pic("images/daily/free_week.png", threshold=0.95, log="点击礼包")
        touch_pos((560, 1385), log="点击购买")
    return_home()


def use_energy(first_time: bool = True):
    """刷材料的规划，需要收藏两张卡，一张用来升级一次卡面，另一张用来刷完体力，也可以都是第一张，第二张主要是升级不了的话备选"""
    print("----------- use_energy -----------")
    isUpgrade = True
    has_energy = True
    has_energy_first_time = False
    wait_pic("images/login/main.png", log="确认目前在主界面")
    if first_time:  # 第一次收体力，需要完成日常任务-升级一次
        touch_pos((530, 1785), sleep_time=5, log="点击作战")
        touch_pos((390, 490), sleep_time=10, log="点击零点追踪")
        touch_pos((330, 660), sleep_time=5, log="点击哈特")
        has_energy_first_time = __material__(multiple=False)    # 刷一次瓶子，完成后回到主界面
    touch_pos((680, 1785), sleep_time=5, log="点击思念")
    touch_pos((280, 700), sleep_time=10, log="点击第一张卡")
    if not exists_pic("images/fight/show_info.png", log="判断卡面信息是否被点掉了"):
        print("卡面信息被点掉了")
        back()
    touch_pos((285, 1700), sleep_time=5, log="点击第一个圈")
    if exists_pic("images/fight/upgrade.png", threshold=0.95, log="判断是否是升级"):
        print("需要升级")
        isUpgrade = True
        return_home()
        touch_pos((530, 1785), sleep_time=5, log="点击作战")
        touch_pos((390, 490), sleep_time=10, log="点击零点追踪")
        touch_pos((330, 660), sleep_time=5, log="点击哈特")
        has_energy = __material__(multiple=True)  # 刷瓶子
    else:   # 是突破，需要先刷材料，再到第二张卡去升级
        print("需要突破")
        isUpgrade = False
        touch_pos((200, 1750), sleep_time=5, log="点击最低等级材料")
        touch_pic("images/fight/go.png", log="跳转到对应材料")
        has_energy = __material__(multiple=True)     # 刷材料
    # 升级一下
    if has_energy or has_energy_first_time:
        wait_pic("images/login/main.png", log="确认目前在主界面")
        touch_pos((680, 1785), sleep_time=5, log="点击思念")
        if isUpgrade:
            touch_pos((280, 700), sleep_time=10, log="点击第一张卡")
        else:
            touch_pos((550, 700), sleep_time=5, log="点击第二张卡")
        if not exists_pic("images/fight/show_info.png", log="判断卡面信息是否被点掉了"):
            back()
        touch_pos((285, 1700), sleep_time=5, log="点击第一个圈")
        touch_pos((200, 1750), sleep_time=5, log="升级最小单位瓶子")
        touch_pos((840, 1765), sleep_time=5, log="点击提升一级")
        return_home()


def __material__(multiple: bool = True):
    """刷材料的逻辑，multiple为true指刷十次，false指刷一次，从显示等级的页面开始运行，刷什么材料要在调用之前写好"""
    print("----------- __material__ -----------")
    material_list = [(695, 535), (870, 735), (745, 930), (530, 1115), (310, 975), (515, 790),
                     (260, 600), (475, 450), (345, 315)]
    # region1 = (210, 1420, 370, 1470)  # 自动追击一次
    # region2 = (420, 1420, 580, 1470)  # 自动追击十次
    has_energy = True
    for i in range(len(material_list)):
        touch_pos(material_list[i], log=f"点击等级{9-i}")  # 接下来判断这关有没有打过
        if not exists_pic("images/fight/success.png", threshold=0.9, log="判断是不是锁着"):
            print(f"关卡{9-i}锁住")
            continue
        region1 = exists_pic("images/fight/fight1.png", threshold=0.9, log="获取 追击一次 的坐标")
        region2 = exists_pic_pos("images/fight/fight10.png", threshold=0.9, log="获取 追击十次 的坐标")
        if not region1:
            back()
            print(f"关卡{9-i}未通关")
            continue
        else:
            print(f"选择关卡{9 - i}")
            while True:
                if region2 is None:
                    print("只剩一次的体力")
                    touch_pic("images/fight/fight1.png", threshold=0.9, log="追击一次")
                    return_home()
                    break
                else:   # region1、region2都找到了按钮
                    if __detect_color__((region2[0]-80, region2[1]-25, region2[0]+80, region2[1]+25), red, tag="红色"):
                        print("没有体力")
                        return_home()
                        break
                    else:
                        print("还有很多体力")
                        touch_pic("images/fight/fight10.png", threshold=0.9, sleep_time=15, log="追击十次")
                        back(1)
            break
        # # elif exists_pic("images/fight/lock.png", threshold=0.8, log="判断是不是没通关"):
        # if not __detect_color__(region1, yellow, tag="light yellow", tolerance=10):
        #     back()
        #     print(f"关卡{9-i}未通关")
        #     continue
        # else:  # 能刷材料
        #     print(f"选择关卡{9-i}")
        #     if __detect_color__(region1, red, "红色"):  # 自动追击一次是红的，说明没体力
        #         print("√ 1. 检测到红色，自动追击一次是红色")
        #         return_home()
        #         has_energy = False
        #     else:
        #         print("× 2. 未检测到红色，自动追击一次不是红色")
        #         if not multiple:  # 只想刷一次，用在豆佬哈特每日任务上
        #             touch_pos((290, 1445), sleep_time=5, log="追击一次")
        #             # wait_pic("images/fight/finish.png", timeout=15, log="等待追击完成")
        #             return_home()
        #         else:   # 追击多次
        #             while True:
        #                 if not __detect_color__(region1, red, "红色"):    # 自动追击一次没有红的，说明有体力，体力>=8
        #                     print("× 3. 未检测到红色，自动追击一次不是红色")
        #                     if __detect_color__(region2, yellow, "黄色"): # 体力>=16
        #                         print("√ 4. 检测到黄色，自动追击十次是黄色")
        #                         touch_pos((510, 1445), sleep_time=15, log="追击十次")
        #                         # wait_pic("images/fight/finish.png", timeout=15, log="等待追击完成")
        #                         back()  # 关掉追击结果
        #                     else:   # 自动追击十次那里是黑的，体力<16，只能追击一次
        #                         print("× 5. 未检测到黄色，自动追击十次不是黄色")
        #                         touch_pos((290, 1445), sleep_time=5, log="追击一次")
        #                         # wait_pic("images/fight/finish.png", timeout=15, log="等待追击完成")
        #                         back()  # 关掉追击结果
        #                 else:
        #                     print("√ 6. 检测到红色，自动追击一次是红色")
        #                     return_home()
        #                     break
        #     break
    return has_energy

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
                return True
    return False
