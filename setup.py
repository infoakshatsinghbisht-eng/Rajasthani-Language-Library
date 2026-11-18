# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

long_desc = ""
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_desc = fh.read()

setup(
    name="rajasthani",
    version="1.0.0",
    author="Akshat Singh Bisht",
    author_email="infoakshatsinghbisht@gmail.com",
    maintainer="Akshat Singh Bisht",
    maintainer_email="infoakshatsinghbisht@gmail.com",
    description="Rajasthani (राजस्थानी) Language Standard Library: Multi-Dialect Translation, Morphological Conjugation, Voice Processing & Cultural Heritage",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/infoakshatsinghbisht-eng/Rajasthani-Language-Library",
    project_urls={
        "Homepage": "https://akshatsinghbisht.com/",
        "GitHub": "https://github.com/infoakshatsinghbisht-eng/Rajasthani-Language-Library",
        "LinkedIn": "https://www.linkedin.com/in/akshat-singh-bisht-digital-performance-marketing-specialist/",
        "Amazon Author": "https://www.amazon.com/stores/Akshat-Singh-Bisht/author/B0D5TYDT28",
        "ResearchGate": "https://www.researchgate.net/profile/Akshat-Bisht-8",
        "Bug Tracker": "https://github.com/infoakshatsinghbisht-eng/Rajasthani-Language-Library/issues",
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "rajasthani.lexicon": ["data/*.json"],
        "rajasthani.culture": ["data/*.json"],
        "rajasthani.web": ["static/*.*"],
    },
    entry_points={
        "console_scripts": [
            "rajasthani=rajasthani.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
    ],
    python_requires=">=3.9",
)
