from setuptools import setup, find_packages

setup(
    name='jghfmanager',
    version='0.1.0',
    author='J.Guillaume D-Isabelle',
    description='A Python module jghfmanager',
    url='https://github.com/jgwill/jghfmanager',
    packages=find_packages(),
    install_requires=[
        "tlid",
        "requests",
        "jgcmlib",
        "huggingface_hub",
    ],
    entry_points={
        'console_scripts': [
            "jghfinference = jghfmanager.jgthfcli:main",
        ]
    },
)
