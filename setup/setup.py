# setup.py
from setuptools import setup, find_packages

setup(
    name="SICILI.SCI.OS",  # Name of your module
    version="1.0.0",
    packages=find_packages(),  # Automatically find packages in your project directory
    include_package_data=True,  # Include non-code files (if any, e.g., readme)
    entry_points={
        "console_scripts": [
            "SICILI.SCI.OS=sicilios.main:run",  # Entry point for command-line execution
        ]
    },
    install_requires=[
        "scratchattach",  # Third-party dependencies
    ],  # Add any dependencies here
    description="A command-line OS  module",
    author="Shahzain Khan/ArtificialXDev",
    author_email="shahzaingenious@gmail.com",
    url="https://github.com/yourgithub/sicilios",  # GitHub or project URL
)
