import os
import smtplib
from email.mime.text import MIMEText

def main():
    to_email = os.getenv("NOTIFY_EMAIL")
    user = os.getenv("SMTP_USERNAME")
    password = os.getenv("SMTP_PASSWORD")
    host = os.getenv("SMTP_HOST", "smtp.office365.com")
    port = int(os.getenv("SMTP_PORT", "587"))

    # Corpo da mensagem
    body = f"""Pipeline executado com sucesso!

Repositório: {os.getenv("GITHUB_REPOSITORY")}
Commit: {os.getenv("GITHUB_SHA", "")[:7]}
"""

    msg = MIMEText(body, _charset="utf-8")
    msg["Subject"] = "[CI] Status do Pipeline"
    msg["From"] = user
    msg["To"] = to_email

    # Conexão SMTP simples
    server = smtplib.SMTP(host, port)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

    print("✅ E-mail enviado para", to_email)

if __name__ == "__main__":
    main()
