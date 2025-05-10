# 🔥 Tinder Auto-Liker Bot

This is an automation script that logs into Tinder using Facebook and automatically likes profiles using Selenium. It's built for educational purposes and demonstrates web automation with Python.

---

## 🚀 Features

- Automated login to Tinder using Facebook credentials
- Handles multiple popups (cookies, location, match dialogs)
- Auto-likes 25 profiles per run
- Uses environment variables to keep login info secure

---

## 🛠 Tech Stack

- Python
- Selenium
- python-dotenv
- Chrome WebDriver

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/tinder-auto-liker.git
cd tinder-auto-liker
```
2. **Install the dependencies
```bash
pip install -r requirements.txt
```
3. Set up environment variables
   Create a .env file in the root directory and add your Facebook credentials:
```bash
EMAIL=your_facebook_email
PASSWORD=your_facebook_password
```
4. **Run the bot
```bash
python main.py
```
