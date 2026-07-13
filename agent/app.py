import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "You are Coach Jordan, a high-energy motivational coach. Your job is to push the user to achieve their fitness and coding goals. Keep your answers short, intense, and disciplined. Use phrases like 'Let's go!', 'Focus!', and 'No excuses!'."
    
    history = []
    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()

#Did it stay in character? Yes. When asked for a pizza poem, it wrote it but quickly asked to go back to talking about technology.

#Was it helpful? Yes, it explained Frontend and Backend easily by comparing them to a restaurant's dining room and kitchen.

#What happened with the unclear text ("It doesn't work")? It did not guess. It asked questions to find out what was wrong and gave a simple checklist to fix it.

#ChatGPT is a general tool for anything. This Agent has a built-in job and personality (Alex the tech tutor) set up in the background. It is already ready to teach tech simply, without the user needing to give it special instructions.