import sys
from tqdm import trange
from string import digits, ascii_uppercase, ascii_lowercase
import pandas as pd
import cv2
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import Dataset, DataLoader  # 用于装载数据集
from torchvision import transforms  # 用于图形变换

train_batch_size = 16
device = torch.device('cuda' if torch.cuda.is_available else 'cpu')  # 优先选择GPU
transformer = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize(mean=[0.5], std=[0.2]),
     transforms.Resize((64, 64), antialias=True)])  # 将1200*900的图片转换为64*64


# 继承torch.utils.data.Dataset，实现__init__，__len__和__getitem__方法
class MyDataset(Dataset):
    def __init__(self, images, labels):
        self.images = images
        self.labels = labels

    def __len__(self):
        """ 获取数据量 """
        return len(self.images)

    def __getitem__(self, index):
        """ 获取第index个数据和标签 """
        return self.images[index], self.labels[index]


def load_dataset():
    # 读取english.csv，获取文件名和标签列表
    # ---------------------
    # |  image  |  label  |
    # ---------------------
    csv_path = "..\\dataset\\english.csv"
    csv_info = pd.read_csv(csv_path)  # 读取english.csv文件
    images: list = csv_info["image"].values
    labels: list = csv_info["label"].values

    # 创建字典 {标签: 编号}
    # 数字：0 -> 0 ... 9 -> 9
    # 大写字母：A -> 10 ... Z -> 35
    # 小写字母：a -> 36 ... z -> 61
    label_string = digits + ascii_uppercase + ascii_lowercase
    label_dict = dict()
    for img_labels, label in enumerate(label_string):
        label_dict[label] = img_labels

    # 构建图片与标签编号列表
    pbar_load = trange(len(images), file=sys.stdout)
    for i in pbar_load:
        img_path = "..\\dataset\\Img\\" + images[i][4:]
        img = cv2.imread(img_path)  # 读取图像
        images[i] = transformer(img).to(device)
        label = label_dict[labels[i]]  # 标签转换
        labels[i] = torch.tensor(label).to(device)
    pbar_load.close()

    # 按8:1:1的比例随机划分训练集、验证集和测试集
    train_images, images, train_labels, labels = train_test_split(images, labels, train_size=0.8)
    validate_images, test_images, validate_labels, test_labels = train_test_split(images, labels, train_size=0.5)
    # 装载训练集
    train_data = MyDataset(train_images, train_labels)
    train_data = DataLoader(dataset=train_data, batch_size=train_batch_size, shuffle=True)
    # 装载验证集
    validate_data = MyDataset(validate_images, validate_labels)
    validate_data = DataLoader(dataset=validate_data, batch_size=1, shuffle=False)
    # 装载测试集
    test_data = MyDataset(test_images, test_labels)
    test_data = DataLoader(dataset=test_data, batch_size=1, shuffle=False)
    return train_data, validate_data, test_data
