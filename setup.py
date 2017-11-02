"""dndiscord setup"""
# TODO
from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="dndiscord",
    version="3.1.0", # new tag
    description="A DND Dungeon Master assistant, character creation "
                "assistant, and general campaign help and logging Discord "
                "Bot.",
    long_description=readme(),
    author="Nathan Klapstein",
    author_email="nklapste@ualberta.ca",
    url="https://github.com/nklapste/DNDiscord",
    download_url="",
    license="MIT",
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(exclude=["test"]),
    package_data={
        "": ["README.md"],
    },
    install_requires=[
        "bot.py"
    ],
    tests_require=["pytest"],
    entry_points={
        "console_scripts": ["dndiscord = dndiscord.__main__:main"],
    },
)
