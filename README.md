Schlayballs Phishing Study
 A Flask-based web application demonstrating phishing scam tactics for educational purposes. Built with Python, SQLite, JavaScript, and hosted via `ngrok` on Kali Linux, this project simulates a mock Nigerian phishing campaign to teach users about cybersecurity awareness.

 ## Features
 - **Dynamic Webpage**: Renders a form for users (e.g., `?user=friend123`) with JavaScript validation.
 - **Response Logging**: Stores user inputs (e.g., “420”) in SQLite.
 - **Email Automation**: Sends mock phishing emails to recipients using `send_email.py`.
 - **Secure Hosting**: Uses `ngrok` for public access (e.g., `https://<ngrok-id>.ngrok-free.app`).

 ## Tech Stack
 - Python, Flask
 - SQLite
 - JavaScript, HTML, CSS
 - ngrok, Kali Linux

 ## Setup
 ```bash
 git clone https://github.com/schlayguy/prank-webpage.git
 cd prank-webpage
 python -m venv venv
 source venv/bin/activate
 pip install flask
 python server.py
 # Run ngrok in another terminal
 ngrok http 5000
 ```

 ## Endpoints
 - `GET /?user=<username>`: Displays phishing form.
 - `POST /submit`: Logs response to SQLite.

 ## Demo
 [Watch the demo video](#) *(coming soon)*  
 ![Terminal Screenshot](screenshot.png) *(see LinkedIn post)*

 ## License
 MIT

 ## Contact
 Dave Schleman | [Fiverr](https://www.fiverr.com/schlayguy) | [LinkedIn](https://linkedin.com/in/daveschleman)

