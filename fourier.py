import cv2
import numpy as np
import matplotlib.pyplot as plt

def fourier_numpy():
    img = cv2.imread('lady.JPG', cv2.IMREAD_GRAYSCALE)

    fnp = np.fft.fft2(img)
    fnpshift = np.fft.fftshift(fnp)
    spectrum_np = 20*np.log(np.abs(fnpshift))

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image NP'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(spectrum_np, cmap='gray')
    plt.title('Magnitude Spectrum NP'), plt.xticks([]), plt.yticks([])

    plt.show()

fourier_numpy()

def fourier_openCV():
    img = cv2.imread('lady.JPG', cv2.IMREAD_GRAYSCALE)

    fcv = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    fcvshift = np.fft.fftshift(fcv)
    spectrum_cv = 20*np.log(cv2.magnitude(fcvshift[:,:,0], fcvshift[:,:,1]))

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image CV'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(spectrum_cv, cmap='gray')
    plt.title('Magnitude Spectrum CV'), plt.xticks([]), plt.yticks([])

    plt.show()

fourier_openCV()

def fourier_last():
    img = cv2.imread('lady.JPG', cv2.IMREAD_GRAYSCALE)

    fnp = np.fft.fft2(img)
    fnpshift = np.fft.fftshift(fnp)

    rows, cols = img.shape
    crow, ccol = int(rows/2), int(cols/2)

    fnpshift[crow-30:crow+30, ccol-30:ccol+30] = 0
    fnpishift = np.fft.ifftshift(fnpshift)
    img_back = np.fft.ifft2(fnpishift)
    img_back = np.abs(img_back)

    plt.subplot(131), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(132), plt.imshow(img_back, cmap='gray')
    plt.title('After HPF'), plt.xticks([]), plt.yticks([])

    plt.subplot(133), plt.imshow(img_back)
    plt.title('Result Imgae'), plt.xticks([]), plt.yticks([])

    plt.show()

fourier_last()

