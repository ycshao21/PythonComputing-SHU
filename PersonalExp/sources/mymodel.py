from torch import nn
from torchvision.models import resnet34  # 残差神经网络


class MyModel(nn.Module):
    """
    # 继承torch.nn.Module，实现__init__和forward方法
    """
    def __init__(self, output):
        super().__init__()
        self.model = resnet34(weights=None)
        self.model.fc = nn.Linear(in_features=512, out_features=output)  # 全连接层

    def forward(self, x):
        return self.model(x)
