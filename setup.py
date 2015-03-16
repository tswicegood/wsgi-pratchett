import sys
if sys.argv[1] == 'develop':
    from setuptools import setup
else:
    from distutils.core import setup

setup(
    name='wsgi-pratchett',
    version='1.0.1',
    author='Travis Swicegood',
    author_email='development@domain51.com',
    description='GNU Terry Pratchett for WSGI',
    long_description=open("./README.rst").read(),
    packages=['pratchett', ],
    include_package_data=True,
    zip_safe=False,
)
