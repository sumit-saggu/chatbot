# Simple Python Chatbot

A command-line personal assistant chatbot built with Python.  
It can search Google, play YouTube videos, fetch Wikipedia summaries, open websites, and launch applications.

---

## 🚀 Features

- **Google Search:**  
  Type `search <your query>` to search Google.  
  **Example:**  
  ```
  You: search weather in delhi
  ```

- **Play YouTube Video:**  
  Type `play <video name>` to play the first YouTube video result.  
  **Example:**  
  ```
  You: play python tutorial
  ```

- **Wikipedia Summary:**  
  Type `wikipedia <topic>` to get a short summary from Wikipedia.  
  **Example:**  
  ```
  You: wikipedia india
  ```

- **Open Website:**  
  Type `open web <website>` (e.g., `open web facebook`) to open a website.  
  **Example:**  
  ```
  You: open web facebook
  ```

- **Open Application:**  
  Type `open <app name>` (e.g., `open notepad`) to launch an application on your computer.  
  **Example:**  
  ```
  You: open notepad
  ```

- **Exit:**  
  Type `bye` to exit the chatbot.  
  **Example:**  
  ```
  You: bye
  ```

---

## 🛠️ Requirements

- Python 3.x
- [pytube](https://pytube.io/)  
  ```
  pip install pytube
  ```
- [wikipedia](https://pypi.org/project/wikipedia/)  
  ```
  pip install wikipedia
  ```

---

## 📄 Usage

1. **Clone or Download this Repository**
2. **Install the requirements** (see above)
3. **Run the chatbot**
   ```bash
   python chatbot.py
   ```
4. **Type your commands as described in the Features section.**

---

## ⚠️ Notes

- For YouTube video playback, a web browser will open the first search result.
- For Wikipedia, ambiguous or missing topics will prompt for clarification.
- Application launching works for apps available in your system's PATH (e.g., `notepad`, `calc` on Windows).
- The chatbot is case-insensitive and works in the terminal/command prompt.

---

## 📄 License

This project is for personal and
