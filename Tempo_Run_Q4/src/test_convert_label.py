import json
import os

# Đường dẫn đến tệp JSON của bạn
json_file_path = '/mlcv2/WorkingSpace/Personal/quannh/Project/Project/datheobc123/Tempo_Run_Q4/Label_studio.json'
# Thư mục chứa hình ảnh
images_dir = '/mlcv2/WorkingSpace/Personal/quannh/Project/Project/datheobc123/Tempo_Run_Q4/data'  # Thay thế bằng đường dẫn thực tế
# Thư mục để lưu tệp nhãn
labels_dir = '/mlcv2/WorkingSpace/Personal/quannh/Project/Project/datheobc123/Tempo_Run_Q4/data_split/labels/'
os.makedirs(labels_dir, exist_ok=True)

with open(json_file_path, 'r') as f:
    annotations = json.load(f)

for annotation in annotations:
    # Kiểm tra nếu có 'poly'
    if 'poly' in annotation and len(annotation['poly']) > 0:
        # Lấy đường dẫn hình ảnh
        img_name = os.path.basename(annotation['ocr'])
        label_file_path = os.path.join(labels_dir, img_name.replace('.jpg', '.txt'))

        # Lấy các điểm trong polygon
        points = annotation['poly'][0]['points']
        
        # Tính toán các tọa độ chuẩn hóa cho YOLO
        width = annotation['poly'][0]['original_width']
        height = annotation['poly'][0]['original_height']
        
        # Ghi nhãn vào tệp
        with open(label_file_path, 'w') as label_file:
            for point in points:
                x_center = point[0] / width
                y_center = point[1] / height
                label_file.write(f"signboard {x_center} {y_center} 0.1 0.1\n")  # Kích thước được gán tạm thời

print("Chuyển đổi hoàn tất!")
