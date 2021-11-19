from setuptools import setup

setup(
    name="cuteroll",
    version="1.0.0",
    description="Download shows from crunchyroll",
    url="https://github.com/insidewhy/cuteroll",
    author="insidewhy",
    license="MIT",
    scripts=["bin/cuteroll"],
    packages=["cuteroll"],
    install_requires=[
        "requests",
        "colorama",
        "termcolor",
        "pyxdg",
        "pysocks",
        "cryptography",
    ],
    tests_requires=[],
    zip_safe=False,
)
