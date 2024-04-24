from ultralytics import YOLO

class PlayerTracker:
    def __init__(self,model_path):
        self.model=YOLO(model_path)

    def detect_frame(self,frame):
        results=self.model.track(frame,persist=True)[0]
        id_name_dict=results.names

        player_dict={}
        for box in results.boxes:
            track_id = int

