from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from TamilBraille import tamil_to_braille, braille_to_tamil, tamil_OCR, tamil_TTS

app = Flask(__name__)

# Define the allowed file extensions
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

# Define the upload folder and ensure it exists
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/TamiltoBraille')
def TtoB():
    return render_template('TtoB.html')

@app.route('/BrailletoTamil')
def BtoT():
    return render_template('BtoT.html')

@app.route('/TexttoSpeech')
def TtoS():
    return render_template('TtoS.html')

@app.route('/TamiltoBraille', methods=['GET', 'POST'])
def conv1():
    if request.method == 'POST':
        text = request.form.get('text')
        # file = request.files.get('file')
        file = request.files['file']
                  
        if text:
            # Do something with the text input
            result = tamil_to_braille(text)
            return render_template('ans.html', result=result)
        elif file:
            # Do something with the file upload
            file.save('uploads/' + secure_filename(file.filename))
            result1 = tamil_OCR(file.filename)
            result = tamil_to_braille(result1)
            return render_template('ans.html', result=result)
        else:
            # Neither text nor file was submitted
            return "Please enter some text or upload a file."
    else:
        return render_template('TtoB.html')
    
@app.route('/BrailletoTamil', methods=['GET', 'POST'])
def conv2():
    if request.method == 'POST':
        text1 = request.form.get('text')
        if text1:
            # Do something with the text input
            result = braille_to_tamil(text1)
            return render_template('ans.html', result=result)
        else:
            # Neither text nor file was submitted
            return "Please enter some text or upload a file."
    else:
        return render_template('BtoT.html')
    
@app.route('/TexttoSpeech', methods=['GET', 'POST'])
def conv3():
    if request.method == 'POST':
        text = request.form.get('text')
        file2 = request.files['file']
        if text:
            # Do something with the text input
            tamil_TTS(text)
            return render_template('TtoS.html')
        elif file2:
            # Do something with the file upload
            file2.save('uploads/' + secure_filename(file2.filename))
            result = tamil_OCR(file2.filename)
            tamil_TTS(result)
            return render_template('TtoS.html')
        else:
            # Neither text nor file was submitted
            return "Please enter some text or upload a file."
    else:
        return render_template('TtoS.html')

if __name__ == '__main__':
    app.run()
