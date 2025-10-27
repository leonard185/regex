import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv


# --- STEP 1: Extract email address from user input ---
sentence = input("Enter a sentence containing one email address: ")

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
match = re.search(pattern, sentence)

if match:
    extracted_email = match.group(0)       # ✅ define variable properly
    print("Extracted email:", extracted_email)
else:
    print("❌ No valid email address found.")
    exit()

# --- STEP 2: Configure sender details ---
MAILTRAP_HOST = "MAILTRAP_HOST"
MAILTRAP_PORT = 'MAILTRAP_PORT'
MAILTRAP_USER = "MAILTRAP_USERNAME"
MAILTRAP_PASS = "MAILTRAP_PASSWORD"

sender_email = "noreply@rpa-bot.com"
receiver_email = extracted_email
# --- STEP 3: Create the email content ---
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Email Extraction Success ✅"

body = f"""
Hello {receiver_email},

Your email address has been successfully extracted by our RPA bot.

Best regards,
The RPA Automation Team 🤖
"""
msg.attach(MIMEText(body, "plain"))

# --- STEP 4: Send the email ---
try:
    with smtplib.SMTP(MAILTRAP_HOST, MAILTRAP_PORT) as server:
        server.login(MAILTRAP_USER, MAILTRAP_PASS)
        server.send_message(msg)
        print("✅ Confirmation email sent successfully!")
except Exception as e:
    print("❌ Failed to send email:", e)
