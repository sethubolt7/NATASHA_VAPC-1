import os
import openai
#from openai.api_resources import completion

# openai.api_key = "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"
# model_engine = "text-davinci-003"
# while True:
#   prompt = str(input())
#   completion= openai.Completion.create(
#     model=model_engine,
#     prompt=prompt,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5,
#   )
#   response = completion.choices[0].text
#   print(response)


# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key

# Define a prompt or input
input_prompt = "Once upon a time"

# Use the OpenAI API to generate text
response = openai.Completion.create(
    engine="text-davinci-003",  # Choose an engine (e.g., text-davinci-003)
    prompt=input_prompt,
    max_tokens=100  # Adjust as needed
)

# Extract and print the generated text
generated_text = response.choices[0].text
print(generated_text)



#################################################################################
#############################NATASHA VAPC-1######################################
#############################testing purpose#####################################
#############################tester:SETHULAKSHMANAN SP###########################
#################################################################################
#################################################################################
#############################NATASHA VAPC-1######################################
#############################testing purpose#####################################
#############################tester:SETHULAKSHMANAN SP###########################
#################################################################################
#################################################################################
#############################NATASHA VAPC-1######################################
#############################testing purpose#####################################
#############################tester:SETHULAKSHMANAN SP###########################
#################################################################################
#################################################################################
#############################NATASHA VAPC-1######################################
#############################testing purpose#####################################
#############################tester:SETHULAKSHMANAN SP###########################
#################################################################################
#################################################################################
#############################NATASHA VAPC-1######################################
#############################testing purpose#####################################
#############################tester:SETHULAKSHMANAN SP###########################
#################################################################################
#################################################################################
#############################NATASHA VAPC-1######################################
#############################testing purpose#####################################
#############################tester:SETHULAKSHMANAN SP###########################
#################################################################################
#################################################################################
#############################NATASHA VAPC-1######################################
#############################testing purpose#####################################
#############################tester:SETHULAKSHMANAN SP###########################
#################################################################################