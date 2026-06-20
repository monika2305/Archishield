# Groq AI Setup

Required only for the "Ask Your Model" AI assistant page. All other pages work without this.

1. Install: `pip install groq`
2. Get a free key at [console.groq.com/keys](https://console.groq.com/keys) (sign in with Google)
3. Set it:
   - Windows: `setx GROQ_API_KEY "your-key-here"` (then reopen terminal)
   - Mac/Linux: `export GROQ_API_KEY="your-key-here"`
4. Run: `streamlit run Back.py`
