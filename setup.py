from setuptools import setup

setup(name='get_pbq',
    version='0.2.6',
    description='Getting per base quality score from fastq/fastq.gz',
    author='Semar Petrus',
    packages=['get_pbq'],
    entry_points = {
        'console_scripts': ['get_pbq=get_pbq.get_pbq:main']},
    install_requires=['biopython'])
