#This library comes with the models v8 nano /large /XL https://docs.ultralytics.com/usage/python/
    # Train the model with your dataset
    # When training a model using frameworks like YOLOv7 or YOLOv8, you can specify various parameters, 
    #including epochs and batch.  
                                         # Parameters
                    #data: Path to the YAML file containing the dataset configuration.
                    #epochs: Number of training epochs (iterations over the entire dataset).
                    #batch: Number of samples processed before the model's internal parameters are updated.

                    #batch : 
                           # Memory Management: Larger batch sizes require more GPU memory, while smaller sizes use less but may take longer to train.
                           # Large Batch Sizes: Can lead to faster training but might generalize poorly.
                           # Small Batch Sizes: Introduce noise, which can help in escaping local minima but may result in unstable training
                           # Learning Dynamics: Finding the right balance is key; experimentation is often necessary to achieve optimal performance.
                           # For 6GB VRAM (e.g., NVIDIA RTX 2060)  Start with: 8 or 16 and increase to 32 if your system isnt lagging
                           # For 8GB VRAM (e.g., NVIDIA RTX 3060): Start with: 16 and increase to 32 if your system isnt lagging
                           # For 8GB VRAM (e.g., NVIDIA RTX 3060): Start with: 32 and increase to 64 if your system isnt lagging or even 128 (Multiple of Powers of 2)
                           # example results = model.train(data="data.yaml", epochs=100, batch_size = 32)
from ultralytics import YOLO
                           # If your script contains long-running processes (like training a model) and you import that script in another module,
                           # all the code outside of the if __name__ == "__main__": block will execute immediately. 
                           # This can lead to unexpected behavior, including freezing, if the imported script starts training the model without your intention. Thats why I use{__name__ == "__main__"}
if __name__ == "__main__":
    # Initialize the YOLO model with a pre-trained model, like the YOLOv8 nano model
    
    model = YOLO("yolov8n.yaml")  # use yolov8n.pt, yolov8s.pt, etc., depending on your needs

    results = model.train(data="data.yaml", epochs=100) # I dont use any batch size, it uses default for mine GPU



# happy coding
