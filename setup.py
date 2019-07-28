import setuptools
import ogc_plugins_env as package
from pathlib import Path

README = Path(__file__).parent.absolute() / "readme.md"
README = README.read_text(encoding="utf8")

setuptools.setup(
    name="ogc-plugins-env",
    version=package.__version__,
    author=package.__author__,
    author_email=package.__author_email__,
    description=package.__description__,
    long_description=README,
    long_description_content_type="text/markdown",
    url=package.__git_repo__,
    py_modules=["ogc_plugins_env"],
    entry_points={"ogc.plugins": "Env = ogc_plugins_env:Env"},
    install_requires=[
        "ogc>=0.3.0,<1.0.0",
        "click>=7.0.0,<8.0.0",
        "python-dotenv>=0.10.3,<1.0.0",
    ],
)
