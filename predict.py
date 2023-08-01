from PIL import ImageTk, Image
from detector import detectCopyRotationMove, readImage, featureExtraction
import cv2
import matplotlib.pyplot as plt

# Đường dẫn đến file ảnh
image_path = r"./image test/test10.png"

# Đọc ảnh
image =readImage(image_path)
# image = cv2.imread(image_path)
# im1 = featureExtraction(image)
# Phát hiện copy-move forgery
forgery_detected = detectCopyRotationMove(image)

# Hiển thị ảnh gốc
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Ảnh gốc ")
plt.axis("off")

# Hiển thị ảnh phát hiện ra (nếu có)
if forgery_detected:
    forgery_image = cv2.imread("results.png")
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(forgery_image, cv2.COLOR_BGR2RGB))
    plt.title("Ảnh đã được chỉnh sửa ")
    plt.axis("off")
else:
    plt.subplot(1,2,2)
    plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title("Ảnh không được chỉnh sửa")
    plt.axis("off")

plt.show()