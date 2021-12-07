from pymouse import PyMouse
from PIL import ImageGrab
from time import sleep

def main():
    m = PyMouse()
    sleep(3)
    for i in range(69):
        img = ImageGrab.grab()
        for y in range(600, 604):
            for xx in range(1015, 1260):
                color = img.getpixel((xx, y))
                if color[0] <= 18 and color[1] <= 18 and color[2] <= 18:
                    print(color)
                    m.click(xx, y+7, 1)
                    break
        
if __name__ == "__main__":
    main()