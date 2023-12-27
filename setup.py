from setuptools import setup, find_packages

setup(
    name='bunkoer',
    version='0.0.2',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bunkoer=bunkoer.main:run_streamlit',
        ],
    },
    install_requires=[
        'streamlit',
        'streamlit-chat',
        'openai',
        'PyPdf2',
        'fpdf',
        'langchain==0.0.352',
        'langchain-experimental==0.0.47',
        'langchain-community==0.0.6',
        'langchain-core==0.1.3',
        'langsmith==0.0.75',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Assurez-vous que cette ligne correspond à votre licence
        'Programming Language :: Python :: 3',  # Assurez-vous que cette ligne correspond à votre version de Python
    ],
)

