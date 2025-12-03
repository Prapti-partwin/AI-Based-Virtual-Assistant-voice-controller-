# AI-Based-Virtual-Assistant-voice-controller-
Developed a standalone command-line voice assistant capable of understanding natural language queries and performing automated tasks. Integrated Speech-to-Text, Text-to-Speech, and GPT-based NLP for real-time conversational interaction.

# AI-Based Virtual Assistant (Voice Controlled)

A standalone **Python command-line voice assistant** capable of understanding natural language queries, performing automated tasks, and interacting in real-time using **Speech-to-Text**, **GPT-based NLP**, and **Text-to-Speech** technologies.

---

## **📌 Features**

* 🎤 **Voice Input** using microphone
* 🧠 **Natural Language Understanding** powered by GPT
* 🔊 **Text-to-Speech output** for voice responses
* ⚙️ **Command-line interface**, lightweight and portable
* 🛠 **Extensible architecture** for adding custom tasks and intents

---

## **🛠 Tools & Technologies**

| Component        | Library / Version                     |
| ---------------- | ------------------------------------- |
| Speech-to-Text   | SpeechRecognition (3.10.0)            |
| Microphone Audio | PyAudio (0.2.13)                      |
| AI/NLP Model     | OpenAI API (openai 0.28.0)            |
| Text-to-Speech   | pyttsx3 (2.90)                        |
| Env Management   | python-dotenv (1.0.0)                 |
| Environment      | Python (Anaconda, Terminal Interface) |

---

## **📁 Project Structure**

```
project-folder/
│── assistant.py
│── .env
│── requirements.txt
│── README.md
```

---

## **🚀 Getting Started**

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
```

### **2. Create a Virtual Environment (Recommended)**

```bash
conda create -n voice-assistant python=3.10
conda activate voice-assistant
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

> ⚠️ If **PyAudio** fails to install, you may need OS-specific steps or a wheel file.

---

## **🔐 Environment Variables**

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

---

## **▶️ Running the Assistant**

Run the main python script:

```bash
python assistant.py
```

You’ll hear:

> **"Hello! I am your assistant. Say 'exit' to quit."**

Then start speaking into your mic.

---

## **📦 Example Code Overview**

### **Main Flow**

1. **Listen** for microphone input
2. Convert speech → text using STT
3. Send text to GPT model
4. Receive understanding/response
5. Convert text → speech
6. Speak reply and wait for next command

---

## **🧩 How It Works (Step-by-Step)**

### **1. Speech Recognition**

* Uses microphone via **PyAudio**
* Converts sound waves into audio frames
* Sends audio to Google Web Speech API for transcription

### **2. GPT-Based NLP**

* The transcribed text is sent to OpenAI's GPT model
* The model interprets user intent
* Generates a natural-language response

### **3. Text-to-Speech (TTS)**

* Response is passed to **pyttsx3**
* Converts text → spoken audio offline

### **4. Real-Time Interaction**

* Loop continues until user says **"exit"**

---

## **📝 Requirements File**

`requirements.txt` example:

```
SpeechRecognition==3.10.0
pyttsx3==2.90
openai==0.28.0
python-dotenv==1.0.0
pyaudio==0.2.13
```

---

## **⚠️ Troubleshooting**

### **PyAudio Installation Error**

* Windows: install `.whl` from unofficial wheel repository
* macOS: `brew install portaudio` then `pip install pyaudio`
* Linux: `sudo apt-get install portaudio19-dev`

### **Microphone Not Detected**

* Check system input device settings
* Ensure permissions are allowed

### **OpenAI Authentication Error**

* Make sure `.env` file is correctly loaded
* Regenerate API key if needed

---

## **📌 Future Enhancements**

* Add offline STT (Whisper)
* Add task automation (open apps, send emails, etc.)
* Add wake-word detection
* Add conversation memory
* Package as an executable (`pyinstaller`)

---

