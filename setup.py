from setuptools import setup

setup(
    name='VoidServiceControl',
    version='0.2',
    url='https://git.orudo.ru/trueold89/void-service-control',
    author='trueold89',
    author_email='trueold89@orudo.ru',
    description="A simple script that will allow you to manage runit services in Void Linux",
    packages=['VoidServiceControl'],
    long_description=open('README.md').read(),
    entry_points={
        "console_scripts": ["vsc = VoidServiceControl.main:main"]
    },
    package_data={
        'VoidServiceControl': ['*.json'],
    },
)
