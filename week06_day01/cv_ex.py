import cv2
import dlib
from contextlib import contextmanager
import imutils


@contextmanager
def open_stream(cam_id):
    print('Opening stream')
    cam_stream = cv2.VideoCapture(cam_id)
    yield cam_stream
    cam_stream.release()
    cv2.destroyAllWindows()
    print('Closing stream')


# credits: https://www.codemade.io/fast-and-accurate-face-tracking-in-live-video-with-python/
def draw_border(img, pt1, pt2, color, thickness, r, d):
    x1, y1 = pt1
    x2, y2 = pt2

    # Top left drawing
    cv2.line(img, (x1 + r, y1), (x1 + r + d, y1), color, thickness)
    cv2.line(img, (x1, y1 + r), (x1, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x1 + r, y1 + r), (r, r), 180, 0, 90, color, thickness)

    # Top right drawing
    cv2.line(img, (x2 - r, y1), (x2 - r - d, y1), color, thickness)
    cv2.line(img, (x2, y1 + r), (x2, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x2 - r, y1 + r), (r, r), 270, 0, 90, color, thickness)

    # Bottom left drawing
    cv2.line(img, (x1 + r, y2), (x1 + r + d, y2), color, thickness)
    cv2.line(img, (x1, y2 - r), (x1, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x1 + r, y2 - r), (r, r), 90, 0, 90, color, thickness)

    # Bottom right drawing
    cv2.line(img, (x2 - r, y2), (x2 - r - d, y2), color, thickness)
    cv2.line(img, (x2, y2 - r), (x2, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x2 - r, y2 - r), (r, r), 0, 0, 90, color, thickness)


def get_frames(camera_stream):
    while True:
        ret, frame = camera_stream.read()
        if ret:
            yield frame
        else:
            break


def show_img(frame, wait_key=1):
    cv2.imshow("Camera stream", frame)
    return cv2.waitKey(wait_key)


def webcam():
    detector = dlib.get_frontal_face_detector()
    with open_stream(0) as cam:
        for frame in get_frames(cam):

            # credits: https://www.codemade.io/fast-and-accurate-face-tracking-in-live-video-with-python/
            frame = imutils.resize(frame, width=700)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            overlay = frame.copy()
            output = frame.copy()
            alpha = 0.5
            face_rects = detector(gray, 0)
            for i, d in enumerate(face_rects):
                x1, y1, x2, y2, w, h = d.left(), d.top(), d.right() + 1, d.bottom() + 1, d.width(), d.height()

                # draw a fancy border around the faces
                draw_border(overlay, (x1, y1), (x2, y2), (162, 255, 0), 2, 10, 10)
            cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
            # credits: https://www.codemade.io/fast-and-accurate-face-tracking-in-live-video-with-python/

            key = show_img(output, wait_key=1)
            if key == ord('q'):
                break


if __name__ == '__main__':
    webcam()
