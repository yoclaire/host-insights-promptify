from setuptools import setup, find_packages

setup(
    name="host-insights-promptify",
    version="0.1.0",
    author="claire young",
    author_email="yoclaire@pm.me",
    description="A CLI tool to gather and format system insights into an AI-ready prompt.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yoclaire/host-insights-promptify",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "docker==7.1.0",
        "psutil==6.0.0",
        "requests==2.32.3",
        "urllib3==2.2.2",
        "charset-normalizer==3.3.2",
        "idna==3.7",
        "certifi==2024.7.4",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'host-insights-promptify=host_insights_promptify.cli:main',
        ],
    },
)