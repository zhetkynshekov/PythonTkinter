from PIL import Image, ImageTk
from screeninfo import get_monitors

def get_geometry(root):
    x = True
    # root.overrideredirect(x) полноэкранный режим
    root.resizable(False, True) #Функция отключаюшее изминение размера окна
    # root.iconify() функция для того чтобы скрывать программу
    root.state('zoomed')
    get_mon = get_monitor()
    monitor = str(get_mon[0]) + "x" + str(get_mon[1]) + "+0+0"
    root.geometry(monitor)
    def exit_win(event):
        root.destroy()
    # def exit_fill(event, x):
    #     if x == True:
    #         x = False
    #         root.overrideredirect(x)
    #     else:
    #         x = True
    #         root.overrideredirect(x)

    root.bind('<Control-q>', exit_win)
    # root.bind('<Control-r>', exit_fill(x))

def get_monitor():
    for m in get_monitors():
        width = m.width
        heigth = m.height
        return width, heigth

def resize_custom(str, x, y):
    image = Image.open(str)
    image = image.resize((x, y), Image.ANTIALIAS)
    return image