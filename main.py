import textwrap
import google.generativeai as genai

def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Manually set your Google API key (consider using environment variables)
GOOGLE_API_KEY = "YOUR_API_KEY"

# Configure the Gemini API
try:
    genai.configure(api_key=GOOGLE_API_KEY)
except Exception as e:
    print(f"Error configuring the API: {e}")
    # Handle the error gracefully, exit, or prompt the user to provide a valid API key

# List available models
available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]

# Display available models
print("Available Models:")
for i, model_name in enumerate(available_models, start=1):
    print(f"{i}. {model_name}")

# Ensure valid input for model selection
while True:
    try:
        selected_model_index = int(input("Enter the number corresponding to the model you want to use: ")) - 1
        if 0 <= selected_model_index < len(available_models):
            break
        else:
            print("Invalid input. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

selected_model = available_models[selected_model_index]

# Initialize the GenerativeModel with the selected model
try:
    model = genai.GenerativeModel(selected_model)
except Exception as e:
    print(f"Error initializing the model: {e}")
    # Handle the error gracefully, exit, or prompt the user to choose a different model

# Prompt the user for input
prompt_text = input("Enter a prompt for content generation: ")

# Generate text from the prompt
try:
    response = model.generate_content(prompt_text)
    formatted_output = to_markdown(response.text)
    print(formatted_output)
except Exception as e:
    print(f"Error generating content: {e}")
    # Handle the error gracefully, exit, or prompt the user to provide a valid prompt
