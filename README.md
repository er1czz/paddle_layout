# paddle_layout_gradio
document layout analysis with paddle OCR and gradio UI
- reference: https://github.com/PaddlePaddle/PaddleOCR/tree/release/2.6/ppstructure/layout#32-Install-paddledetection
- run [demo.py](https://github.com/er1czz/paddle_layout/blob/main/demo.py)
### key note
- OS: Windows 10 Pro
- create conda virtual env under python 3.8
- use the pretrained_model ```picodet_lcnet_x1_0_fgd_layout_infer``` for inference
- layout analysis is through **command line** (example below), which is executed via python subprocess.
  ```
  python deploy/python/infer.py \
    --model_dir=pretrained_model/picodet_lcnet_x1_0_fgd_layout_infer/ \
    --image_file=docs/images/layout.jpg \
    --device=CPU
  ```
- UI visualization is achieved by gradio
- gradio will read image file path with backslash ```\``` as the seperator, which need to be converted into forward slash ```/```
<p align="center"><img src="https://github.com/er1czz/paddle_layout/blob/main/paddleOCR_gradio_demo.JPG" style = "border:10px solid white"></p> 

### code of [demo.py](https://github.com/er1czz/paddle_layout/blob/main/demo.py) 
```
import gradio as gr
import paddle
import cv2
import subprocess
import os

def main_fn(image_filepath):

    # extract the file name from full path
    image_name = os.path.basename(image_filepath)

    # convert to string and replace the backslash with forward slash 
    image_filepath = str(image_filepath).replace(os.sep, '/')

    model_dir = 'pretrained_model/picodet_lcnet_x1_0_fgd_layout_infer'
    device='cpu'
    cmd_str = f"python deploy/python/infer.py --model_dir={model_dir} --image_file={image_filepath} --device={device}"
    cmd_ls = cmd_str.split(' ')

    # this command will start inference and output an annotated image in the default dir 'output'
    p1 = subprocess.Popen(cmd_ls, shell=True)

    # wait for p1 to be finished before proceed
    p1.wait() 

    # read the annotated image from p1 output
    output_img = cv2.imread(os.path.join('output', image_name))
  
    return image_name, output_img


#inputs =  [gr.Text(label='Type image full name here'), gr.Image(type='filepath', label='Drage input image here')]
inputs =  [gr.Image(type='filepath', label='Drage input image here')]
outputs = [gr.Text(label='Image name'), gr.Image(label='Image output with annotation')]
demo = gr.Interface(fn=main_fn, inputs=inputs, outputs=outputs)

if __name__ == "__main__":
    demo.launch(share=True)
```

