import pygame, sys, logging, os, ctypes
from shutil import copyfile

# init
sys.path.append("./src/py")

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
log = logging
logfilepath = './src/debug/debug-log.log'

# dlc file path
dlc_logging_path = './dlc/dlc_logging'

def funcMsgBox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def init_win():
    print("재설정 하는중..")
    #pygame.display.set_icon('./src/img/icon.png')
    pygame.display.set_caption('THISGAMEREQUIRESDLCTOSHOWTITLE')

def init_logging():
    if os.path.isfile(logfilepath):
        print("로그파일 읽는중..")
        if os.path.isfile(logfilepath):
            print("설정 중..")
            log.basicConfig(filename=logfilepath, level=logging.INFO, encoding="utf-8")
        else:
            print("로그용 파일이 존재하지 않음, 복사중..")
            print("파일을 복사하는중..")
            copyfile(dlc_logging_path + 'debug-log.log', './src/debug/debug-log.log')
try:
    init_win()
    if(os.path.isdir('.\\dlc\\dlc_logging\\')):
        init_logging()
    else:
        funcMsgBox('DLC가 존재하지 않음', 'DLC "dlc_logging" 파일이 존재하지 않습니다.', 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")

        pygame.display.flip()
        clock.tick(60)
except Exception as e:
    log.error(e.add_note("welp"))

pygame.quit()