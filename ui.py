import gradio as gr
from pipeline import *
import time

story = []
with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Story Writer
        Type your input and we write a story together
        """
    )
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    def user(user_message, history):
        return "", history + [[user_message, None]]
    
    def respond(input, history):
        bot_message = chat(input)
        story.append(bot_message) # combine all previous inputs
        history[-1][1] = ""
        for character in bot_message:
            history[-1][1] += character
            time.sleep(0.05)
            yield history
        time.sleep(0.05)
        return "", history
    msg.submit(user, chatbot, chatbot, queue=False).then(respond, chatbot, chatbot)
    clear.click(lambda: None, None, chatbot, queue=False)

with gr.Accordion("Story so far"):
        result = '\n'.join(story)
        gr.Markdown(result)
demo.queue()
demo.launch()   