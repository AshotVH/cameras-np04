from flask import Flask, render_template
import os


app = Flask(__name__)

STREAM_SOURCE_1 = os.environ["STREAM_SOURCE_1"]
STREAM_SOURCE_2 = os.environ["STREAM_SOURCE_2"]
STREAM_SOURCE_3 = os.environ["STREAM_SOURCE_3"]
STREAM_SOURCE_4 = os.environ["STREAM_SOURCE_4"]
STREAM_SOURCE_5 = os.environ["STREAM_SOURCE_5"]
STREAM_SOURCE_6 = os.environ["STREAM_SOURCE_6"]
STREAM_SOURCE_7 = os.environ["STREAM_SOURCE_7"]
STREAM_SOURCE_8 = os.environ["STREAM_SOURCE_8"]


@app.route('/')
def root():
    return render_template('index.html',cam401=STREAM_SOURCE_1,cam404=STREAM_SOURCE_2,cam406=STREAM_SOURCE_3,cam407=STREAM_SOURCE_4,cam408=STREAM_SOURCE_5,cam409=STREAM_SOURCE_6,cam410=STREAM_SOURCE_7,cam411=STREAM_SOURCE_8)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
