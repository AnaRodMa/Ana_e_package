from setuptools import find_packages, setup

setup(
    name="TemplatePythonPackage",
    version="0.1.0",
    description="A Minimal Template Python Package",
    url="https://github.com/RealityBending/TemplatePythonPackage",
    author="Ana Rodriguez",
    author_email="anaelisarodma@gmail.com",
    license="M",
    install_requires=["numpy", "pandas", "scipy", "matplotlib"],
    packages=find_packages(),
    zip_safe=False,
)
