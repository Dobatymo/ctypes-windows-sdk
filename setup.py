from setuptools import setup

with open("README.md", encoding="utf-8") as fr:
    long_description = fr.read()

setup(
    author="Dobatymo",
    name="ctypes-windows-sdk",
    version="0.0.12",
    url="https://github.com/Dobatymo/ctypes-windows-sdk",
    description="Ctypes port of Windows SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: System :: Operating System",
    ],
    packages=["cwinsdk", "cwinsdk.km", "cwinsdk.km.crt", "cwinsdk.shared", "cwinsdk.um"],
    python_requires=">=3.7",
)
