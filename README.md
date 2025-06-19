# Stock Analyser

Interaktivní webová aplikace pro technickou a fundamentální analýzu akcií. Běží na Streamlit Cloud.

## Jak spustit online

1. Vytvoř si účet na [https://github.com](https://github.com) a [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Nahraj tento projekt do GitHub repozitáře (např. Adarq77/Stock-analyser)
3. Na [Streamlit Cloud](https://streamlit.io/cloud) klikni na "New app"
4. Vyber repozitář, jako hlavní soubor nastav `app.py`
5. Do sekce `Secrets` v administraci Streamlit Cloud vlož:

```
FMP_API_KEY = "TVŮJ_API_KLÍČ"
```

✅ Aplikace bude fungovat na iPadu i jiném zařízení jako webová aplikace.