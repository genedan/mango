import setuptools

from mango.constants import BUILD_VERSION

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mango_act",
    version=BUILD_VERSION,
    author="Gene Dan",
    author_email="genedan@gmail.com",
    description="A Python library based on the papers of Donald Mango",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/genedan/mango",
    project_urls={
        "Documentation": "https://genedan.com/mango/docs"
    },
    # install_requires=['numpy', 'scipy', 'python-dateutil'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.10.0',
)
