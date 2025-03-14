from setuptools import setup, find_packages

setup(
    name="pokedex",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests==2.32.3",
        "langchain==0.3.2",
        "unstructured",
        "langchain_community",
        "torch",
        "torchvision",
        "transformers",
        "sentence-transformers",
        "pillow",
        "numpy",
        "qdrant-client",
        "selenium"
    ],
    author="Tanatorn Intarapanya",  
    author_email="unkiaura@gmail.com",
    description="Search for pokedex.",
)
