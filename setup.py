import setuptools

setuptools.setup(
    name="topsis",
    version="0.0.1",
    author="Seyedsaman Emami",
    author_email="saman.emami@gmail.com",
    description="Technique for Order of Preference by Similarity to Ideal Solution",
    packages=["topsis"],
    install_requires=['numpy', 'pandas', 'scipy'],
    classifiers=("Programming Language :: Python :: 3")
)
