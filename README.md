# YoloV8-on-Xview-dataset
___________________________________________________________________________
A mini guide how to set up an object detection project using YOLO, we will utilize the dataset located at C:xxxx//xViewv11. 
The training images are organized in the directory idata//train//images, while the validation images are found in idata//valid//images. 
Although the test images are not specified, they could potentially be added later in the idata//test//images directory. The dataset consists of 16 classes, 
each representing different types of vehicles and equipment commonly found on construction sites. 
The classes are: Cement Mixer, Construction Site, Container Crane, Crane Truck, Dump Truck, Engineering Vehicle, Excavator, Front Loader-Bulldozer,
Ground Grader, Haul Truck, Mobile Crane, Pickup Truck, Reach Stacker, Scraper-Tractor, Straddle Carrier, and Tower Crane. 
This structured approach will facilitate effective training and evaluation of the YOLO model for object detection tasks related to construction environments.

Documentation https://docs.ultralytics.com/datasets/detect/xview/
yaml file from official repository https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/xView.yaml

Want to Download the dataset ? Press Here : [Xview Dataset](https://storage.googleapis.com/roboflow-platform-regional-exports/Z7YmCqym5SXx6wrhRSlbpYVvk5g1/WV29gdqCVKBZjzyNDpjT/1/yolov11.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=481589474394-compute%40developer.gserviceaccount.com%2F20241029%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20241029T195109Z&X-Goog-Expires=900&X-Goog-SignedHeaders=host&X-Goog-Signature=285dece412f6a1814d009e2e9d5f2435d499497be5602ca5a739b443f23f216d09d0f8404311a61fa2955abc0cd62f9495b225647492b6c46169ac0922e93b672ac63dadc104a34f21bd7c56bcce1d571b2224f63e1cec5404e729b2e4f4e0663e4fb0eadbfc6ca05621d1b7df0a28307d9ec9d24941a5f16eff2307489d998b01263e38f11f77cb15cf43398e31d09413da1815639f099a55eb3d5f0a6ea7594186f27b5352e99232e7d2a4cdd7308324c6f9661ec77f164859d35ab5193b39924953d5313dfbef905b031a34b60a8aa582d674f1b8aa9ef74b3ac2103fa294c11984f6049784271cd541be8e8d09755f83ec179756470a1dc20a5215186d4a)
