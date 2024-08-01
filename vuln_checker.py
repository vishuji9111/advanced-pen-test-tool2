import requests
from src.logger import logger

def check_xss(url):
    logger.info(f"Checking {url} for XSS vulnerabilities...")
    payload = "<script>alert('XSS')</script>"
    response = requests.get(url + payload)
    if payload in response.text:
        logger.warning("XSS vulnerability detected!")
        return "XSS vulnerability detected!"
    else:
        logger.info("No XSS vulnerability found.")
        return "No XSS vulnerability found."

def check_sql_injection(url):
    logger.info(f"Checking {url} for SQL Injection vulnerabilities...")
    payload = "' OR '1'='1"
    response = requests.get(url + payload)
    if "SQL syntax" in response.text:
        logger.warning("SQL Injection vulnerability detected!")
        return "SQL Injection vulnerability detected!"
    else:
        logger.info("No SQL Injection vulnerability found.")
        return "No SQL Injection vulnerability found."

def check_open_redirect(url):
    logger.info(f"Checking {url} for Open Redirect vulnerabilities...")
    payload = "/redirect?url=https://evil.com"
    response = requests.get(url + payload)
    if response.status_code == 302 and 'evil.com' in response.headers.get('Location', ''):
        logger.warning("Open Redirect vulnerability detected!")
        return "Open Redirect vulnerability detected!"
    else:
        logger.info("No Open Redirect vulnerability found.")
        return "No Open Redirect vulnerability found."

def check_vulnerabilities(url):
    results = []
    results.append(check_xss(url))
    results.append(check_sql_injection(url))
    results.append(check_open_redirect(url))
    return "\n".join(results)
