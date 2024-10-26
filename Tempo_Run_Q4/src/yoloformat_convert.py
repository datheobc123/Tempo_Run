import json
import os
import cv2
import numpy as np

def convert_polygon_to_yolo(points, img_width, img_height):
    # Chuyển đổi tọa độ từ phần trăm sang pixel
    points_pixel = np.zeros_like(points, dtype=np.float32)
    points_pixel[:, 0] = (points[:, 0] / 100 * img_width)
    points_pixel[:, 1] = (points[:, 1] / 100 * img_height)

    # Tính toán các tọa độ cho bounding box
    x_min = np.min(points_pixel[:, 0])
    x_max = np.max(points_pixel[:, 0])
    y_min = np.min(points_pixel[:, 1])
    y_max = np.max(points_pixel[:, 1])

    # Tính toán center_x, center_y, width, height theo định dạng YOLO --> lấy tọa độ trung tâm
    center_x = (x_min + x_max) / 2 / img_width
    center_y = (y_min + y_max) / 2 / img_height
    width = (x_max - x_min) / img_width
    height = (y_max - y_min) / img_height

    return center_x, center_y, width, height, points_pixel

# Đường dẫn đến file JSON
json_file_path = '/mlcv2/WorkingSpace/Personal/quannh/Project/Project/datheobc123/Tempo_Run_Q4/project-17-at-2024-10-02-10-42-f81936e5.json'
# Thư mục chứa hình ảnh gốc
images_dir = '/mlcv2/WorkingSpace/Personal/quannh/Project/Project/datheobc123/Tempo_Run_Q4/data'
# Thư mục lưu ảnh đã gán nhãn
output_images_dir = '/mlcv2/WorkingSpace/Personal/quannh/Project/Project/datheobc123/Tempo_Run_Q4/labeled_images'
# Thư mục lưu file .txt
output_txt_dir = '/mlcv2/WorkingSpace/Personal/quannh/Project/Project/datheobc123/Tempo_Run_Q4/labeled_txt'
os.makedirs(output_images_dir, exist_ok=True)
os.makedirs(output_txt_dir, exist_ok=True)

# Đọc file JSON
with open(json_file_path, 'r') as f:
    annotations = json.load(f)

for annotation in annotations:
    # Kiểm tra xem có trường 'ocr' và 'poly' trong annotation hay không
    if 'ocr' not in annotation or 'poly' not in annotation:
        print(f"Missing 'ocr' or 'poly' in annotation: {annotation}")
        continue

    img_url = annotation["ocr"]
    img_id = os.path.basename(img_url)  # Lấy tên file hình ảnh
    img_path = os.path.join(images_dir, img_id)  # Đường dẫn đầy đủ đến hình ảnh

    # Đọc hình ảnh để lấy kích thước
    image = cv2.imread(img_path)
    if image is None:
        print(f"Image {img_path} not found, Skip.")
        continue
    
    height, width, _ = image.shape

    # Chuyển đổi từng polygon thành bounding box
    with open(os.path.join(output_txt_dir, img_id.replace('.jpg', '.txt')), 'w') as txt_file:
        for poly in annotation['poly']:
            # Kiểm tra xem poly có chứa 'points' hay không
            if 'points' not in poly:
                print(f"Missing 'points' in poly: {poly}")
                continue
            
            points = poly['points']
            points = np.array(points)  # Đảm bảo points là numpy array
            center_x, center_y, bbox_width, bbox_height, points_pixel = convert_polygon_to_yolo(points, width, height)

            # class_id = 0 cho lớp "signboard"
            class_id = 0  
            txt_file.write(f"{class_id} {center_x} {center_y} {bbox_width} {bbox_height}\n")

            # Vẽ polygon lên hình ảnh
            points_pixel = points_pixel.reshape((-1, 1, 2)).astype(np.int32)  # Reshape để vẽ
            cv2.polylines(image, [points_pixel], isClosed=True, color=(0, 255, 0), thickness=2)

    # Lưu hình ảnh đã gán nhãn
    output_image_path = os.path.join(output_images_dir, img_id)
    cv2.imwrite(output_image_path, image)

print("Labeling completed!")
