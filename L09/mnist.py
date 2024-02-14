import sys
import numpy as np
import matplotlib.pyplot as plt

if (len(sys.argv) < 4):
    print ("Not enough command line arguments")
    exit(1)

imagefile = sys.argv[1]
idx1 = int(sys.argv[2])
idx2 = int(sys.argv[3])

# read the data file
data = np.loadtxt(sys.stdin,comments='#')

plt.rcParams['figure.figsize'] = (20, 20)
plt.rc('xtick', labelsize=20) 
plt.rc('ytick', labelsize=20) 
plt.rcParams['axes.facecolor']='white'
plt.rcParams['savefig.facecolor']='white'
image1 = np.asarray(data[idx1]).reshape(28,28)
image2 = np.asarray(data[idx2]).reshape(28,28)

f, axarr = plt.subplots(1,2)
axarr[0].imshow(image1,cmap='gray',vmin=0, vmax=255, interpolation='none')
axarr[1].imshow(image2,cmap='gray',vmin=0, vmax=255, interpolation='none')
plt.savefig(imagefile,bbox_inches='tight')
