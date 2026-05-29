import json
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

OLLAMA_BASE_URL = "http://localhost:11434/v1"

ollama = OpenAI(
    base_url=OLLAMA_BASE_URL,
    api_key="ollama"
)

response = ollama.chat.completions.create(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response.choices[0].message.content)

# airline assistant
system_message = '''You are a helpful assistant for an Airline called FlightAI.
Give short, courteous answers, no more than 1 sentence.
Always be accurate. If you don't know the answer, say so.'''

ticket_prices = {"Hyderabad": 100, "Bangalore": 80, "Delhi": 120, "Mumbai": 150}
def get_ticket_price(destination):
    print(f"Tool call for city {destination}")
    price = ticket_prices.get(destination)
    return price
print(get_ticket_price("Hyderabad"))

price_function = {
    "name": "get_ticket_price",
    "description": "Get the price of a return ticket to the destination city.",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city that the customer wants to travel to",
            },
        },
        "required": ["destination_city"],
        "additionalProperties": False
    }
}
tools = [{"type": "function", "function": price_function}]
print(tools)


from gtts import gTTS
def talker(message):
    tts = gTTS(text=message, lang="en")
    audio_file = "response.mp3"
    tts.save(audio_file)
    return audio_file


# A multimodel AI assistant with audio generation. 
def chat(history):
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    messages = [{"role": "system", "content": system_message}] + history
    response = ollama.chat.completions.create(model="llama3.2", messages=messages, tools=tools)
    cities = []

    while response.choices[0].finish_reason=="tool_calls":
        message = response.choices[0].message
        responses, cities = handle_tool_calls_and_return_cities(message)
        messages.append(message)
        messages.extend(responses)
        response = ollama.chat.completions.create(model="llama3.2", messages=messages, tools=tools)

    reply = response.choices[0].message.content
    history += [{"role":"assistant", "content":reply}]

    voice = talker(reply)

    
    return history, voice 

def handle_tool_calls_and_return_cities(message):
    responses = []
    cities = []
    for tool_call in message.tool_calls:
        if tool_call.function.name == "get_ticket_price":
            arguments = json.loads(tool_call.function.arguments)
            city = arguments.get('destination_city')
            cities.append(city)
            price_details = get_ticket_price(city)
            responses.append({
                "role": "tool",
                "content": str(price_details),
                "tool_call_id": tool_call.id
            })
    return responses, cities

# 3 types of Gradio UI - gr.ChatInterface, gr.Interface, and gr.Blocks

def put_message_in_chatbot(message, history):
        return "", history + [{"role":"user", "content":message}]

# UI definition

with gr.Blocks() as ui:
    with gr.Row():
        chatbot = gr.Chatbot(height=500)
    with gr.Row():
        audio_output = gr.Audio(autoplay=True)
    with gr.Row():
        message = gr.Textbox(label="Chat with our AI Assistant:")

    message.submit(put_message_in_chatbot, inputs=[message, chatbot], outputs=[message, chatbot]).then(
        chat, inputs=chatbot, outputs=[chatbot, audio_output]
    )

ui.launch(inbrowser=True, auth=("sujju", "sujju"))
