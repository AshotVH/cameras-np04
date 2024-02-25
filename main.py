from flask import Flask, Response, stream_with_context, request, render_template,redirect, url_for, session, flash
import requests
import os
import time
app = Flask(__name__)

STREAM_SOURCE = os.environ["STREAM_SOURCE"]
PASSWORD = os.environ.get("PASSWORD")
app.secret_key = os.environ.get("SECRET_KEY", "secret")

def is_logged_in():
    return session.get("logged_in")

@app.route('/')
def root():
    if is_logged_in():
        return redirect(url_for('index', cam='cam401'))
    else:
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index', cam='cam401'))
        else:
            time.sleep(1)
            flash('Incorrect password', 'error')
            return redirect(url_for('login'))
    else:
        if is_logged_in():
            return redirect(url_for('index', cam='cam401'))
        else:
            return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('root'))


@app.route('/<cam>')
def index(cam):
    if is_logged_in():
        return render_template('index.html', cam=cam)
    else:
        return redirect(url_for('root'))



@app.route('/video_feed/<stream_id>')
def video_feed(stream_id):
    if is_logged_in():
        internal_stream_url = f"http://{STREAM_SOURCE}/api/stream.mp4?src=video1&mp4=flac"
        def generate():
            with requests.get(internal_stream_url, stream=True) as r:
                for chunk in r.iter_content(chunk_size=4096):
                    yield chunk
        return Response(stream_with_context(generate()), content_type='multipart/x-mixed-replace; boundary=frame')
    else:
        return "Unauthorized", 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
