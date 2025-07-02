import openai
import os
from dotenv import load_dotenv

class GPTProcessing :
    def __init__(self) :
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
    
    #defining the function to process collected data
    def process_data(self, data) :
        #creating the prompt 
        prompt = "Here are the list of water purifiers :"

        #iterating through the data to create the prompt
        for i, product in enumerate(data, start = 1) :
            prompt += f"\n{i}. Name: {product['name']}, Price: {product['price']}, Link: {product['link']}"
        
        #returning the final prompt
        prompt += "\n\nPlease provide a summary of the top 5 water purifiers based on the data provided."

        #calling the openAI API to get the requested response
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        '''
        Calls the Chat API endpoint.
        Tells openAI to use the gpt-4 model.
        Sends a message to model like a a user asking a question.
        The response will contain the model's reply.
        '''
        #returning the response
        return response.choices[0].message.content
    
    