from setuptools import setup

setup(
    name="pycypher",
    version="0.0.1",
    packages=['pycypher'],
    install_requires=['antlr4-python3-runtime'],
    # metadata for upload to PyPI
    author="Mushtaque Ahamed (alias Mizzlr)",
    author_email="mushtaque@codenation.co.in",
    description="""A module to parse cypher in python.""",
    license="Proprietary",
    keywords="Cypher, Open Cypher, Neo4j, Python, Parser, Lexer, ANTLR",
)
