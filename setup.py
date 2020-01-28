import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='emfwebcrawler',
    version='0.1.4',
    author="Erik Fabry",
    author_email="erikfabry@gmail.com",
    license="MIT",
    description="Basic web crawler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Max1mum4444/emf-web-crawler",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'beautifulsoup4',
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
