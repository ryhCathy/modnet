# Revised MODNet Background Image Replacement

## Application

A deep learning approach to remove background and adding new background image. For full details of [MODNet](https://github.com/pollinations/modnet), check [reference.md](reference.md).

- Remove background from **images,videos & live webcam**
- Adding new background to those **images,videos & webcam footage**


### Demo

<table>
<tr align="center">
<td><b>Before removing the background</b></td>
<td><b>After replacing the background with new image</b></td>
</tr>
<tr align="center">
<td><img src="test.jpeg" alt="Male.jpg" width="460" height="500"/></td>
<td><img src="output/test.png" alt="Male.png" width="460" height="500"/></td>
<table>


## Installation

### Python Version

- Python == 3.9

### Virtual Environment

### Library Installation

- Library Install
  - `pip install --upgrade pip`
  - `pip install --upgrade setuptools`
  - `pip install -r requirements.txt`
  - To run in **web interface**
    - `pip install -r web_requirements.txt`

### Pretrained Weights Download
- [Weights Detail](pretrained/README.md)


## Inference

### Image

#### Single image

It will generate the output file in **output/** folder

- `python inference.py --image image_path` **[Without background image]**
- `python inference.py --image image_path --background True` **[With background image]**
- `python inference.py --image image_path --background True --background_path background_img_path` **[With background image and path]**
- Example:
  - `python inference.py --image assets/sample_image/female.jpeg`
  - `python inference.py --image assets/sample_image/male.jpeg --background True`
  - `python inference.py --image test.jpeg --background True --background_path assets/background/bg2.jpg`



### 替换prompt-based背景图像的接口（POST）

## 接口地址
`http://183.179.173.18:5000/replace-background` (app.py Flask app as backend)

## 请求方法
`POST`

## 请求参数
### Body
- `bg_prompt`: 字符串，描述希望生成的背景图片风格
- `file_path`: 字符串，被替换背景的图片路径

## 请求示例
```python
import requests
from IPython.display import display
from PIL import Image
import io

# URL of the Flask app
url = 'http://183.179.173.18:5000/replace-background'
file_path = './modnet/test.jpeg'
bg_prompt = '夜间小路背景'

with open(file_path, 'rb') as file:
    files = {'file': (os.path.basename(file_path), file, 'image/jpeg')}   # 记得根据上传图片类型，更换MIME参数
    response = requests.post(url, files=files, data={'background_prompt': prompt})
        
    if response.status_code == 200:
        # Display image directly in Jupyter Notebook
        image_bytes = io.BytesIO(response.content)
        img = Image.open(image_bytes)
        display(img)
    else:
        print("Failed to process image:", response.text)


```
