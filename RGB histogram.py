import matplotlib.pyplot as plt
import  numpy as np
import cv2


img= cv2.imread("image.jpg")
img = cv2.resize(img, (500,500))
cv2.imshow("image",img)


R = np.zeros((256), dtype=int)     #Empty matrices for Red, Green, Blue frequencies
G = np.zeros((256), dtype=int)
B = np.zeros((256), dtype=int)
k = 0

while k<256:
    R[k] = np.count_nonzero(img[:, :, 2] == k)    #R[0]= frequency of 0 ,  R[1]= frequency of 1 ....
    G[k] = np.count_nonzero(img[:, :, 1] == k)
    B[k] = np.count_nonzero(img[:, :, 0] == k)
    k = k+1


intensity = np.arange(0,256,1)      #intensity values between 0-255 and it counts one by one

plt.figure(figsize=(10,20))

#RED
plt.subplot(422)
plt.bar(intensity, R, color="red", width=0.5)
plt.ylabel("Frequency")
plt.title("RED")

#BLUE
plt.subplot(423)
plt.bar(intensity, G, color="green", width=0.5)
plt.xlabel("GREEN")
plt.ylabel("Frequency")


#GREEN
plt.subplot(421)
plt.bar(intensity, B, color="blue", width=0.5)
plt.ylabel("Frequency")
plt.title("BLUE")


plt.show()
cv2.waitKey(0)
