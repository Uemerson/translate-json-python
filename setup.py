from importlib.metadata import entry_points
from setuptools import find_packages
from setuptools import setup

setup(
    name="Uemerson Pinheiro Junior",
    version="1.0.0",
    description="A program to translate a JSON file.",
    author="Uemerson Pinheiro Junior",
    author_email="uemersonpinheirojunior@gmail.com",
    url="https://github.com/Uemerson/translate-json-python",
    install_requires=["googletrans==3.1.0a0"],
    packages=find_packages(),
    entry_points={"console_scripts": ["translate-json-cli = translate_json.main:main"]},
)
