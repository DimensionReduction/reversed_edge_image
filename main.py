
import cv2
import imageio
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.animation as amt

gif=imageio.mimread('under one person.gif')# 仅支持英文路径

plt.ion()
fig,ax=plt.subplots(3,2)

def graph(img):
    f1=ax[0,0].imshow(img)
    ax[0,0].set_title('Original Image'),ax[0,0].set_xticks([]),ax[0,0].set_yticks([])

    img2=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
    f2=ax[0,1].imshow(img2)
    ax[0,1].set_title('RGB_to_BGR Image'),ax[0,1].set_xticks([]),ax[0,1].set_yticks([])

    img3=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    f3=ax[1,0].imshow(img3)
    ax[1,0].set_title('BGR_to_Gray Image'),ax[1,0].set_xticks([]),ax[1,0].set_yticks([])

    matrix=np.asarray(img2)
    matrix=255-matrix
    img4=Image.fromarray(matrix)
    f4=ax[1,1].imshow(img4)
    ax[1,1].set_title('Reversed BGR Image'),ax[1,1].set_xticks([]),ax[1,1].set_yticks([])

    edges=cv2.Canny(img2,50,200)
    f5=ax[2,0].imshow(edges,cmap='gray')
    ax[2,0].set_title('Edge Image'),ax[2,0].set_xticks([]),ax[2,0].set_yticks([])

    matrix2=np.asarray(edges)
    matrix2=255-matrix2
    edges2=Image.fromarray(matrix2)
    f6=ax[2,1].imshow(edges2,cmap='gray')
    ax[2,1].set_title('Reversed Edge Image'),ax[2,1].set_xticks([]),ax[2,1].set_yticks([])

    plt.pause(0.01)
    return f1,f2,f3,f4,f5,f6

artists=[]
for img in gif:
    g=graph(img)
    artists.append(g)

plt.ioff()
plt.show()
amt.ArtistAnimation(fig=fig,artists=artists).save('动图.gif',writer='pillow',fps=60,dpi=100)# fps：每秒帧数，dpi：每英寸像素点