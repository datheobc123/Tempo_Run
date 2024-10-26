from ultralytics import YOLO

model = YOLO('path to your file .pt')
model.train(data="path to your yaml file"
            , epochs=82, batch = 8)




'''
-----------------Evaluation-----------------
Load a model
model = YOLO("/mlcv2/WorkingSpace/Personal/quannh/Project/Project/runs/detect/train14/weights/best.pt") 
metrics = model.val(data="/mlcv2/WorkingSpace/Personal/quannh/Project/Project/datheobc123/Tempo_Run_Q4/data_split/signboard.yaml")
print(metrics.box.maps)  # map50-95

metrics.box.map  # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps  # a list contains map50-95 of each category

-----------------Export file txt for each images-----------------

model = YOLO(model='/mlcv2/WorkingSpace/Personal/quannh/Project/Project/datheobc123/Tempo_Run_Q4/best.pt')
image_folder = '/mlcv2/WorkingSpace/Personal/quannh/Project/Project/datheobc123/Tempo_Run_Q4/eval/data/test/images'


for image_file in os.listdir(image_folder):
    if image_file.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(image_folder, image_file)

        model.predict(source=image_path, save_txt=True)
print("Completed")

'''