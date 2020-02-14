from typing import List
import matplotlib.pyplot as plt
import numpy as np


def plot_2_img(img, img_2, text=''):
    # Plot the result
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
    f.tight_layout()

    ax1.imshow(img)
    ax1.set_title('Original Image', fontsize=40)

    ax2.imshow(img_2, cmap='gray')
    ax2.set_title(text, fontsize=40)
    plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)

def diff(a, b):
    if a is None:
        return 0
    x = abs(a - b)
    return x

def avg(lst: List[np.array]):
    if len(lst) > 0:
        return np.mean(lst, axis=0)
    else:
        return 0

def add_to_list(l: List, elt, max_len: int) -> List:
    l.append(elt)
    if len(l) >= max_len:
        l.pop(0)
    return l
