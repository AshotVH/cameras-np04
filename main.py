from flask import Flask, Response, stream_with_context, request, render_template,redirect, url_for
import requests
import os
app = Flask(__name__)

STREAM_SOURCE = os.environ["STREAM_SOURCE"]

@app.route('/')
def root():
    return redirect(url_for('index', cam='cam401'))

@app.route('/<cam>')
def index(cam):
    return render_template('index.html', cam=cam)


@app.route('/video_feed/<stream_id>')
def video_feed(stream_id):
    
    internal_stream_url = f"http://{STREAM_SOURCE}/api/stream.mp4?src=video1&mp4=flac"
    
    def generate():
        with requests.get(internal_stream_url, stream=True) as r:
            for chunk in r.iter_content(chunk_size=4096):
                yield chunk

    return Response(stream_with_context(generate()), content_type='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
