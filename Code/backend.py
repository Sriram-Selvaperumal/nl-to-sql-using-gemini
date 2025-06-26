import os
import google.generativeai as genai

genai.configure(api_key="*******API-KEY*******")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="An AI tool that takes input as prompt from user in Any natural language (ex:english,spanish,tamil,hindi) and convert it to sql query",
)

def GenerateResponse(input_text):
    response = model.generate_content([
    "input: who are you",
    "output: I am an Universal Natural Language to SQL Query Converter !!! "
    "input: What all can you do?",
    "output: I can Convert Any language that Known to Mankind to SQL QUery !!!",
    f"input:{input_text}",
    "output:",
    ])



    return response.text
