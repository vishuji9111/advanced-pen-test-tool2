import unittest
from src.scanner import scan_ports

class TestScanner(unittest.TestCase):

    def test_scan_ports(self):
        result = scan_ports('127.0.0.1')
        self.assertIn('1/tcp', result)  # Adjust this according to expected output

if __name__ == '__main__':
    unittest.main()
