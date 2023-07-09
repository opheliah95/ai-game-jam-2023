import gradio as gr
from chat import *
from image_gen import *
import time

story = []
bot_message = ''

def respond(message, chat_history):
        bot_message=chat(message)
        chat_history.append((message, bot_message))
        story.append(bot_message)  # Combine all previous inputs
        time.sleep(0.05)
        return "", chat_history

def update_image(message, image):
    processed_image = query_image(message)
    print('image wip: ', message)
    image.update(processed_image)

def generate_null_image():
    # Generate a blank image with the specified width
    image = Image.new("RGB", (512, 512), (255, 255, 255))
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
            null_image = generate_null_image()
            image = gr.Image(value=null_image,
                             height='512', 
                             width='512', 
                             label='image generated',
                             show_label=True)
            
    with gr.Accordion("Story so far"):
        result = '\n'.join(story)
        print('the story is: ', result)
        gr.Markdown(result)
        
    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    image.change(update_image, [msg, image])

demo.launch()   