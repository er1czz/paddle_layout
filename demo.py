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

def test_fn(image_file):
    return image_file

#inputs =  [gr.Text(label='Type image full name here'), gr.Image(type='filepath', label='Drage input image here')]
inputs =  [gr.Image(type='filepath', label='Drage input image here')]
outputs = [gr.Text(label='Image name'), gr.Image(label='Image output with annotation')]
demo = gr.Interface(fn=main_fn, inputs=inputs, outputs=outputs)

if __name__ == "__main__":
    demo.launch(share=True)