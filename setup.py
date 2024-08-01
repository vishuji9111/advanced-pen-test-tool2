from setuptools import setup, find_packages

setup(
    name='advanced-pen-test-tool',
    version='0.2',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'nmap',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'scanner=src.scanner:scan_and_report',
            'vuln_check=src.vuln_checker:check_vulnerabilities',
            'report=src.report_generator:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    author='Your Name',
    author_email='your.email@example.com',
    description='A comprehensive tool for automated penetration testing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/advanced-pen-test-tool',
)
