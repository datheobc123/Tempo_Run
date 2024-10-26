import cv2
import numpy as np

# Đường dẫn đến hình ảnh
image_path = '/mlcv2/WorkingSpace/Personal/quannh/Project/Project/datheobc123/Tempo_Run_Q4/IMG_0002.jpg'
image = cv2.imread(image_path)

# # Kiểm tra nếu hình ảnh được đọc thành công
# if image is None:
#     print("Error: Unable to load image.")
#     exit()

# Lấy kích thước của hình ảnh
height, width, _ = image.shape

# Tọa độ các điểm của BBox dưới dạng phần trăm
points = np.array([
    [97.6513098464318, 17.479674796747968],
    [99.3676603432701, 88.34688346883469],
    [1.1743450767841013, 89.83739837398373],
    [3.523035230352303, 17.208672086720867]
], dtype=np.float32)

# Chuyển đổi tọa độ từ phần trăm sang pixel
points_pixel = np.zeros_like(points, dtype=np.int32)
points_pixel[:, 0] = (points[:, 0] / 100 * width).astype(np.int32)
points_pixel[:, 1] = (points[:, 1] / 100 * height).astype(np.int32)

# Reshape lại để phù hợp với định dạng yêu cầu của polylines
points_pixel = points_pixel.reshape((-1, 1, 2))

# Nối các điểm lại thành một đa giác
cv2.polylines(image, [points_pixel], isClosed=True, color=(0, 255, 0), thickness=2)  # Đóng đa giác

# Vẽ các điểm của đa giác
# for point in points_pixel:
#     cv2.circle(image, tuple(point[0]), 5, (255, 0, 0), -1)


output_path = 'output_image_polygon.png'
cv2.imwrite(output_path, image)

print(f"Output image saved at: {output_path}")
