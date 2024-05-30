from utils import (read_video, save_video)
from trackers import PlayerTracker,BallTracker
from court_line_detector import CourtLineDetector
import cv2

def main():
    # read video
    input_video_path="input_videos/input_video.mp4"
    video_frames=read_video(input_video_path)

    # Detect Players
    player_tracker=PlayerTracker(model_path="yolov8x")
    ball_tracker=BallTracker(model_path="models\yolo5_last.pt")

    player_detections=player_tracker.detect_frames(video_frames,read_from_stub=False,
                                                   stub_path="tracker_stubs/player_detections.pkl")

    ball_detections=ball_tracker.detect_frames(video_frames,
                                               read_from_stub=False,
                                               stub_path="tracker_stubs/ball_detections.pkl")
    ball_detections=ball_tracker.interpolate_ball_position(ball_detections)

    # court line detectionn model
    court_model_path="models/keypoints_model.pth"
    court_line_detector=CourtLineDetector(model_path=court_model_path)
    court_keypoints=court_line_detector.predict(video_frames[0])

    # Draw Outputs

    ## Draw Player Bounding boxes
    output_video_frames=player_tracker.draw_bboxes(video_frames,player_detections)
    output_video_frames=ball_tracker.draw_bboxes(output_video_frames,ball_detections)

    # Draw the keypoints
    output_video_frames=court_line_detector.draw_keypoints_on_video(output_video_frames,court_keypoints)
    # Draw Frame Number on the top of the each frame for debugging purpose
    for i,frame in enumerate(output_video_frames):
        cv2.putText(frame, f"frame : {i}",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    ## save the video
    save_video(output_video_frames,"output_videos/output_video.avi")


if __name__ == "__main__":
    main()



