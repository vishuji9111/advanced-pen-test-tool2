import unittest
from src.vuln_checker import check_xss, check_sql_injection, check_open_redirect

class TestVulnChecker(unittest.TestCase):

    def test_check_xss(self):
        result = check_xss('http://test.url')
        self.assertIn("No XSS vulnerability found.", result)

    def test_check_sql_injection(self):
        result = check_sql_injection('http://test.url')
        self.assertIn("No SQL Injection vulnerability found.", result)

    def test_check_open_redirect(self):
        result = check_open_redirect('http://test.url')
        self.assertIn("No Open Redirect vulnerability found.", result)

if __name__ == '__main__':
    unittest.main()
