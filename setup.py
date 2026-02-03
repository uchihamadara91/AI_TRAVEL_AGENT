from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="AI TRAVEL PLANNER AGENT",
    version="0.4",
    author="Shankar",
    packages=find_packages(),
    install_requires = requirements,
)