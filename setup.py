from setuptools import setup, find_packages

setup(
    name='bunkoer',
    version='0.0.9-dev',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bunkoer=bunkoer.main:run_streamlit',
        ],
    },
    install_requires=[
        # liste des dépendances
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Assurez-vous que cette ligne correspond à votre licence
        'Programming Language :: Python :: 3',  # Assurez-vous que cette ligne correspond à votre version de Python
    ],
)

