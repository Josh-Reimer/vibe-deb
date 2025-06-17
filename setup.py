from setuptools import setup

setup(
    name="hello-world-pyqt",
    version="1.0.0",
    description="A simple Hello World application using PyQt6",
    author="Your Name",
    author_email="your.email@example.com",
    py_modules=["hello_world"],
    install_requires=[
        "PyQt6",
    ],
    entry_points={
        "console_scripts": [
            "hello-world-pyqt=hello_world:main",
        ],
    },
) 