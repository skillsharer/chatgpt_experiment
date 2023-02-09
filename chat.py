import openai

# Set up the OpenAI API client
with open(".env", "r") as envfile:
	my_api_key = envfile.readlines()
openai.api_key = my_api_key[0].strip("\n")

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = "Hello, how are you today?"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)