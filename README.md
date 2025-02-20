# Wi-Fi Credential Extractor

A Python script to retrieve saved Wi-Fi profiles and their passwords on Windows systems using the `netsh` command-line utility. 

---

## Features
- Retrieves a list of all saved Wi-Fi profiles on the system.
- Extracts the plaintext password for each profile (if available).
- Outputs the results in a clean, readable JSON format.

---

## Requirements
- **Operating System**: Windows (tested on Windows 10/11).
- **Python**: Python 3.x installed.

---

## Usage

1. **Clone the Repo**:  
   Clone the repo with:
   ```bash
   git clone https://github.com/Skky-dev/WIfi-Credentials-Extractor.git
3. **Run the Script**:  
   Execute the script using Python on Command Prompt or Powershell:
   ```bash
   python Script.py

---

## Example Output

```json
{
  "HomeWiFi": "MySecurePassword123",
  "OfficeNetwork": "Not Available",
  "GuestNetwork": "GuestPass456"
}
```
-  If a password is not available, it will return **"Not Available"**


---

## How it Works

The script uses the following commands:

 1. `netsh wlan show profile` to list all saved Wi-Fi profiles.
 
 2. `netsh wlan show profile <profile_name> key=clear` to extract the password for each profile.

The output is parsed, and the results are formatted into a JSON object for easy readability.
