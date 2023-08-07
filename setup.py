import setuptools

with open("README.md") as f:
    long_desc= f.read()

__version__ = "0.0.1"


REPO_NAME = "mlops-with-mlflow"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author="crazy-bot",
    author_email="guhanilima45@gmail.com",
    description="A demo ML project",
    long_description=long_desc,
    long_description_content = "text/markdown",
    url="https://github.com/crazy-bot/mlops-with-mlflow",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)