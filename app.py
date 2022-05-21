from flask import Flask,render_template,Response
import cv2
from plot_object_detection_saved_model import load_image_into_numpy_array
app=Flask(__name__)

camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/video_run', methods = ['post'])
def video():
    return Response(load_image_into_numpy_array(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)