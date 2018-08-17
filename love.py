import os
import sys
import random

import pygame
from pygame.locals import *


# 设置窗口长宽
WIDTH, HEIGHT = 640, 480
# 设置背景颜色RGB
BACKGROUND = (255, 255, 255)
# 设置基础文件路径
if getattr(sys, 'frozen', False):
    CurrentPath = sys._MEIPASS
else:
    CurrentPath = os.path.dirname(__file__)
# 字体文件路径
FONTPATH = os.path.join(CurrentPath, 'msyhl.ttc')
# 音乐文件路径，建议不要有中文
MUSICPATH = os.path.join(CurrentPath, '1.mp3')
# 图片文件路径，建议不要有中文
IMGPATH = os.path.join(CurrentPath, '1.png')


# 按钮
def button(text, x, y, w, h, color, screen):
    '''
    按钮接口
    :param text: 
    :param x: 
    :param y: 
    :param w: 
    :param h: 
    :param color: 
    :param screen: 
    :return: 
    '''
    # 画一个矩形
    pygame.draw.rect(screen, color, (x, y, w, h))
    font = pygame.font.Font(FONTPATH, 20)
    textRender = font.render(text, True, (0, 0, 0))
    textRect = textRender.get_rect()
    # 按钮文本中心点位置
    textRect.center = ((x+w/2), (y+h/2))
    screen.blit(textRender, textRect)


# 标题
def title(text, screen, scale, color=(255, 0, 0)):
    '''
    标题接口
    :param text:
    :param screen:
    :param scale:
    :param color:
    :return:
    '''
    font = pygame.font.Font(FONTPATH, WIDTH//(len(text)*2))
    textRender = font.render(text, True, color)
    textRect = textRender.get_rect()
    textRect.midtop = (WIDTH/scale[0], HEIGHT/scale[1])
    screen.blit(textRender, textRect)


# 生成随机的位置坐标
def get_random_pos():
    x, y = random.randint(20, 620), random.randint(20, 460)
    return x, y


# 点击喜欢按钮后显示的页面
def show_like_interface(text, screen, color=(255, 0, 0)):
    screen.fill(BACKGROUND)
    font = pygame.font.Font(FONTPATH, WIDTH//(len(text)))
    textRender = font.render(text, True, color)
    textRect = textRender.get_rect()
    textRect.midtop = (WIDTH/2, HEIGHT/2)
    screen.blit(textRender, textRect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


# 主函数
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    # 设置窗口显示标题
    pygame.display.set_caption('FROM一个喜欢你很久的小哥哥(#^.^#)')

    clock = pygame.time.Clock()
    # 加载音乐
    pygame.mixer.music.load(MUSICPATH)
    # 音乐从头开始播放
    pygame.mixer.music.play(-1, 1)
    # 设置音量
    pygame.mixer.music.set_volume(0.25)
    # 不同意按钮初始位置
    unlike_pos_x = 330
    unlike_pos_y = 250
    # 不同意按钮宽高、颜色
    unlike_pos_width = 100
    unlike_pos_height = 50
    unlike_color = (182, 194, 154)
    # 同意按钮初始位置
    like_pos_x = 180
    like_pos_y = 250
    # 同意按钮宽高、颜色
    like_pos_width = 100
    like_pos_height = 50
    like_color = (255, 192, 203)
    # 设置循环标记为True
    running = True
    # 死循环
    while running:
        # 设置背景颜色
        screen.fill(BACKGROUND)
        # 加载图片
        img = pygame.image.load(IMGPATH)
        imgRect = img.get_rect()
        imgRect.midtop = int(WIDTH/1.3), HEIGHT//7
        screen.blit(img, imgRect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 获取鼠标位置
                mouse_pos = pygame.mouse.get_pos()
                # 当鼠标的位置的宽高在 同意按钮 的范围之内，设置循环标记为False
                if mouse_pos[0] < like_pos_x+like_pos_width+5 and mouse_pos[0] > like_pos_x-5 and\
                    mouse_pos[1] < like_pos_y+like_pos_height+5 and mouse_pos[1] > like_pos_y-5:
                    like_color = BACKGROUND
                    running = False
        # 获取鼠标位置
        mouse_pos = pygame.mouse.get_pos()
        # 当鼠标的位置的宽高在 不同意按钮 的范围之内，随机生成不同意按钮的位置
        if mouse_pos[0] < unlike_pos_x+unlike_pos_width+5 and mouse_pos[0] > unlike_pos_x-5 and\
            mouse_pos[1] < unlike_pos_y+unlike_pos_height+5 and mouse_pos[1] > unlike_pos_y-5:
            while True:
                unlike_pos_x, unlike_pos_y = get_random_pos()
                # 检测鼠标，如果还是想点击不同意，继续回到此循环，让不同意按钮到处跑
                if mouse_pos[0] < unlike_pos_x+unlike_pos_width+5 and mouse_pos[0] > unlike_pos_x-5 and\
                    mouse_pos[1] < unlike_pos_y+unlike_pos_height+5 and mouse_pos[1] > unlike_pos_y-5:
                    continue
                # 如果鼠标不进入不同意按钮的范围内，跳出本次循环，暂时让不同意按钮待在那里
                break
        # 设置窗口内显示的话语，及其显示的位置
        title('小霞子，我观察你很久了', screen, scale=[3, 8])
        title('做我女朋友好不好呀', screen, scale=[3, 4])
        # 设置 同意按钮 与 不同意按钮
        button('好呀', like_pos_x, like_pos_y, like_pos_width, like_pos_height, like_color, screen)
        button('算了吧', unlike_pos_x, unlike_pos_y, unlike_pos_width, unlike_pos_height, unlike_color, screen)
        # 把刚才设置的内容更新到窗口去
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
    # 如果对象折服了，就显示下面的文字
    show_like_interface('我就知道小霞子你也喜欢我 mua! (*╯3╰)', screen, color=(255, 0, 0))


if __name__ == '__main__':
    main()

