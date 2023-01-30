from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="instagram_crawler",
    version="0.0.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=requirements,
)


