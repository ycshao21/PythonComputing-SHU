import os
import numpy as np
import matplotlib.pyplot as plt
from train import epoch_num, validate_interval


def loss_curve(train_loss_values, validate_loss_values, show):
    folder_path = "../plot"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    plt.plot(list(range(1, epoch_num + 1)),
             train_loss_values,
             color='red', marker='o', label="training")
    plt.plot(list(range(validate_interval, epoch_num + 1, validate_interval)),
             validate_loss_values,
             color='blue', marker='o', label="validation")
    plt.title("Loss curve")
    plt.legend()
    plt.savefig("../plot/loss_curve.png")
    if show:
        plt.show(block=True)


def acc_curve(train_acc_values, validate_acc_values, show):
    folder_path = "../plot"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    plt.plot(np.array(range(1, epoch_num + 1)),
             train_acc_values,
             color='red', marker='o', label="training")
    plt.plot(list(range(validate_interval, epoch_num + 1, validate_interval)),
             validate_acc_values,
             color='blue', marker='o', label="validation")
    plt.title("Accuracy curve")
    plt.legend()
    plt.savefig("../plot/acc_curve.png")
    if show:
        plt.show(block=True)
