import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="marcopytools-marc0u",  # Replace with your own username
    version="0.0.1",
    author="Marco Urriola",
    author_email="marco.urriola@gmail.com",
    description="My tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marc0u/marcopytools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
