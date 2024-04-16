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

4. **Running the application**

   Start the HTTP server using uvicorn:

   ```
   uvicorn main:app --reload
   ```
   
  Alternatively, you can create a systemd service in Linux to manage the application and automatically start it on boot:

  - Create a systemd service file. For example, create a file named `telegram_bot_api.service` in the directory `/etc/systemd/system/`:

    ```
    sudo nano /etc/systemd/system/telegram_bot_api.service
    ```

  - Add the following content to the file, adjusting the paths as necessary:

    ```
    [Unit]
    Description=Telegram Bot API HTTP Server
    After=network.target

    [Service]
    User=your_username
    Group=your_group
    WorkingDirectory=/path/to/your/project
    ExecStart=/path/to/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
    Restart=always

    [Install]
    WantedBy=multi-user.target
    ```

    Replace `your_username`, `your_group`, `/path/to/your/project`, and `/path/to/venv/bin/uvicorn` with the appropriate values for your system.

  - Save the file and close the editor.

  - Reload systemd to load the new service file:

    ```
    sudo systemctl daemon-reload
    ```

  - Start the service:

    ```
    sudo systemctl start telegram_bot_api
    ```

  - Enable the service to start automatically on boot:

    ```
    sudo systemctl enable telegram_bot_api
    ```

  Now the Telegram Bot API HTTP Server will be managed by systemd, allowing you to start, stop, and restart it using systemd commands (`systemctl`). Additionally, it will start automatically on boot.

5. **Multiple Conversations**

   - By creating separate chat groups, you can have multiple conversations with the bot simultaneously.
   - Use the `/authorize` endpoint to create a new chat group with the bot user and obtain the group ID.
   - Use the obtained group ID in the requests to send messages to the bot in that specific group.

6. **Usage**

   To begin, you need to create a separate chat for isolated communication with the bot:

   - Use the `/authorize` endpoint to create a new chat group with the bot. This will generate a unique group ID for the chat:

     ```
     GET /authorize
     ```

     Example response:
     ```json
     {
       "group_id": 4147886708
     }
     ```

   Once you have obtained the group ID, you can use it to send requests:

   - Send requests to the bot using the following URL format:

     ```
     https://example.site/?group_id=your_group_id&text=your_command
     ```

     Example request:
     ```
     https://example.site/?group_id=4141332086&text=/start
     ```

     Example response:
     ```
      {
        "message": "Hi! I'm a translator @perebot ✋\n\nI will automatically translate messages in this group. To manage the bot, we recommend using the /settings command (it is also always available in the bot menu for administrators)\n\nReplacement bot: @ perevod_bot, channel.",
        "date": "04-16-2024 11:17:58",
        "replies": [
          "✅ Translate everything"
          "Except Russian"
          "Stop (pause)",
          "Go to bot"
          "🆓 Learn English for free",
          "Add to another chat"
        ]
      }
     ```

     You can use either the `text` parameter to send text messages or the `button` parameter (int) to specify the index of the button to press. 

     If you send a request like `https://example.site/?group_id=4141332086&button=0`, you will press the button ✅ Translate everything. Please note that if you simultaneously send both `button` and `text` parameters in the request, nothing will happen. Only one parameter should be used at a time.


## Notes

- Please ensure you comply with Telegram API usage rules to avoid getting your account blocked.

---

This README file provides the basic steps for installing, configuring, and using your project, as well as instructions for users to interact with your HTTP server to send messages to the bot and receive responses.
