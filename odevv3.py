"""import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread("pirincc.jpg")

# Görüntüyü griye dönüştür
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Eşik değerini belirle
threshold_value = 127

# Eşikleme işlemi uygula
_, threshold = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

# Kontürleri bul
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Pirinç sayısını yazdır
print("Pirinç sayısı:", len(contours))

# Eşiklenmiş görüntüyü göster
cv2.imshow("Eşiklenmiş Görüntü", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

"""import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread("pirinc.jpg")

# Görüntüyü griye dönüştür
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Adaptif eşikleme uygula
threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Kontürleri bul
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Siyah bir görüntü oluştur
black_image = np.zeros_like(image)

# Kontürleri siyah görüntü üzerine çiz
cv2.drawContours(black_image, contours, -1, (0, 0, 0), thickness=cv2.FILLED)

# Siyah arkaplanlı görüntüyü göster
cv2.imshow("Siyah Arkaplanlı Görüntü", black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread("pirinc.jpg")

# Görüntüyü griye dönüştür
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Eşik değerini belirle
threshold_value = 225

# Eşikleme işlemi uygula
_, threshold = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

# Kontürleri bul
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Pirinç sayısını yazdır
print("Pirinç sayısı:", len(contours))

# Eşiklenmiş görüntüyü göster
cv2.imshow("Eşiklenmiş Görüntü", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()