from setuptools import find_packages, setup

setup(
    name="homework2",
    python_requires='>=3.4',
    packages=find_packages(),
    version='0.1.0',
    description="This is homework2 project",
    author="Egor Morozov",
    install_requires=[
        "pydantic==1.8.2",
        "uvicorn==0.13.4",
        "pandas==1.1.5",
        "fastapi==0.65.1",
        "scikit_learn==0.24.2"
    ],
    license="MIT",
)