import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='buildcdf',
    version='1',
    author='Lucas Barsand',
    author_email='barsandlucas@gmail.com',
    description='''Python package to generate input data for Cumulative Distribution Function
                 (CDF) plots.''',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/barsand/buildcdf',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
