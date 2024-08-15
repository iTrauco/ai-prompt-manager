from setuptools import setup, find_packages

setup(
    name="prompt_manager",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "click",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "prompt-manager=prompt_manager.cli:cli",
        ],
    },
)
