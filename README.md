# LiveKit Vobiz Outbound Agent with Eleven Labs TTS 📞

A production-ready voice agent capable of making outbound calls using **LiveKit**, **Deepgram**, and **Groq (Llama 3.3)**.
**NOW WITH ELEVEN LABS TEXT-TO-SPEECH!** 🎤

## 🚀 Features
- **Eleven Labs TTS** - Default high-quality Text-to-Speech with natural voices (Rachel, Chris, Nova, Bella, etc.)
- **Ultra-Fast LLM** - Uses **Groq** running `llama-3.3-70b-versatile` for near-instant responses
- **Multiple TTS Options** - Supports Deepgram, OpenAI, Sarvam, and Cartesia as fallback
- **High-Quality STT** - Uses **Deepgram** for accurate Speech-to-Text transcription
- **SIP Trunking** - Integrated with **Vobiz** for PSTN connectivity
- **Robust Configuration** - Centralized `config.py` for easy customization

---

## 🛠️ Setup & Installation

### 1. Prerequisites
- Python 3.10+ (Recommended: 3.10.13)
- A [LiveKit Cloud](https://cloud.livekit.io/) account
- A [Deepgram](https://deepgram.com/) API Key
- A [Groq](https://groq.com/) API Key
- An [Eleven Labs](https://elevenlabs.io/) API Key
- A SIP Provider (e.g., Vobiz)

### 2. Clone & Install
```bash
# Clone the repository
git clone <your-repo-url>
cd elevemnlab

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment
```bash
cp .env.example .env
# Edit .env and add your API keys:
# - LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET
# - DEEPGRAM_API_KEY
# - GROQ_API_KEY
# - ELEVENLABS_API_KEY (new!)
# - VOBIZ_SIP_*
```

---

## 🏃 Quick Start

### 1. Start the Agent
```bash
python agent.py start
```

### 2. Make an Outbound Call
```bash
python make_call.py --to +91XXXXXXXXXX
```

---

## 🎤 Eleven Labs Configuration

### Get Your API Key
1. Sign up at https://elevenlabs.io/
2. Go to Settings → API Keys
3. Copy your API key

### Set in .env
```
ELEVENLABS_API_KEY=your_api_key
TTS_PROVIDER=elevenlabs
ELEVENLABS_VOICE_ID=Rachel  # Options: Rachel, Chris, Nova, Bella, Sophia, Oliver, etc.
ELEVENLABS_MODEL=eleven_monolingual_v1
```

### Available Voices
- **Rachel** ⭐ (Default) - Warm, professional
- **Chris** - Energetic, friendly
- **Nova** - Clear, articulate
- **Bella** - Smooth, natural
- **Sophia** - Sophisticated
- **Oliver** - Deep, authoritative
- And more!

---

## 🔧 Troubleshooting

### Eleven Labs Not Working
1. Verify `ELEVENLABS_API_KEY` in `.env`
2. Check voice name is correct (case-sensitive)
3. Ensure your account has API credits
4. Check logs for error messages

### Switch TTS Providers
Edit `.env` to switch providers:
```
# OpenAI
TTS_PROVIDER=openai

# Deepgram
TTS_PROVIDER=deepgram

# Sarvam (Indian voices)
TTS_PROVIDER=sarvam
```

---

## 📂 Project Structure
- `agent.py` - Main agent with TTS/LLM provider support
- `config.py` - Configuration for prompts, models, voices
- `requirements.txt` - Python dependencies
- `.env.example` - Environment variables template

---

**Now with Eleven Labs TTS for the most natural voice experience! 🎉**