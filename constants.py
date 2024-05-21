import os
from dotenv import load_dotenv

load_dotenv()

# Tweeter
bearer = os.getenv("X_BEARER")
consumer_key = os.getenv("X_CONSUMER_KEY")
consumer_secret = os.getenv("X_CONSUMER_SECRET")
access_token = os.getenv("X_ACCESS_TOKEN")
access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

# Postgres
db_name = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")

# Google Gemini
gemini_key = os.getenv("GEMINI_KEY")

prompts = [
    "Share a motivational quote from the Quran.",
    "Provide an inspirational saying from Prophet Muhammad (PBUH) about patience.",
    "What did Imam Al-Ghazali say about the importance of seeking knowledge?",
    "Share a motivational poem that reflects the values of Islam.",
    "Give a motivational statement about the significance of charity in Islam.",
    "What are some wise words from Ibn Khaldun about the rise and fall of civilizations?",
    "Share an uplifting quote from Rumi about love and spirituality.",
    "Provide a motivational saying from an Islamic scholar about the power of prayer.",
    "What did Ibn Sina say about the relationship between health and spirituality?",
    "Share a poem that inspires courage and resilience, written by an Islamic poet.",
    "Give a motivational statement on the importance of community and unity in Islam.",
    "What are some profound thoughts from Al-Farabi on the pursuit of happiness?",
    "Share an inspirational saying from a contemporary Islamic scholar about hope.",
    "Provide a motivational quote from the Hadith about perseverance and faith.",
    "What did Al-Kindi say about the importance of reason and intellect in Islam?",
    "Share a motivational poem that encourages self-reflection and inner peace.",
    "Give a motivational statement on the role of justice and fairness in Islam.",
    "What are some inspiring words from Jalaluddin Rumi about personal growth?",
    "Share an uplifting quote from the Quran about the power of gratitude.",
    "Provide a motivational saying from an Islamic scholar about the value of time.",
    "What did Al-Biruni contribute to the understanding of science and faith in Islam?",
    "Share a poem that motivates kindness and compassion, inspired by Islamic teachings.",
    "Give a motivational statement about the significance of fasting in Islam.",
    "What are some enlightening thoughts from Muhammad Iqbal on self-discovery?",
    "Share an inspirational quote from the Quran about the importance of family.",
    "Provide a motivational saying from an Islamic scholar about humility and modesty.",
    "What did Averroes (Ibn Rushd) say about the harmony between philosophy and religion?",
    "Share a motivational poem that emphasizes the beauty of forgiveness.",
    "Give a motivational statement on the importance of honesty and integrity in Islam.",
    "What are some wise words from Hassan al-Basri on leading a righteous life?"
]
