import setuptools
from pathlib import Path

README = Path(__file__).parent.absolute() / 'readme.md'
README = README.read_text(encoding='utf8')

setuptools.setup(
    name="ogc-plugins-env",
    version="0.0.2",
    author="Adam Stokes",
    author_email="adam.stokes@ubuntu.com",
    description="ogc-plugins-env, a ogc plugin for environment discovery",
    long_description=README,
    long_description_content_type='text/markdown',
    url="https://github.com/battlemidget/ogc-plugin-env",
    packages=["ogc_plugins_env"],
    entry_points={"ogc.plugins": "Env = ogc_plugins_env:Env"},
    install_requires=[
        "ogc>=0.1.5,<1.0.0",
        "click>=7.0.0,<8.0.0",
        "python-dotenv==0.10.3",
    ],
)
