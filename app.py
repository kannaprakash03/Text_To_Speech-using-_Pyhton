from flask import Flask, render_template, request, make_response
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    language = request.form['lang']

    if not text:
        return "Please enter some text."

    tts = gTTS(text=text, lang=language)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    response = make_response(fp.read())
    response.headers['Content-Type'] = 'audio/mp3'
    return response

if __name__ == '__main__':
    app.run(debug=True)
