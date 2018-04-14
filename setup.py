from setuptools import setup, find_packages

version = "0.1.2"

setup(
    name="sequence_tagging",
    version=version,
    description="Sequence Tagging powered by the Averaged Perceptron.",
    author="Brian Lester",
    author_email="blester125@gmail.com",
    url="https://github.com/blester125/sequence_tagging",
    download_url=f"https://github.com/blester125/sequence_tagging/archive/{version}.tar.gz",
    license="MIT",
    packages=find_packages(),
    package_data={
        'sequence_tagging': [
            'sequence_tagging/data/model.p',
            'sequence_tagging/data/tagdict.p',
        ],
    },
    include_package_data=True,
    keywords=["NLP", "sequence tagging", "ML"],
)
