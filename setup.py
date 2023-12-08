from setuptools import setup, find_packages

setup(
    name='bunkoer',
    version='0.0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bunkoer = bunkoer.main:main',
    ],
    install_requires=[
        # liste des dépendances
    ],
    classifiers=[
        'Development Status :: Alpha',
        'Intended Audience :: Developers',
        'License MIT License',
        'Programming Language :: Python :: 3x',
    ],
)

