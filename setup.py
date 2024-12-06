from setuptools import setup, find_packages

setup(
    name="Lavender-Icon",
    version="1.0.3",
    description="A pip package for distributing file icons.",
    long_description=open(
        "README.md").read(),
    long_description_content_type="text/markdown",
    author="Zeyu Xie",
    author_email="xie.zeyu20@gmail.com",
    url="https://github.com/Zeyu-Xie/Lavender-Icon",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_data={
        'lavender_icon': ['src/icons.json'],
    },
    python_requires=">=3.6",
)
