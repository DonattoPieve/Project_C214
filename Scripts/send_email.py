import os
import smtplib
from email.mime.text import MIMEText

def env(name, default=None, required=False):
    val = os.getenv(name, default)
    if required and not val:
        raise SystemExit(f"Variável de ambiente ausente: {name}")
    return val

def main():
    repo = env("GITHUB_REPOSITORY", "unknown")
    run_id = env("GITHUB_RUN_ID", "unknown")
    sha = env("GITHUB_SHA", "unknown")[:7]
    test_status = env("TEST_STATUS", "unknown")
    build_status = env("BUILD_STATUS", "unknown")
    to_email = env("NOTIFY_EMAIL", required=True)

    run_url = f"https://github.com/{repo}/actions/runs/{run_id}" if run_id != "unknown" else "(desconhecido)"

    body = f"""Pipeline executado!

Repositório: {repo}
Commit: {sha}
Testes: {test_status}
Build: {build_status}
Execução: {run_url}
"""

    msg = MIMEText(body, _charset="utf-8")
    msg["Subject"] = f"[CI] {repo} — Testes: {test_status} | Build: {build_status}"
    msg["From"] = env("SMTP_FROM", env("SMTP_USERNAME", "ci@example.com"))
    msg["To"] = to_email

    host = env("SMTP_HOST", required=True)
    port = int(env("SMTP_PORT", "587"))
    user = env("SMTP_USERNAME", required=True)
    password = env("SMTP_PASSWORD", required=True)
    use_tls = env("SMTP_USE_TLS", "true").lower() in {"1","true","yes","on"}

    if use_tls:
        server = smtplib.SMTP(host, port)
        server.starttls()
    else:
        server = smtplib.SMTP_SSL(host, port)

    server.login(user, password)
    server.send_message(msg)
    server.quit()
    print("E-mail enviado para", to_email)

if __name__ == "__main__":
    main()
