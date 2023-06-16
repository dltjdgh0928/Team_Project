from ultralytics import YOLO
import torch
import os
import multiprocessing
import warnings
warnings.filterwarnings('ignore')

def main():
    torch.cuda.is_available()
    os.environ['KMP_DUPLICATE_LIB_OK']='True'

    # model = YOLO('yolov8n.pt')
    # model.train(data='traffic_data/data.yaml', epochs=1, patience=5, batch=16, seed=42)
    
    # 가중치로 돌리는 코드
    model = YOLO("./runs/detect/train2/weights/best.pt")
    
    result = model.predict(source='traffic_data/test/images', save=False)
    # print(result[0])
    print(len(result))
    
    for i in range(len(result)):
        
        print(result[i].boxes)
        print(result[i].boxes.xyxy)
        print(result[i].boxes.cls)
        
        cls_list = result[i].boxes.cls.tolist()
        print(type(cls_list))
        indices = {}

        for index, value in enumerate(cls_list):
            if value in [0, 1, 2] and value not in indices:
                indices[value] = index

        print(indices)
        print(indices[2])
        print(indices[1])
        new_dict = {key: value for index, (key, value) in enumerate(indices.items()) if index < 2}



        if 2 in result[i].boxes.cls:
            if result[i].boxes.xyxyn[indices[2]][3] > 0.8\
                and 0.3 < result[i].boxes.xywhn[indices[2]][0] < 0.7\
                and result[i].boxes.xywhn[indices[2]][2] > 0.4:
                if 1 in result[i].boxes.cls and 1 in new_dict:
                    print('빨간불입니다')
                    
                elif 0 in result[i].boxes.cls and 0 in new_dict:
                    print('초록불입니다')
                    
                else:
                    print('신호등이없으니 조심하세요')
                
            else:
                print('멀리 떨어져있는 횡단보도')
                
        
        
        
        
        
        
        
        
        # crosswalk_indices = []

        # for index, value in enumerate(result[i].boxes.cls):
        #     if value == 2:
        #         crosswalk_indices.append(index)

        # if 1 in result[i].boxes.cls:
        #     print(f'{i+1}번째 사진 빨간불(위험)감지')
        #     for j in range(len(crosswalk_indices)):
        #         print(f'{j+1} 번째 횡단보도 아래좌표 위치{result[i].boxes.xyxy[crosswalk_indices[j]][3]}')

    
            
if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()