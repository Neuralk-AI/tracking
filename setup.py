import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tracking",
    version="0.0.1",
    author="Alexandre Pasquiou",
    author_email="alex@neuralk-ai.com",
    description="Tracking tools for training, inference, etc ...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Neuralk-AI/tracking",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "torch",
        "PyYAML",
        "matplotlib",
        "tqdm",
        "scikit-learn",
        "pytest",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
)
