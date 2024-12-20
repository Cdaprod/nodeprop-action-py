from setuptools import setup, find_packages

setup(
    name="nodeprop-action",
    version="1.0.0",
    author="Cdaprod",
    author_email="Cdaprod@Cdaprod.dev",  # Replace with your actual email
    description="A GitHub Action to generate nodeprop.config.yaml with repository details",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Cdaprod/nodeprop-action",
    packages=find_packages(),
    install_requires=[
        "PyYAML",
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)