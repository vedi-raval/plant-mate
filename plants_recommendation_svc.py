import chainlit as cl
from openai import AsyncOpenAI
import asyncio

# instrument the OpenAI client
cl.instrument_openai()

client = AsyncOpenAI()
settings = {
    "model": "gpt-4o-mini",
    "temperature": 0.7,
    "max_tokens": 250, 
}

# Function to create a prompt based on user input
def create_prompt(past_conversation_history):
    base_prompt = ''' You are an expert in gardening. A user is chatting with you and will provide you with details about their garden plot, such as the plot size, sunlight exposure, soil type, and perhaps other preferences. 
    
    You are tasked with suggesting the top 3-5 most suitable plants they should consider planting in their garden. 

    Below, you will be provided with the past conversation between you and the user. Respond based on the known knowledge you have of your conversation with the user.
    A user can ask any question or further detail about the conversation history and you must respond. Remember, they can reference content from your reponses.
    '''

    prompt_builder = f"{base_prompt}\n\nPast Conversation between you and the user: {past_conversation_history}\n\nYour Response:"
    
    # Adding user input to the prompt
    return prompt_builder

@cl.on_chat_start
async def start_chat(): 

    initial_message = "Hello! My name's Plant Mate and I'm here to help you choose the best plants for your garden. To get started, could you please tell me about the size of your plot, the amount of sunlight it recieves, and any specific preferences you have?"

    msg = cl.Message(content="")
    await msg.send()

    for idx in range(0, len(initial_message), 1): 
        current_chunk = initial_message[idx: idx + 1]
        await asyncio.sleep(0.01)
        await msg.stream_token(current_chunk)


    await msg.update()

    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": f"Bot: {initial_message}"}],
    )


@cl.on_message
async def on_message(message: cl.Message):

    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": f"User:{message.content}"})
    
    bot_response = cl.Message(content="")
    await bot_response.send()


    prompt = create_prompt(past_conversation_history=message_history)
        
    streamed_response = await client.chat.completions.create(
        messages=[
            {
                "content": prompt,
                "role": "system"
            }
        ],
        stream=True,
        **settings
    )

    async for part in streamed_response:
        if token := part.choices[0].delta.content or "":
            await bot_response.stream_token(token)

    message_history.append({"role": "system", "content": f"Bot:{bot_response.content}"})
    await bot_response.update()
