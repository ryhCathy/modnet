import requests
from IPython.display import display
from PIL import Image
import io
from bg_remove import BGRemove

# Sending the request to the API
url = "http://183.179.173.18:8083/generate_for_attachment"

def generateImg(prompt, path_to_save_image):
    payload = {
        'input1': prompt,  # Example description in Chinese: 'patriotic cat'
        'input2': 'realistic',
        'input3': '1024x1024'
    }
    response = requests.post(url, data=payload)

    # Assuming the response is in binary format, save and display the image
    if response.ok:
        # Convert binary data to an image
        image_data = io.BytesIO(response.content)
        image = Image.open(image_data)
        # Display the image
        display(image)

        # Save the image to local filesystem
        # Specify the path and filename where you want to save the image
        image.save(path_to_save_image, format='PNG')
        
        print(f"Image successfully saved to {path_to_save_image}")
    else:
        print("Error fetching the image:", response.status_code)


def replaceOrRemoveBg(image_path, background_path='', output_path='./output'):
    bg_remover = BGRemove('pretrained/modnet_photographic_portrait_matting.ckpt')

    try:
        if background_path:
            bg_remover.image(image_path, background=True, output=output_path, background_path=background_path)
        else:
            bg_remover.image(image_path, background=False, output=output_path)
    except Exception as Err:
        print("Erro happend {}".format(Err))


def replaceGenImgBg(prompt='城市小路背景', image_path='./test.jpeg', background_path="./bg1.png", output_dir='./output'):
    generateImg(prompt, path_to_save_image=background_path)
    replaceOrRemoveBg(image_path, background_path=background_path, output_path=output_dir)



if __name__ == '__main__':
    # for test purpose
    replaceGenImgBg(prompt='未来世界小路背景', image_path='./test.jpeg', background_path="./bg1.png")



