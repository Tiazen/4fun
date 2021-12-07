from pymouse import PyMouse
from PIL import ImageGrab, Image
from time import sleep
import cv2
import numpy

def main():
    # m = PyMouse()
    # sleep(3)
    # for i in range(69):
    #     img = ImageGrab.grab()
    #     for y in range(600, 604):
    #         for xx in range(1015, 1260):
    #             color = img.getpixel((xx, y))
    #             if color[0] <= 18 and color[1] <= 18 and color[2] <= 18:
    #                 print(color)
    #                 m.click(xx, y+7, 1)
    #                 break

    tracker = cv2.legacy.TrackerKCF_create()
    
    x1 = 1865
    x2 = 2300
    y1 = 260
    y2 = 1002

    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    frame = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)

    bbox = cv2.selectROI(frame, False)
    
    ok = tracker.init(frame, bbox)

    m = PyMouse()

    for i in range(1000):
        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        frame = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)

        ok, bbox = tracker.update(frame)
        
        if ok:
            m.click(int(x1 + bbox[0]+bbox[2]//2), int(y1 + bbox[1]+bbox[3]), 1)

        if cv2.waitKey(1) & 0xFF == ord('q'): # if press SPACE bar
            break

if __name__ == "__main__":
    main()