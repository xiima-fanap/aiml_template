from setuptools import setup


def _read_requirements(path="./requirements.txt"):
    """Load requirements.txt as a list of strings."""
    
    with open(path, encoding='utf-8', errors='ignore') as file:
        install_requires = file.readlines()

    return install_requires


# Module information
setup(
    name="aiml_template",
    # Semantic Versioning 2.0.0
    version="0.1.0",
    author="Hamid Mohammadi",
    author_email="sandstormeatwo@gmail.com",
    description=(
        "A template base-line project to act as initial empty repo for AIML"
        " team packages"
    ),
    packages=[
        "aiml_template",
        "aiml_template.exceptions",
    ],
    include_package_data=True,
    install_requires=_read_requirements()
)
