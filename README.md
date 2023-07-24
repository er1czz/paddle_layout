# paddle_layout_gradio
document layout analysis with paddle OCR and gradio UI
- reference: https://github.com/PaddlePaddle/PaddleOCR/tree/release/2.6/ppstructure/layout#32-Install-paddledetection
- run [demo.py](https://github.com/er1czz/paddle_layout/blob/main/demo.py)
### key note
- OS: Windows 10 Pro
- create conda virtual env under python 3.8
- use the pretrained_model ```picodet_lcnet_x1_0_fgd_layout_infer``` for inference
- layout analysis is through command line (example below), which is executed via python subprocess.
  ```
  python deploy/python/infer.py \
    --model_dir=pretrained_model/picodet_lcnet_x1_0_fgd_layout_infer/ \
    --image_file=docs/images/layout.jpg \
    --device=CPU
  ```
- UI visualization is achieved by gradio
- gradio will read image file path with backslash ```\``` as the seperator, which need to be converted into forward slash ```/```
<p align="center"><img src="https://github.com/er1czz/paddle_layout/blob/main/paddleOCR_gradio_demo.JPG" style = "border:10px solid white"></p>  

