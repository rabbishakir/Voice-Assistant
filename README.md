# Voice-Assistant

Jarvis is a basic Python voice assistant designed for beginners who want to understand how speech recognition, text-to-speech, conditions, and functions work together in a real project.
This project uses simple Python logic (if/else functions) to listen to your voice, process commands, and speak back responses making it a perfect starting point for anyone learning Python automation or AI assistant development.

## **Features**

* Greet the user according to the time of day (morning, afternoon, evening)
* Recognize voice commands using Google Speech Recognition
* Speak responses using pyttsx3
* Time & Date announcements
* Wikipedia search with spoken summary
* Open websites like Google, Facebook, YouTube
* Play random music from a specified folder
* Open system applications: Calculator, Notepad, CMD
* Open Calendar (Google Calendar via browser)
* Tell jokes and respond to basic small talk
* Exit gracefully with a voice command

## **How to run?**

### **1. Create a virtual environment:**

```bash
conda create -n jarvis python=3.11 -y
```

### **2. Activate virtual environment:**

```bash
conda activate jarvis
```

### **3. Install required packages:**

```bash
pip install -r requirements.txt
```

## **What packages do we need**

```bash
SpeechRecognition==3.14.3
pyttsx3==2.99
PyAudio
wikipedia
```

## **Author**

Md Nazmul Shakir Rabbi
Creator & Maintainer of the Jarvis Python Assistant Project
Passionate about AI, Automation, and building beginner-friendly learning resources.

## **License**

This project is open-source and free to use for learning and educational purposes.
You may modify, improve, and share it, as long as you credit the original author.
