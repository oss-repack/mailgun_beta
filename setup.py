import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mailgun_demo1', # Replace with your own username
    version="1.0.4",
    author="diskovod",
    author_email="diskovodik@gmail.com",
    description="Mailgun beta project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/diskovod/mailgun_beta",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # install_requires=['requests>=2.25.0'],
    install_requires=['requests'],
    python_requires='>=3.6',
)