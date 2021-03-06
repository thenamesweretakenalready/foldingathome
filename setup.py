from distutils.core import setup

setup(
    name="foldingathome",
    packages=["foldingathome"],
    version="0.1.6",
    license="MIT Licence",
    description="A Python wrapper for the Folding@Home API.",
    author="leet_hakker",
    author_email="leet_haker@cyber-wizard.com",
    url="https://github.com/thenamesweretakenalready/foldingathome/",
    download_url="https://github.com/thenamesweretakenalready/foldingathome/archive/v0.1.6.tar.gz",
    keywords=["API wrapper", "Python", "Folding@Home"],
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
