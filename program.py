from easyfacenet.simple import facenet
import cv2
import os, errno

images = []


def capture_images():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Smile! Press SPACE to capture.")
    img_counter = 1

    while True:
        ret, frame = cam.read()
        cv2.imshow("Picture", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k % 256 == 27:
            # ESC pressed
            print("Escape key hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            img_path = "assets/img" + str(img_counter) + ".png"
            remove_if_exist(img_path)
            cv2.imwrite(img_path, frame)
            images.append(img_path)
            print(img_path + " written!")
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()


def remove_if_exist(filename):
    try:
        os.remove(filename)
    except OSError as e:
        if e.errno != errno.ENONET:  # errno.ENONET = no such file or directory
            raise


def main():
    capture_images()
    aligned = facenet.align_face(images)
    comparisons = facenet.compare(aligned)

    print("Is image 1 and 2 similar? ", bool(comparisons[0][1]))
    print("Is image 1 and 3 similar? ", bool(comparisons[0][2]))


if __name__ == "__main__":
    main()
