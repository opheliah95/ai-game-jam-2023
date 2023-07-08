import gradio as gr
from pipeline import *


demo = gr.Interface(fn=chat, inputs="text", outputs="text")
    
demo.launch()   