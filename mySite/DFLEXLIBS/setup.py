from setuptools import setup, find_packages

setup(
    name="controls",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["*.png"]
    }
)