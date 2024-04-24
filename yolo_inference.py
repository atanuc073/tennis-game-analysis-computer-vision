from ultralytics import YOLO

# model=YOLO("models\yolo5_last.pt")
model=YOLO("yolov8x")

result= model.track("input_videos/input2.png",save=True)[0]
print(result.boxes)

