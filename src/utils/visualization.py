import matplotlib.pyplot as plt
from typing import List, Union
import numpy as np

def plot_loss(losses: Union[List, np.ndarray], save_path: str = None):
    '''绘制损失下降曲线并保存为png格式图片

    如果没有给定save_path, 默认不保存图片

    Attributes:
        losses (List or np.ndarray): 损失记录
        save_path (str, optional):图片保存路径
    '''
    plt.plot(losses)
    plt.xlabel('steps')
    plt.ylabel('losses')
    plt.title('losses curve')
    plt.savefig(save_path) if save_path else None
    plt.show()
