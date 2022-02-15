import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tdd-project-sb",
    version="0.0.1",
    author="Sri Barrow",
    author_email="sribarrow@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sribarrow/tdd_proj_mt",
    project_urls={
        "Bug Tracker": "https://github.com/sribarrow/tdd_proj_mt/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    setup_requires=['pytest-runner', 'flake8','black'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['my-command=tdd_proj.app:main']
    },
)