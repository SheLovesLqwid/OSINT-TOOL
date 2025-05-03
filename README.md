# 🕵️‍♂️ **OSINT Multi-Tool**
### ⚡ **The Ultimate Open-Source OSINT CLI for Hackers, Pentesters & Cyber Sleuths**  

🔥 **Welcome to the most advanced, yet easy-to-use OSINT CLI ever built.**  

✔ **Skid-proof?** Yes.  
✔ **Skid-friendly?** Also yes.  
✔ **Database-free, API-supported, and 100% badass?** Absolutely.  

---

# 🎯 **What This Tool Does**
This isn't your average, half-baked "hacking" script. This is a **real** OSINT (Open-Source Intelligence) framework designed for:  

✅ **Pentesters** – Info gathering before attacks 🚀  
✅ **Investigators** – Track down people, leaks, and fraud cases 🔍  
✅ **Hackers** – Anonymous recon with TOR support 🕵️‍♂️  
✅ **Cybersecurity Pros** – Spot vulnerabilities before attackers do 🔥  
✅ **Skids Who Wanna Learn** – We got you, just don’t be dumb 😎  

---

# 🛠 **Features**
✔ **IP Lookup** – Geo-location, ISP, ASN, risk score  
✔ **Phone Lookup** – Carrier, location, line type, VOIP detection  
✔ **Email Lookup** – Breach check, verification, domain info  
✔ **Username Lookup** – Scans **50+ platforms** for a username  
✔ **Dark Web Search** – Queries **.onion** sites (TOR Required)  
✔ **Reverse Image Search** – Find images across the internet  
✔ **Metadata Extraction** – Get hidden EXIF data from images/docs  
✔ **WHOIS & DNS Lookup** – Full domain intelligence  
✔ **Proxy & TOR Support** – Stay anonymous while searching  

---

# 📂 **Project Structure**
```
python multitool/
│── osint-tool/               # Source Code
│   ├── data/                 # Stores lookup results
│   │   ├── results.csv
│   │   ├── results.json
│   ├── modules/              # All OSINT modules
│   │   ├── ip_lookup.py
│   │   ├── phone_lookup.py
│   │   ├── email_lookup.py
│   │   ├── username_lookup.py
│   │   ├── dark_web_lookup.py
│   │   ├── reverse_image.py
│   │   ├── metadata_extractor.py
│   │   ├── whois_dns.py
│   │   ├── utils.py
│   ├── config/               # API keys & settings
│   │   ├── settings.json
│   ├── main.py               # Main CLI interface
│   ├── requirements.txt      # Dependencies
│── README.md                 # Documentation
```

---

# 🔑 **API Keys Setup (REQUIRED!)**  

This tool requires API keys for certain lookups (phone numbers, email breaches, etc.).  

## 📌 **Step 1: Get API Keys**
You'll need to sign up for **NumVerify** and **Have I Been Pwned (HIBP)** APIs.  

- **NumVerify (Phone Number Intelligence)**
  - Get your API key: [https://numverify.com/](https://numverify.com/)
  - Sign up for a free or paid plan  
  - Copy your **API Key**  

- **HIBP (Email Breach Check)**
  - Get your API key: [https://haveibeenpwned.com/API/Key](https://haveibeenpwned.com/API/Key)  
  - Sign up and pay the **$3.50 fee**  
  - Copy your **API Key**  

---

## 📌 **Step 2: Configure API Keys**  
After obtaining the keys, open the `config/settings.json` file and add them:  

```json
{
  "api_keys": {
      "numverify": "YOUR_NUMVERIFY_API_KEY",
      "hibp": "YOUR_HIBP_API_KEY"
  },
  "proxy": {
      "enabled": false,
      "http": "",
      "https": ""
  }
}
```
🚨 **DO NOT SHARE YOUR API KEYS!** 🚨  

---

# 🚀 **Installation & Setup**  

### 1️⃣ **Extract & Copy Files Into a New Folder**
After downloading/cloning the repo, **extract all contents** and move them into a **new directory**.  

**Example:**  
```powershell
mkdir osint-tool
mv extracted_files/* osint-tool/
cd osint-tool
```
⚠️ **Skipping this step will break the setup!**  

---

### 2️⃣ **Install Python (If Not Installed)**
- Download & Install **Python 3.10+** from:  
  🔗 [https://www.python.org/downloads/](https://www.python.org/downloads/)  
- **Check the box ✅ "Add Python to PATH"** during installation.

---

### 3️⃣ **Clone This Repository**
```powershell
git clone https://github.com/SheLovesLqwid/OSINT-TOOL.git
cd OSINT-TOOL
```

---

### 4️⃣ **Install Dependencies**  
**(pip install)**  
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

### 5️⃣ **Run the OSINT Tool**
```powershell
python main.py
```

---

# 🛡 **TOR Setup (For Dark Web Search)**
### 1️⃣ **Install TOR**  
- **Windows:** [Download TOR](https://www.torproject.org/download/)  
- **Linux:**  
  ```bash
  sudo apt install tor
  ```

### 2️⃣ **Start TOR**
```powershell
tor.exe
```

### 3️⃣ **Run Dark Web Search**
```powershell
python main.py
```
Select **Option 5** → **Enter a search term** → **Results appear!** 🚀  

---

# ⚡ **Supported Platforms**
✔ Windows 10/11  
✔ macOS  
✔ Linux (Ubuntu, Debian, Arch, Kali)  

---

# 🚀 **Contributing**
Want to add a feature? Fork the repo, make changes, and submit a pull request! 🚀  
```powershell
git clone https://github.com/SheLovesLqwid/osint-tool.git
cd osint-tool
```

---

# 🔥 **Upcoming Features**
✔ **Automated Subdomain Enumeration**  
✔ **Deep Web Search Without TOR**  
✔ **AI-Based OSINT Data Correlation**  

---

# 🛑 **Legal Disclaimer**
⚠ **This tool is for educational and research purposes only.**  
The developers take **no responsibility** for misuse. **Don’t be an idiot.** 🕵️‍♂️💻  

---

🔥 **Enjoy this ultimate OSINT tool!** If you have feature requests or issues, let me know! 🚀
