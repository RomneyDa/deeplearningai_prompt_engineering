import openai
import os

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(
    prompt, model="gpt-3.5-turbo", temperature=0
):  # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    """
    This function takes a prompt and returns a completion from the OpenAI API
    Reference: https://platform.openai.com/docs/api-reference

    Optionally, you can specify the model and temperature
    Info on models: https://platform.openai.com/docs/models
    Temperature: decimal between 0 and 1; 0 is deterministic (always the same result), 1 is highly random
    """
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    #     print(str(response.choices[0].message))
    return response.choices[0].message["content"]
