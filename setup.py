import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.md")).read()

install_requires = []

setup_requires = []

tests_require = install_requires + []

setup(
    name="bashcolor",
    version="1.0.1",
    description="A simple library to get colors in the bash terminal",
    long_description=README,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Typing :: Typed",
    ],
    author="Stéphane Brunner",
    author_email="stephane.brunner@gmail.com",
    url="https://github.com/sbrunner/bashcolor/",
    packages=find_packages(exclude=["*.tests", "*.tests.*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    entry_points={
        "console_scripts": [
            "print_colors = bashcolor:print_colors",
        ],
    },
    data={"bachcolor": ["py.typed"]},
)
