import setuptools

# Open and read the contents of the README.md file for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Version of the package
__version__ = "0.0.0"

# Metadata about the package
REPO_NAME = "Chicken-Disease-Classification"
AUTHOR_USER_NAME = "vbabua"
SRC_REPO = "ChickenDiseaseClassification"
AUTHOR_EMAIL = "babuvadakemu@gmail.com"

# Setup configuration for the package
setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python package for CNN app",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src")
)