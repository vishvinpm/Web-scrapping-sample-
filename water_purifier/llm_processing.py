import openai
import os
from dotenv import load_dotenv

class LLMClient :
    def __init__(self) :
        load_dotenv()
        # Load the OpenAI API key from environment variables
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def run(self, prompt, data) :

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]   
        )
        """
        role and content are used to define the user message in the chat format
        The response will contain the model's reply.
        """
        return response