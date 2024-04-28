from flask import Flask, Response
import cv2
from queue import Queue
from ultralytics import YOLO
import numpy as np

app = Flask(__name__)
model = YOLO('./models/best.pt')
# The maximum number of frames to store in the buffer
BUFFER_SIZE = 60

def detect(img):
    results = model(img)
    results_list = []
    for result in results:
        if len(result.boxes.cls)>0:
            for i in range(len(result.boxes.cls)):
                label_id = int(result.boxes.cls[i].item())
                label = result.names[label_id]
                confidence = result.boxes.conf[i].item()
                position = result.boxes.xyxy[i].tolist()
                print(label, confidence, position)
                result_data = {'label': label, 'confidence': confidence, 'position': position}
                results_list.append(result_data)
    return results_list

@app.route('/')
def video_feed():
    # Open the video file
    cap = cv2.VideoCapture('https://wzmedia.dot.ca.gov/D5/101atBetteraviaRd.stream/playlist.m3u8')

    # The buffer for storing frames
    buffer = Queue(maxsize=BUFFER_SIZE)
    
    def generate():
        while True:
            ret, frame = cap.read()
            if ret:
                frame = np.array(frame)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                results = detect(frame)
                # Draw rectangle
                for result in results:
                    position = [int(p) for p in result['position']]
                    cv2.rectangle(frame, (position[0], position[1]), (position[2], position[3]), (0, 255, 0), 2)
                    cv2.putText(frame, result['label'], (position[0], position[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

                # Encode the frame as JPEG
                ret, jpeg = cv2.imencode('.jpg', frame)
                if ret:
                    # Add the frame to the buffer
                    buffer.put(jpeg.tobytes())

                # If the buffer is full, yield the oldest frame
                if buffer.full():
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + buffer.get() + b'\r\n\r\n')

    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='localhost', port='5000')


