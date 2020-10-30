from setuptools import setup, find_packages

"""
[]
"""

def read(filename):
    return [req.strip() for req in open(filename).readlines()]

setup(
    name="appi2c",
    version="0.1.0",
    description="",
    homepage="Andre Queiroz",
    platform="raspberry",
    packages=find_packages(exclude="/__pycache__, /.vscode"),
    include_package_data=True,
    install_requirements=read("requirements.txt"),
    extras_require={"dev": read("requirements-dev.txt")}
)