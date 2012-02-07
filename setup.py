import os

from setuptools import setup, find_packages

# The version of the wrapped library is the starting point for the
# version number of the python package.
# In bugfix releases of the python package, add a '-' suffix and an
# incrementing integer.
# For example, a packaging bugfix release version 1.4.4 of the
# js.jquery package would be version 1.4.4-1 .

version = '4.3.1'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.jqgrid',
    version=version,
    description="Fanstatic packaging of jqgrid",
    long_description=long_description,
    classifiers=[],
    keywords='jqgrid',
    author='Fanstatic Developers',
    author_email='fanstatic@googlegroups.com',
    url='https://github.com/do3cc/js.jqgrid',
    license='',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=[
        'fanstatic',
        'js.jquery',
        'js.jqueryui',
        ],
    entry_points={
        'fanstatic.libraries': [
            'jqgrid = js.jqgrid:library',
            ],
        },
    )
