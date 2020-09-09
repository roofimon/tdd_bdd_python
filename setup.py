from setuptools import setup, find_packages
setup(
    name='next_lib',
    packags=find_packages(where='src'),
    package_dir={'': 'src'},
)