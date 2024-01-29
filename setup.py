from setuptools import setup

with open("README.md") as f:
    long_description = f.read()


setup(
    name="fastapi-and-babel",
    version="0.0.4",
    url="https://github.com/heysaeid/fastapi-and-babel",
    license="MIT",
    author="Saeid Noormohammadi",
    author_email="heysaeid92@gmail.com",
    description="Easy to use babel in FastAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "fastapi",
        "babel",
        "fastapi babel",
    ],
    packages=["fastapi_and_babel"],
    zip_safe=False,
    platforms="any",
    install_requires=[
        "Babel==2.13.1",
        "fastapi",
    ],
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Typing :: Typed",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
