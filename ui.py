import gradio as gr
from pipeline import *
import time

story = []
def respond(message, chat_history):
        bot_message =chat(message)
        chat_history.append((message, bot_message))
        story.append(bot_message)  # Combine all previous inputs
        time.sleep(0.05)
        return "", chat_history


# def user(user_message, history):
#         return "", history + [[user_message, None]]

# def respond(input, history):
#     bot_message = chat(input)
#     story.append(bot_message)  # Combine all previous inputs
#     history[-1][1] = ""
#     for character in bot_message:
#         history[-1][1] += character
#         time.sleep(0.05)
#         yield history
#     time.sleep(0.05)
#     return "", history

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
    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    # msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(respond, [msg,chatbot], chatbot)
    # clear.click(lambda: None, None, chatbot, queue=False)

with gr.Accordion("Story so far"):
        result = '\n'.join(story)
        print(result)
        gr.Markdown(result)
# demo.queue()
demo.launch()   