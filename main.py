import pygame, sys, logging, os, ctypes

# init
sys.path.append("./src/py")

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
log = logging
logFilePath = './debug/debug-log.log'

# buttons
MB_OK = 0x0
MB_OKCXL = 0x01
MB_YESNOCXL = 0x03
MB_YESNO = 0x04
MB_HELP = 0x4000

# icons
ICON_EXCLAIM = 0x30
ICON_INFO = 0x40
ICON_STOP = 0x10

def funcMsgBox(title, text, icon ,style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, icon | style)

def init_win():
    print("재설정 하는중..")
    #pygame.display.set_icon('./src/img/icon.png')
    pygame.display.set_caption('no gamename right now lol')

def init_logging():
    try:
        print("Reading..")
        print(os.path.isfile(logFilePath))
        print("Setting up debug log..")
        log.basicConfig(filename='./debug/debug-log.log', level=logging.INFO, encoding="utf-8")
        print("Resetting..")
        f = open('./debug/debug-log.log', 'w')
        f.close()
    except FileNotFoundError:
        if os.path.isfile(logFilePath) == False:
            print("Logging file not exists, making...")
            try:
                f = open('./debug/debug-log.log', 'w')
                f.close()
            except:
                funcMsgBox('파일 읽기 오류', '"debug" 폴더 안에 있는 debug-log.log 파일을 읽는데 실패하였습니다.', ICON_STOP ,0)
                print("An error occurred while writing log file.")
                print("It may the file still exists but not able to read file or no permission to write file to location.")
                print("This isn't important error, executing..")

try:
    init_win()
    init_logging()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple")

        pygame.display.flip()
        clock.tick(60)
except Exception as e:
    funcMsgBox('게임 실행 오류', '게임을 실행하는도중 오류가 발생하였습니다.\n해당 오류가 계속 반복해서 나타날시 개발자에게 문의를 해주십시오.', ICON_STOP, 0)
    log.error(e)

pygame.quit()