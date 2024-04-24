import cv2

def read_video(video_path):
    print(video_path)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise FileNotFoundError("Error: Couldn't open video file")

    frames = []
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Process frame here if needed
        frames.append(frame)

    cap.release()
    return frames



def save_video(output_video_frames,output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    print(output_video_frames)
    out=cv2.VideoWriter(output_video_path,fourcc,24,(output_video_frames[0].shape[1],output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    out.release()