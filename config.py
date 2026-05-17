import os
from dotenv import load_dotenv

load_dotenv()

# =========================================================================================
#  🤖 RAPID X AI - AGENT CONFIGURATION
#  Use this file to customize your agent's personality, models, and behavior.
# =========================================================================================

# --- 1. AGENT PERSONA & PROMPTS ---
SYSTEM_PROMPT = """
You are a helpful and polite School Receptionist at "Rapid X High School".

**Your Goal:** Answer questions from parents about admissions, fees, and timings.

**Key Behaviors:**
1. **Multilingual:** You can speak fluent English and Hindi. If the user speaks Hindi, switch to Hindi immediately.
2. **Polite & Warm:** Always be welcomed and respectful.
3. **Be Concise:** Keep answers short (1-2 sentences).
4. **Admissions:** If asked about admissions, say they are open for Grade 1 to 10.
5. **Fees:** If asked about fees, say it starts at roughly 50k per year.

**CRITICAL:**
- Only use `transfer_call` if they explicitly ask to talk to the Principal or Admin.
- If they say "Bye", say "Namaste" or "Goodbye" and end the call.
"""

INITIAL_GREETING = "The user has picked up the call. Introduce yourself as the School Receptionist immediately."
fallback_greeting = "Greet the user immediately."

# --- 2. SPEECH-TO-TEXT (STT) SETTINGS ---
STT_PROVIDER = "deepgram"
STT_MODEL = "nova-2"
STT_LANGUAGE = "en"

# --- 3. TEXT-TO-SPEECH (TTS) SETTINGS ---
DEFAULT_TTS_PROVIDER = "elevenlabs"
DEFAULT_TTS_VOICE = "Rachel"

# Eleven Labs Specifics
ELEVENLABS_VOICE_ID = "Rachel"
ELEVENLABS_MODEL = "eleven_monolingual_v1"

# OpenAI TTS
OPENAI_TTS_VOICE = "alloy"

# Sarvam AI Specifics
SARVAM_MODEL = "bulbul:v2"
SARVAM_LANGUAGE = "en-IN"

# Cartesia Specifics
CARTESIA_MODEL = "sonic-2"
CARTESIA_VOICE = "f786b574-daa5-4673-aa0c-cbe3e8534c02"

# --- 4. LARGE LANGUAGE MODEL (LLM) SETTINGS ---
DEFAULT_LLM_PROVIDER = "openai"
DEFAULT_LLM_MODEL = "gpt-4o-mini"

# Groq Specifics
GROQ_MODEL = "llama-3.3-70b-versatile"
GROQ_TEMPERATURE = 0.7

# --- 5. TELEPHONY & TRANSFERS ---
DEFAULT_TRANSFER_NUMBER = os.getenv("DEFAULT_TRANSFER_NUMBER")
SIP_TRUNK_ID = os.getenv("VOBIZ_SIP_TRUNK_ID")
SIP_DOMAIN = os.getenv("VOBIZ_SIP_DOMAIN")