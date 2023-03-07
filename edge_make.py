import numpy as np
import matplotlib.pyplot as plt
import math
import os
import cv2

tampered_file = './data/tampered_imgs.txt'
untampered_file = './data/untampered_imgs.txt'
train_tampered_imgs_path = './datas/train/train/tampered/imgs/'
train_untampered_path = './datas/train/train/untampered/'
tampered_file_output = './datas/train/trans_tampered/'
untampered_file_output = './datas/train/trans_untampered/'



def Edge_Extract():

    train_tampered_imgs_list = os.listdir(train_tampered_imgs_path)
    index = 0
    for image in train_tampered_imgs_list:
        edge_root = tampered_file_output + image
        img = cv2.imread(train_tampered_imgs_path + image, 0)
        edges = cv2.Canny(img, 100, 200)
        cv2.imwrite(edge_root, edges)
        index += 1
        print('NO.' + str(index) + 'edge_imgs output!\n')
    return 0

if __name__ == "__main__":
    Edge_Extract()
    print('****All is ok!****\n')



