# 🌤️ Real-Time Weather CLI Application

A lightweight, terminal-based **Python application** that fetches real-time weather information from the **OpenWeatherMap API**. The application handles sensitive credentials securely using environment variables and outputs current temperature metrics alongside clear weather descriptions.

---

## 🗺️ System Architecture

```text
               +---------------------------+

               |    User Interface (CLI)   |
               +-------------+-------------+
                             |
                      [Enter City Name]
                             v
               +-------------+-------------+

               |          main.py          | <--- [Load Secure Token] --- .env
               +-------------+-------------+
                             |
                  [HTTPS GET Request]
                             v
               +-------------+-------------+

               |     OpenWeather API       |
               +-------------+-------------+
                             |
                    [JSON Data Payload]
                             v
               +-------------+-------------+

               |   Console Output Terminal | ---> (Temp: 28°C, Cloudy)
               +---------------------------+
```

---

## 📂 Project Structure

```text
├── .env                 # Local environment variables (Contains API Secret Key - Hidden)
├── .gitignore           # Prevents sensitive files like .env from pushing to GitHub
├── main.py              # Main application pipeline execution script
└── README.md            # Detailed application documentation
```

---

## 🛠️ Features

*   **Secure Credential Handling:** Utilizes `python-dotenv` to safeguard private API tokens from exposed source control repositories.
*   **Dynamic Location Support:** Accepts international city and country formatting parameters (e.g., `Ahmedabad,IN` or `Nadiād,IN`).
*   **Metric System Calibration:** Automatically processes and outputs real-time heat indices scaled cleanly to Celsius (°C).

---

## ⚙️ Local Configuration & Setup

### 1. Project Dependencies
Ensure you install the required network connection and environment mapping packages:
```bash
pip install requests python-dotenv
```

### 2. Configure Credentials
Create a file named `.env` in the root folder alongside `main.py` and assign your personal token string:
```env
OPENWEATHER_API_KEY=your_secret_api_key_here
```

### 3. Git Security Precaution
Verify that your `.gitignore` file includes the path rule below so your key remains confidential:
```text
.env
```

---

## 💻 Usage

Execute the primary script block using your active terminal environment profile:
```bash
python main.py
```

### Application Simulation Example:
```text
Enter city: Ahmedabad,IN
Temp: 31.4°C, Description: clear sky
```
