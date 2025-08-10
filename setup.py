"""
Setup script for the HelloWorld package.
"""

from setuptools import setup, find_packages
import os

# Read the README file for the long description
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Read version from __init__.py
def get_version():
    version_file = os.path.join(here, "src", "helloworld", "__init__.py")
    with open(version_file, encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"')
    raise RuntimeError("Unable to find version string.")

setup(
    name="helloworld",
    version=get_version(),
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple Python package for greeting the world",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/helloworld",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        # Add runtime dependencies here
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "helloworld=helloworld.main:main",
        ],
    },
) 