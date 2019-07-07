import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyshikiapi",
    version="1.0.1",
    author="a68366",
    description="Python wrapper for shikimori API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a68366/pyshikiapi",
    packages=['pyshikiapi'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests-oauthlib"]
)
