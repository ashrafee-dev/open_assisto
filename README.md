# Open-Assisto 🎙️

A lightweight, privacy-focused open source voice assistant built with Python

## Overview

Open-Assisto is a simple voice assistant that listens to your commands and helps with daily tasks—without collecting your data or requiring paid services. Built entirely with free tools, it's perfect for learning, experimenting, or just having a personal assistant on your local machine.

## Features

- 🗓️ **Calendar Management** - Add and check events using voice commands
- 🎥 **YouTube Search** - Find videos hands-free
- 🌤️ **Weather Updates** - Get current weather information
- ⏰ **Time & Date** - Ask for the current time or date (works offline)
- 💬 **Voice Interaction** - Natural speech recognition and text-to-speech responses

## Tech Stack

**Core:**
- Python 3.x
- SpeechRecognition - Voice input processing
- ElevenLabs - Natural voice output
- pyttsx3 - Text-to-speech fallback

**APIs:**
- OpenWeatherMap API - Weather data
- YouTube Data API v3 - Video search
- Google Calendar API - Calendar integration

## Getting Started

### Prerequisites

```bash
pip install SpeechRecognition pyttsx3 gTTS
```

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/open-assisto.git
cd open-assisto
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up API keys (see documentation)

4. Run the assistant
```bash
python main.py
```

## Why Open-Assisto?

Unlike Siri, Alexa, or Google Assistant, Open-Assisto:
- ✅ Runs entirely on your machine
- ✅ Doesn't store your voice data in the cloud
- ✅ Uses only free, open-source tools
- ✅ Can be customized and extended
- ✅ Great for learning about voice technology

## Project Goals

- Support at least 5 voice commands
- Integrate 3+ free APIs
- Achieve 90%+ accuracy with clear audio
- Maintain privacy and local-first design

## Team

- **Project Manager:** Mahdi Ashrafee
- **Team Lead:** Ehsanul Huqq
- **Testing Lead:** Mahmud Wahab

**Course:** CSE 368 - University at Buffalo  
**Instructor:** Professor Asif Imran

## Documentation

- [API References](#tech-stack)
- [User Guide](docs/user-guide.md) *(coming soon)*
- [Demo Video](docs/demo.mp4) *(coming soon)*

## License

This project is open-source and available for educational purposes.

## Acknowledgments

Built with support from the CSE Department at University at Buffalo.

---

*Made with ❤️ by the Open-Assisto team*

