from setuptools import setup, find_packages

with open("readme.md", "r", encoding="utf-8") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="suzy-bank",
    version="0.0.6",
    author="sudo2dev",
    author_email="sudo2dev@gmail.com",
    description="Suzy Bank Toy Project",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sudo2dev/suzy-bank",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'suzy_bank = suzy_bank.main:main',  # ajusta ao nome do módulo e função principal
        ]
    },
)