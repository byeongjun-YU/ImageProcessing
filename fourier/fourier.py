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

def fourier_HPF():
    img = cv2.imread('lady.JPG', cv2.IMREAD_GRAYSCALE)

    f = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    fshift = np.fft.fftshift(f)

    rows, cols = img.shape
    crow, ccol = int(rows / 2), int(cols / 2)

    fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0
    fishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(fishift)
    img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(img_back, cmap='gray')
    plt.title('Result HPF'), plt.xticks([]), plt.yticks([])

    plt.show()

fourier_HPF()

def fourier_LPF():
    img = cv2.imread('lady.JPG', cv2.IMREAD_GRAYSCALE)

    f = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
    fshift = np.fft.fftshift(f)

    rows, cols = img.shape
    crow, ccol = int(rows / 2), int(cols / 2)

    mask = np.zeros((rows, cols, 2), np.uint8)
    mask[crow-30:crow+30, ccol-30:ccol+30] = 1
    fshift = fshift*mask
    fishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(fishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(122), plt.imshow(img_back, cmap='gray')
    plt.title('Result LPF'), plt.xticks([]), plt.yticks([])

    plt.show()

fourier_LPF()