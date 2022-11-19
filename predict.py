import os

from bg_remove import BGRemove
from cog import BasePredictor, Input, Path


class Predictor(BasePredictor):
    def setup(self):
        print("setup")
        self.bgremover = BGRemove("/modnet_webcam_portrait_matting.ckpt")

    def predict(self, 
        image: Path = Input(description="input image"),
        ) -> Path:
        print("running bgremover on image", str(image))
        self.bgremover.image(str(image), background=False, output='/outputs')
        os.system("ls -l /outputs")
        os.system("mv /outputs/*.png /outputs/output.png")
        return Path("/outputs/output.png")

