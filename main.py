#This library comes with the models v8 nano /large /XL https://docs.ultralytics.com/usage/python/
from ultralytics import YOLO

if __name__ == "__main__":
    # Initialize the YOLO model with a pre-trained model, like the YOLOv8 nano model
    
    model = YOLO("yolov8n.yaml")  # use yolov8n.pt, yolov8s.pt, etc., depending on your needs
    # Train the model with your dataset
    # When training a model using frameworks like YOLOv7 or YOLOv8, you can specify various parameters, 
    #including epochs and batch.  
  
    results = model.train(data="data.yaml", epochs=100)
