from setuptools import setup
import io

with io.open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="sylk-docs",
    description="A sylk CLI plugin for interacting with docusaurus-sylk plugin for Docusaurus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires="sylk",
    entry_points={"sylk": ["docs = sylk_docs"]},
    py_modules=["sylk_docs"],
    version = "0.0.2",
    python_requires="~=3.7",
    author_email="Sylk Team <contact@sylk.build>",
    url="https://sylk.build/",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
