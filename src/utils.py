import matplotlib.pyplot as plt


def plot_2_img(img, img_2, text=''):
    # Plot the result
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))
    f.tight_layout()

    ax1.imshow(img)
    ax1.set_title('Original Image', fontsize=40)

    ax2.imshow(img_2, cmap='gray')
    ax2.set_title(text, fontsize=40)
    plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
