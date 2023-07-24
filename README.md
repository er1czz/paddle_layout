# paddle_layout
document layout analysis with paddle ocr and gradio UI

- reference: https://github.com/PaddlePaddle/PaddleOCR/tree/release/2.6/ppstructure/layout#32-Install-paddledetection
- use the pretrained_model ```picodet_lcnet_x1_0_fgd_layout_infer``` for inference
- main function is execuated through subprocess
  ```
  python deploy/python/infer.py \
    --model_dir=output_inference/picodet_lcnet_x1_0_layout/ \
    --image_file=docs/images/layout.jpg \
    --device=CPU
  ```
- UI visualization is achieved through gradio
