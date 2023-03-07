import os


test_path = './datas/test/imgs/'
train_tampered_imgs_path = './datas/train/train/tampered/imgs/'
train_tampered_masks_path = './datas/train/train/tampered/masks/'
train_tampered_edge_path = './datas/train/trans_tampered/'
train_untampered_path = './datas/train/train/untampered/'
#submission_path ='./datas/example/competition2/815914/2023-02-14_14_06_41/submission'

# 获取文件名
train_tampered_imgs_list =os.listdir(train_tampered_imgs_path)
train_tampered_masks_list = os.listdir(train_tampered_masks_path)
train_untampered_list =os.listdir(train_untampered_path)
train_tampered_edge_list =os.listdir(train_tampered_edge_path)
#test_list = os.listdir(test_path)

train_tampered_edge_list.sort(key=lambda x: int(x[ 0:-4]))

train_untampered_list= sorted(train_untampered_list)
train_tampered_imgs_list= sorted(train_tampered_imgs_list)
train_tampered_masks_list= sorted(train_tampered_masks_list)

#submission_list = os.listdir(submission_path)
'''
    with open ('./datas/example/competition2/label.txt', 'w') as f:
        for submission_name in submission_list:
            f.write(submission_name + ' 1\n')
        
    with open('./data/untampered_imgs.txt', 'w') as f:
        for untampered_name in train_untampered_list:
            f.write(train_untampered_path  + untampered_name + ' None 0\n')

    with open('./data/tampered_imgs.txt', 'w') as f:
        for tampered_name in train_tampered_imgs_list:
            f.write( train_tampered_imgs_path + tampered_name +'\n')

    with open('./data/mask_imgs.txt', 'w') as f:
        for masks_name in train_tampered_masks_list:
            f.write( train_tampered_masks_path + masks_name + ' 1\n')

    with open('./data/test.txt', 'w') as f:  # test
        for test_name in test_list:
            f.write( test_path + test_name + '\n')
'''

with open('./data/tampered_edge_imgs.txt', 'w') as f:
    for edge_name in train_tampered_edge_list:
        f.write(train_tampered_edge_path + edge_name + ' 1\n')

with open('./data/untampered_imgs.txt', 'w') as f:
    for untampered_name in train_untampered_list:
        f.write(train_untampered_path + untampered_name + ' None None 0\n')

with open('./data/tampered_imgs.txt', 'w') as f:
    for tampered_name in train_tampered_imgs_list:
        f.write(train_tampered_imgs_path + tampered_name + '\n')

with open('./data/mask_imgs.txt', 'w') as f:
    for masks_name in train_tampered_masks_list:
        f.write(train_tampered_masks_path + masks_name + '\n')

print('\n' + 'OK')
