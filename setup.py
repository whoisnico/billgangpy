from setuptools import setup, find_packages

setup(
    name='billgangpy',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',  
    ],
    description='Ein Wrapper für die Billgang API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ihr Name',
    author_email='Ihre Email',
    url='https://github.com/whoisnico/billgangpy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
