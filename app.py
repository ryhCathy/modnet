from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
import os
from demo import replaceGenImgBg

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploaded_images'
app.config['OUTPUT_FOLDER'] = './output'
app.config['MAX_CONTENT_PATH'] = 16 * 1024 * 1024  # 16 MB Max for upload

## use pycharm to run as python system path (__init__) not well configured in this structure
@app.route('/replace-background', methods=['POST'])
def replace_background():
    if 'file' not in request.files:
        print('file1')
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        print('file2')
        return "No selected file", 400

    filename = secure_filename(file.filename)
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(input_path)

    # Assuming the background replacement logic is in replace_gen_img_bg
    background_path = os.path.join(app.config['UPLOAD_FOLDER'], "bg1.png")
    im_name = filename.split('/')[-1]
    name = '.'.join(im_name.split('.')[:-1]) + '.png'
    print(name)

    # New: Fetching text parameter from form-data
    prompt_text = request.form.get('background_prompt', '乡村小路背景')

    replaceGenImgBg(prompt_text, image_path=input_path, background_path=background_path, output_dir=app.config['OUTPUT_FOLDER'])
    output_path = os.path.join(app.config['OUTPUT_FOLDER'], name)
    print(output_path)

    return send_file(output_path, mimetype='image/png')



if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(host='0.0.0.0', port=8085, debug=True)
