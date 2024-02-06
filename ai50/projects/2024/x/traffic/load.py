import os
import sys
import numpy as np
import cv2

IMG_WIDTH = 30
IMG_HEIGHT = 30

def main():
    print(load(sys.argv[1]))

def load(data_dir):
    images = []
    labels = []

    for category in os.listdir(data_dir):
        # MacOS
        if category == '.DS_Store':
            continue
    
        c = os.path.join(data_dir, category)
        for filename in os.listdir(c):
            img = cv2.imread(os.path.join(c, filename))
            # image can't be opened
            if img is not None:
                img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
                # check resized correctly
                # print(img.shape)
                images.append(img)
                # label each input image
                labels.append(int(category))

    return (images, labels)


if __name__ == "__main__":
    main()