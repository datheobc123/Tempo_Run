import os
import shutil

data_dir = '/path/to/your/data'
label_data_dir = 'path/to/your/label'

train_images_dir = 'path/to/your/images_train'
train_labels_dir = 'path/to/your/label_train'

val_images_dir = 'path/to/your/images_val'
val_labels_dir = 'path/to/your/labels_val'

test_images_dir = 'path/to/your/images_test'
test_labels_dir = 'path/to/your/labels_test'

os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)
os.makedirs(test_images_dir, exist_ok=True)
os.makedirs(test_labels_dir, exist_ok=True)

# images_file = sorted(os.listdir(data_dir))
# labels_file = sorted(os.listdir(label_data_dir))
# total_files = min(len(images_file), len(label_files))

# for i in range(min(100, total_files)):
#     shutil.copy(os.path.join(data_dir, image_files[i]), train_images_dir)
#     shutil.copy(os.path.join(label_data_dir, label_files[i]), train_labels_dir)
