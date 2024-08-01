import nmap
from src.logger import logger

def scan_ports(target_ip):
    nm = nmap.PortScanner()
    logger.info(f"Scanning {target_ip} for open ports...")
    nm.scan(target_ip, arguments='-T4 -A')  # Aggressive scan
    scan_result = nm.csv()
    logger.debug(f"Scan results: {scan_result}")
    return scan_result

def scan_and_report(target_ip):
    return scan_ports(target_ip)
