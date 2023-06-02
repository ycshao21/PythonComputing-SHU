import torch
from torch import nn
import time
from tqdm import tqdm
import sys

from load_dataset import load_dataset, device, train_batch_size
from mymodel import MyModel
from draw_plot import *

model_name = "model"
epoch_num = 25  # 进行25轮训练
learning_rate = 0.001
validate_interval = 5

folder_path = "../models"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


def train(test=False, show_plot=True):
    """
    epoch_num: 训练轮数
    test: 是否在测试集上运行模型
    """
    # 记录训练与验证时loss和accuracy的变化，用于绘图
    train_loss_values = list()
    validate_loss_values = list()
    train_acc_values = list()
    validate_acc_values = list()

    print("Building network...\n")
    label_num = 62
    model = MyModel(label_num).to(device)  # 建立模型

    print("Loading dataset...")
    train_data, validate_data, test_data = load_dataset()  # 装载数据集
    criterion = nn.CrossEntropyLoss().to(device)  # 交叉熵损失函数
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)  # 优化器
    best_train_loss, best_validate_loss = 1000, 1000  # 最佳损失值
    torch.cuda.empty_cache()  # 释放GPU显存

    print("\nStart training...")
    start = time.time()
    for epoch in range(epoch_num):
        print(f"epoch: {epoch + 1}/{epoch_num}")

        # 训练模式
        train_loss, train_correct = 0, 0
        model.train()
        for x, y in tqdm(train_data, desc="Training", colour="red", file=sys.stdout):
            y = y.reshape(-1)  # 将y转为一维数组
            x, y = x.to(device), y.to(device)
            y_pred = model(x)  # 预测结果
            _, y_max = torch.max(y_pred.data, 1)  # 最大值

            loss = criterion(y_pred, y)
            train_loss += loss.item()
            train_correct += torch.sum(y_max == y).cpu()

            optimizer.zero_grad()  # 梯度清零
            loss.backward()  # 反向传播
            optimizer.step()  # 更新训练参数

        # 计算平均损失值
        train_avg_loss = train_loss / len(train_data)
        train_loss_values.append(train_avg_loss)
        if train_avg_loss < best_train_loss:
            best_train_loss = train_avg_loss
        # 计算准确率
        train_accuracy = train_correct / (train_batch_size * len(train_data))
        train_acc_values.append(train_accuracy)
        print(f"train_loss: {train_avg_loss:.5f}, train_accuracy: {100 * train_accuracy:.5f}%, "
              f"best_train_loss: {best_train_loss:.5f}")

        # 评估模式
        if (epoch + 1) % validate_interval == 0:
            validate_loss, validate_correct = 0, 0
            model.eval()
            print()
            with torch.no_grad():  # 不记录梯度信息
                for x, y in tqdm(validate_data, desc="Validating", colour="yellow", file=sys.stdout):
                    y = y.reshape(-1)  # 将y转为一维数组
                    x, y = x.to(device), y.to(device)
                    y_pred = model(x)  # 预测结果
                    _, y_max = torch.max(y_pred.data, 1)  # 最大值

                    loss = criterion(y_pred, y)  # 计算代价函数
                    validate_loss += loss.item()
                    validate_correct += torch.sum(y_max == y).cpu()

                validate_avg_loss = validate_loss / len(validate_data)
                validate_loss_values.append(validate_avg_loss)
                if validate_avg_loss < best_validate_loss:
                    best_validate_loss = validate_avg_loss
                # 计算准确率
                validate_accuracy = validate_correct / len(validate_data)
                validate_acc_values.append(validate_accuracy)
                print(f"validate_loss: {validate_avg_loss:.5f}, "
                      f"validate_accuracy: {100 * validate_accuracy:.5f}%, "
                      f"best_validate_loss: {best_validate_loss:.5f}")
        print("-------------------------------------------------------------")
    end = time.time()
    print("Training ends.")
    print(f"Training time: {end - start}s.")

    if test is True:
        test_loss, test_correct = 0, 0
        model.eval()
        with torch.no_grad():  # 不记录梯度信息
            for x, y in tqdm(test_data, desc="Testing", colour="green", file=sys.stdout):
                y = y.reshape(-1)  # 将y转为一维数组
                x, y = x.to(device), y.to(device)
                y_pred = model(x)  # 预测结果
                _, y_max = torch.max(y_pred.data, 1)  # 最大值
                test_correct += torch.sum(y_max == y)
            # 计算准确率
            test_accuracy = test_correct / len(test_data)
            print(f"\ntest_accuracy: {100 * test_accuracy:.5f}%")

    # 保存模型
    torch.save(model.state_dict(), f"../models/{model_name}.pkl")

    # 绘制loss和accuracy图像
    loss_curve(train_loss_values, validate_loss_values, show_plot)
    acc_curve(train_acc_values, validate_acc_values, show_plot)


if __name__ == '__main__':
    train(test=True, show_plot=True)
