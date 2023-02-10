import openai
import time
import random

# Set up the OpenAI API client
with open(".env", "r") as envfile:
	my_api_key = envfile.readlines()
openai.api_key = my_api_key[0].strip("\n")

# Set up the model and prompt
model_engine = "text-davinci-003"
request = " Please continue this reasoning thread."
topic = "time travelling"
prompt = "Lets brainstorm of " + topic + ". How would you solve this problem?" + request
discussion_length = 10

print("Conversation starter: ", prompt)
answers = []
idx = 0

while idx < discussion_length:
	# Generate a response
	completion = openai.Completion.create(
	    engine=model_engine,
	    prompt=prompt,
	    max_tokens=100,
	    n=1,
	    stop=None,
	    temperature=0.99,
	)

	prompt = completion.choices[0].text
	if len(prompt) == 0:
		prompt = answers[-1]
	
	answers.append(prompt)
	print("------------------------------------------", idx)
	print(prompt)
	
	if idx == discussion_length-2:
		request = " Please finalize our thread."
	
	prompt += request
	time.sleep(5)
	idx += 1
