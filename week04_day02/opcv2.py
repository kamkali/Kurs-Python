import numpy as np
import cv2


def show_lenna():
    img: np.ndarray = cv2.imread('Lenna.png')
    print(type(img), np.shape(img), img.dtype)
    # img[120:320, 120:320] = 0
    edit_image(img, 0)
    cv2.imshow('myimag', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def edit_image(img, rgb: int):
    img[:, :, rgb] *= 2
    img[:, :, rgb] = np.where(img[:, :, rgb] > 125, 255, img[:, :, rgb])


def show_webcam():
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if ret_val:
            cv2.imshow('159.205.32.52 webcam', img)
            if cv2.waitKey(1) == ord('q'):
                break  # esc to quit
            cv2.destroyAllWindows()


if __name__ == '__main__':
    show_lenna()
    # show_webcam()
