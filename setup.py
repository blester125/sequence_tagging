from setuptools import setup, find_packages

setup(
    name="sequence_tagging",
    version="0.1.0",
    description="Sequence Tagging powered by the Averaged Perceptron.",
    long_description=open('README.md').read(),
    author="Brian Lester",
    author_email="blester125@gmail.com",
    license="MIT",
    packages=find_packages(),
    package_data={
        'sequence_tagging': [
            'sequence_tagging/data/model.p',
            'sequence_tagging/data/tagdict.p',
        ],
    },
    include_package_data=True,
)
