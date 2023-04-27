# Mail.tm-Telegram-Bot
Use Mail.tm in Telegram
# Mail.tm API Chatbot

This is a simple chatbot that uses the Mail.tm API to send and receive messages. You can use this chatbot to receive messages from users and respond to them automatically.

## Getting Started

Follow these steps to get started with the Mail.tm API Chatbot:

1. Clone the repository to your local machine:

<code>git clone https://github.com/your_username/mail-tm-api-chatbot.git</code>

2. Install the necessary dependencies:

In the root directory of your cloned repository, create a virtual environment and activate it:

<code>python3 -m venv env</code>
<code>source env/bin/activate</code>


Then, install the required packages:
<code>pip install -r requirements.txt</code>

<br><br>


3. Create a Mail.tm account:

If you haven't already done so, create a free account on [Mail.tm](https://mail.tm/) to get your API key.

4. Set your Mail.tm API key:

Export your Mail.tm API key as an environment variable:

export MAIL_TM_API_KEY=your_mail_tm_api_key_here



5. Run the application:

In the root directory of your cloned repository, run the following command:

<code>gunicorn app:app</code>

6. Test the application:

Send a POST request to `http://localhost:8000/` with a JSON payload containing a message:

<code> curl -X POST 

-H "Content-Type: application/json" 

-d '{"message": "Hello, bot!"}' 

http://localhost:8000/

</code>




The chatbot should send an email containing the received message to your email address.

## Deploying to Heroku

You can also deploy this chatbot to Heroku. Simply click on the button below to deploy the application:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/iSabbir/Mail.tm-Telegram-Bot/)

Make sure to replace `your_username` with your actual Github username in the above URL.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

