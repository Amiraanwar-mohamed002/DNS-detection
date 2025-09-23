# DNS Scam Detector

Minimal Flask + Tailwind app to score domain/URL suspiciousness using static heuristics only.

## Features
- Static checks: length, digits, hyphens, subdomains, IPv4-in-host, path length, entropy, punycode, non-ascii, suspicious TLD
- Weighted score → verdict: Likely Safe / Suspicious / Likely Scam
- Clean Tailwind UI, minimal JS
- Pytest with synthetic cases

## Run (Python 3.10+)

Windows PowerShell:
```bash
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
set FLASK_APP=app.py
flask run
```

macOS/Linux:
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
```

Open `http://localhost:5000`.

## Tests
```bash
pytest -q
```

## Security Notes
- Static analysis only. The app does not fetch, visit, or execute untrusted URLs.
- Always exercise caution with unknown domains.

## Optional improvements
- Integrate offline phishing feeds (do not auto-open URLs)
- Add DNS/WHOIS/TLS age checks via safe APIs
- Batch CSV import/export
