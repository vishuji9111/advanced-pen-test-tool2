from setuptools import setup, find_packages

def readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name='advanced-pen-test-tool',
    version='0.2',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'nmap-python',
        'requests',
        'beautifulsoup4',
        'pandas',
        'lxml',
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'flake8',
            'mypy',
            'black',
            'isort',
        ],
        'doc': [
            'sphinx',
            'sphinx-rtd-theme',
        ],
    },
    entry_points={
        'console_scripts': [
            'scanner=src.scanner:scan_and_report',
            'vuln_check=src.vuln_checker:check_vulnerabilities',
            'report=src.report_generator:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Topic :: Security',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    author='Your Name',
    author_email='your.email@example.com',
    description='A comprehensive tool for automated penetration testing',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/advanced-pen-test-tool',
    project_urls={
        'Bug Tracker': 'https://github.com/yourusername/advanced-pen-test-tool/issues',
        'Documentation': 'https://github.com/yourusername/advanced-pen-test-tool/wiki',
        'Source Code': 'https://github.com/yourusername/advanced-pen-test-tool',
    },
    include_package_data=True,
    zip_safe=False,
)
