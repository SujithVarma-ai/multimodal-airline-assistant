# FlightAI Voice Assistant

An AI-powered airline customer support assistant built using Ollama, Llama 3.2, Gradio, and Google Text-to-Speech (gTTS).

## Overview

FlightAI is an intelligent airline assistant that helps users obtain ticket pricing information through natural conversations. The assistant uses Llama 3.2 running locally via Ollama and supports tool calling to retrieve ticket prices dynamically. It also generates voice responses to create a more interactive user experience. The application also includes user authentication to provide secure access to the chatbot interface.

## Features

* AI-powered airline customer support assistant
* Built with Ollama and Llama 3.2
* Function calling for ticket price retrieval
* Voice response generation using Google Text-to-Speech (gTTS)
* Interactive Gradio web interface
* Real-time conversational experience
* Custom airline pricing assistant
* Secure chat interface with authentication support

## Technologies Used

* Python
* Ollama
* Llama 3.2
* OpenAI Compatible SDK
* Gradio
* Google Text-to-Speech (gTTS)

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Ollama and pull the model:

```bash
ollama pull llama3.2
```

Run the application:

```bash
python app.py
```

## How It Works

1. User enters a travel-related query.
2. Llama 3.2 processes the request.
3. If ticket pricing is required, the model triggers a tool call.
4. The pricing function retrieves the ticket cost.
5. The assistant generates a response.
6. gTTS converts the response into speech.
7. Gradio displays the conversation and plays the generated audio.

## Example Ticket Prices

| Destination | Price |
| ----------- | ----- |
| Hyderabad   | 100   |
| Bangalore   | 80    |
| Delhi       | 120   |
| Mumbai      | 150   |

## Sample Queries

* What is the ticket price to Hyderabad?
* How much does a return ticket to Delhi cost?
* Can you tell me the fare for Mumbai?
* What destinations are available?
 
# 📸 Application Screenshot

![App Screenshot](https://github.com/SujithVarma-ai/multimodal-airline-assistant/blob/main/Screenshot%202026-05-29%20080310.png)

## Future Improvements

* Flight booking support
* Database integration
* Dynamic fare retrieval
* Multi-language voice responses
* Flight status tracking

## License

MIT License
