import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vn_fullname_generator", # Replace with your own username
    version="0.0.1",
    author="Lh Long",
    author_email="lhlong@github.com",
    description="Generate Vietnamese Fullname",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lhlong/vietnamese-fullname-generator",
    project_urls={
        "Bug Tracker": "https://github.com/lhlong/vietnamese-fullname-generator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    package_data={'': ['*.name']},
    include_package_data=True,
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)