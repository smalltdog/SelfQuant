import torch
import torch.nn as nn

print(torch.cuda.is_available())

class NetBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(NetBlock, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1)
        self.relu = nn.ReLU()

    def forward(self, x):
        return self.relu(self.conv(x))