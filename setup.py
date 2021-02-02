import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ubConvert",
    version="0.0.2",
    author="ZennDogg",
    author_email="",
    description="A small math formula conversion package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zazen000/ubConvert.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)