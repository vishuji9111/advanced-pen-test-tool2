import unittest
from src.report_generator import generate_html_report
import os

class TestReportGenerator(unittest.TestCase):

    def test_generate_html_report(self):
        generate_html_report('test_report.html', 'Test scan results', 'Test vulnerability results')
        self.assertTrue(os.path.exists('test_report.html'))

if __name__ == '__main__':
    unittest.main()
