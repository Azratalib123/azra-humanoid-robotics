from google import genai

API_KEY = "AIzaSyCCIWdmzu5OcCmAZ7j1aGtusepVSBd28xc"

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-pro",
    contents="Hello! Explain what humanoid robotics is in one line."
)

print(response.text)
