from cog import BasePredictor, Input, Path


class Predictor(BasePredictor):
    def setup(self):
        print("setup")


    def predict(self, 
        image: Path = Input(description="input image"),
        task_type: str = Input(
            description='image restoration task type',
            default='Real-World Image Super-Resolution',
            choices=['Real-World Image Super-Resolution', 'Grayscale Image Denoising', 'Color Image Denoising','JPEG Compression Artifact Reduction']        
        ),  
        scale_factor: int = Input(
            description="updscale factor for RealSR. 2 or 4 are allowed",
            default=4),
        jpeg: int = Input(
            description="scale factor, activated for JPEG Compression Artifact Reduction. ",
            default=40),
        noise: int = Input(
             description="noise level, activated for Grayscale Image Denoising and Color Image Denoising.",
             default=15)
        ) -> Path:

        
        return None

