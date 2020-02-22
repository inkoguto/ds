import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ds",
    version="0.0.3",
    author="apawcenis",
    author_email="andrzej.pawcenis@gmail.com",
    description="a package with simple data structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inkoguto/ds",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)