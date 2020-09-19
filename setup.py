import setuptools


def get_description():
    with open("README.md", 'r') as f:
        return f.read()


setuptools.setup(
    name="stateless-defaults",
    version="1.0.0",
    author="Yam Tirosh",
    author_email="yam.tirosh@gmail.com",
    description="Eliminate default argument caching from your functions!",
    long_description=get_description(),
    py_modules=["stateless_defaults"],
    install_requires=[],
    keywords="default arguments caching stateless",
    classifiers=["Operating System :: OS Independent"],
)
