## AI Chatbot & Image Generator Using Together API
# Project Overview

This Python project uses the Together API to create an AI that can perform two tasks: chatting with users and generating images based on user prompts. Both functionalities are seamlessly integrated into a single main script.

# Features
**AI Chat:** The AI can engage in conversations with users, providing dynamic and context-aware responses.<BR/>

**Image Generation:** The AI can create images based on user-provided prompts. Generated images are saved locally for future use.<BR/>

# Project Structure

**main.py:** The main script where the AI chat and image generation functionalities are implemented.<BR/>

**Api.py:** A separate file where the API key is stored. You can create your own `Api.py` file and replace the variable with your API key.<BR/>

**Generated Images:** Images created by the AI are stored in the same directory as the main script, with filenames like `Ai_image_generate_X.jpg` where X is a number.

# Installation
<BR/>

 **1. Clone the repository:**


 `git clone https://github.com/Abidashoukat/Together-API-Project/main.py`

 **2. Install the required dependencies:**


`pip install -r requirements.txt`
<BR/>
 **3. Create your Api.py file:**

Create a file named `Api.py` in the root directory.
Inside Api.py, define your `API key` variable like this:

`apikey = 'your_api_key_here'`
<BR/>

**4. Run the main script:**

`python main.py`
<BR/>

# Usage
Upon running` main.py`, you will be prompted to choose between two options:

**Chat with AI:** You can have a conversation with the AI by choosing option `1` or typing `"chat"`. The AI will respond to your queries based on the provided model.<BR/>

**Generate an Image:** By choosing option `2` or typing `"image"` or `"generate image"`, you can provide prompts to the AI, and it will generate images based on your input. Images are saved in the working directory.<BR/>

To exit either mode, type "quit" or "exit".

# How It Works

**AI Chat**
The `Ai_chat` method sends the user's query to the Together API's chat model and prints the response.<BR/>

**Image Generation**
The Ai_image_generate method takes a prompt and generates an image using the Together API's image generation model. The generated image is decoded from base64 and saved locally.<BR/>

**Error Handling**
The project includes basic error handling to manage exceptions during API calls or user input errors. If an error occurs, an informative message is displayed to guide the user.

 # Future Enhancements
 
**Add more AI models:** Integrate additional models for diverse chat and image generation capabilities.<BR/>

**Enhanced Error Handling:** Improve the robustness of error handling to cover more edge cases.<BR/>

**User Interface:** Develop a GUI for a more user-friendly experience.<BR/>

# Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests. For significant changes, please open an issue to discuss the proposed changes.

# License
This project is licensed under the MIT License. See the LICENSE file for details.










