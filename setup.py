from setuptools import setup, find_packages


setup(
    name="bard",
    version="0.0.1",
    author="Mathias Darr",
    author_email="mddarr@gmail.com",
    packages=find_packages(),
    entry_points={
        "bard.init": [],
        "console_scripts": ["bard = bard.manage:cli"],
    }
)