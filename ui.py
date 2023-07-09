import gradio as gr
from chat import *
from image_gen import *
import time

story = []
bot_message = ''

def respond(message, chat_history):
        image_button.interactive = True
        bot_message=chat(message)
        chat_history.append((message, bot_message))
        story.append(bot_message)  # Combine all previous inputs
        time.sleep(0.05)
        image_button.interactive = False
        return "", chat_history


def generate_null_image():
    # Generate a blank image with the specified width
    image = Image.new("RGB", (300, 300), (255, 255, 255))
    return image

with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Story Writer
        Type your input and we write a story together
        """
    )
    with gr.Row():
        with gr.Column(scale=1, min_width=600):
            chatbot = gr.Chatbot()
            msg = gr.Textbox()
            clear = gr.Button("Clear")
            
        with gr.Column(scale=2, min_width=600):
            gr.Markdown(
                """
                # Image generator
                Your text will be generated into an image every time
                """)
            image_button = gr.Button("Generate")
            null_image = generate_null_image()
            image_output = gr.Image(value=null_image,
                             height='512', 
                             width='512', 
                             label='image generated',
                             show_label=True)
            
    with gr.Accordion("Story so far"):
        result = '\n'.join(story)
        print('the story is: ', result)
        gr.Markdown(result)
        
    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    image_button.click(query_image, inputs=[msg], outputs=image_output)

demo.launch(share=True)   