from ultralytics import YOLO
import zipfile
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

model = YOLO('yolov8n.pt')

# with zipfile.ZipFile('./test01.v1i.yolov8.zip') as target_file:
#     target_file.extractall('test01.v1i.yolov8')

model.train(data='test01.v1i.yolov8/data.yaml', epochs=3)

model.predict(source='test01.v1i.yolov8/test/images', save=True)
