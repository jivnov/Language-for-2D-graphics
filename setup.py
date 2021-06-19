from setuptools import setup

setup(
    name='Language-for-2D-graphics',
    version='1.1',
    packages=['twodim_compiler'],
    url='https://github.com/jivnov/Language-for-2D-graphics',
    license='',
    author='Pawel Bilko, Lizaveta Hurskaya, Andrei Zhyunou',
    author_email='',
    description='A language for creating 2D graphics using relational operations, implemented for Compilers course at AGH UST.',
    install_requires=[
        "antlr4-python3-runtime>=4.9.2",
        "writesvg",
        "enum"
    ],
    entry_points={
        'console_scripts': [
            'twodim=twodim_compiler.main:main'
        ]
    },
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    package_dir={"": "./"},
)
