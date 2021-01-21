import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="danger",
  version="0.0.1",
  author="wushiyong",
  author_email="wushiyong1209@gmail.com",
  description="A python tool package",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/danger812/danger",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: Apache-2.0 License",
  "Operating System :: OS Independent",
  ],
)