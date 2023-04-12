from setuptools import setup


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="fastapi-and-babel",
    version='0.0.1',
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
        "Babel",
        "fastapi",
    ],
    classifiers=[
        "Framework :: FastAPI",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)