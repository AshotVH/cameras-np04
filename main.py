from flask import Flask, Response, stream_with_context, request, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed/<stream_id>')
def video_feed(stream_id):
    
    # internal_stream_url = f"http://137.138.155.45:1984/api/stream.mp4?src={stream_id}&mp4=flac"
    # internal_stream_url = "http://188.185.66.11:8080/"
    internal_stream_url = "https://streams-np04-slow-control.app.cern.ch/api/stream.mp4?src=cartoon-http&mp4=flac"
    
  
    def generate():
        with requests.get(internal_stream_url, stream=True) as r:
            for chunk in r.iter_content(chunk_size=4096):
                yield chunk

    return Response(stream_with_context(generate()), content_type='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
