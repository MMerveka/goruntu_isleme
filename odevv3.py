
import cv2
import numpy as np

image = cv2.imread("pirinc.jpg")


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
