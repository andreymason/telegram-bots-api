# Telegram Bot API

This project aims to create a simple HTTP server using FastAPI for building an API to interact with Telegram bots. It facilitates sending messages to a Telegram bot and receiving responses, essentially serving as an API for interacting with any Telegram bot.

## Installation and Usage

1. **Obtaining API credentials for Telegram**

   - Sign up for Telegram using any application.
   - Log in to your Telegram account: [https://my.telegram.org](https://my.telegram.org).
   - Go to "API development tools" and fill out the form.
   - You will receive basic addresses as well as the api_id and api_hash parameters required for user authorization.
   - Currently, each number can only have one api_id connected to it.

2. **Setting up the .env file**

   - Create a file named .env in the root of the project.
   - In the .env file, specify values for API_ID and API_HASH obtained in the previous step:
     ```
     API_ID="your_api_id"
     API_HASH="your_api_hash"
     ```

Here's the revised section for setting up the virtual environment using `python3 -m venv venv`:

---

3. **Setting up the virtual environment / Installing dependencies**

   - Create a virtual environment using Python's built-in venv module:
     ```
     python3 -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       venv\Scripts\activate
       ```
     - On Unix or MacOS:
       ```
       source venv/bin/activate
       ```

   Ensure you have activated the virtual environment. Then run the following command to install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

---

This revised section provides instructions for setting up the virtual environment using Python's venv module and installing dependencies from the requirements.txt file.

4. **Running the application**

   Start the HTTP server using uvicorn:

   ```
   uvicorn main:app --reload
   ```

5. **Usage**

   - Find the bot in Telegram that you want to interact with.
   - Send it a message.
   - Get the bot's ID using @username_to_id_bot.
   - Now you can send requests to the bot with commands using the following URL format:
     ```
     http://127.0.0.1:8000/?chat_id=your_chat_id&text=your_command
     ```
  
     Example request:
     ```
     http://127.0.0.1:8000/?chat_id=292972715&text=/help
     ```
     ```json
      {
          "message": "🌎 Please select a language.",
          "date": "04-02-2024 11:46:23",
          "replies": [
              "🇬🇧 English",
              "🇪🇸 Español",
              "🇷🇺 Русский"
          ]
      }
     ```

## Notes

- Please ensure you comply with Telegram API usage rules to avoid getting your account blocked.

---

This README file provides the basic steps for installing, configuring, and using your project, as well as instructions for users to interact with your HTTP server to send messages to the bot and receive responses.
