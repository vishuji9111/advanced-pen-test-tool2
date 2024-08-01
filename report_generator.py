import os
from src.logger import logger

def generate_html_report(filename, scan_results, vuln_results):
    logger.info(f"Generating HTML report: {filename}")
    report_content = f"""
    <html>
    <head><title>Penetration Testing Report</title></head>
    <body>
        <h1>Penetration Testing Report</h1>
        <h2>Network Scan Results:</h2>
        <pre>{scan_results}</pre>
        <h2>Vulnerability Scan Results:</h2>
        <pre>{vuln_results}</pre>
    </body>
    </html>
    """
    with open(filename, 'w') as file:
        file.write(report_content)
    logger.info(f"HTML report saved to {filename}")

def main():
    from src.config import load_config
    from src.scanner import scan_and_report
    from src.vuln_checker import check_vulnerabilities

    config = load_config()
    target_ip = config['target_ip']
    target_url = config['target_url']
    
    scan_results = scan_and_report(target_ip)
    vuln_results = check_vulnerabilities(target_url)
    generate_html_report('penetration_test_report.html', scan_results, vuln_results)

if __name__ == "__main__":
    main()
