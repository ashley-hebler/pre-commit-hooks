from setuptools import find_packages
from setuptools import setup

setup(
    name='tt-pre-commit-hooks',
    description='Pre-commit hooks',
    url='https://github.com/ashley-hebler/pre-commit-hooks',
    version='1.0.0',
    platforms='linux',
    packages=find_packages('.'),
    install_requires=[
        'lxml',
    ],
    entry_points={
        'console_scripts': [
            'html_target_attribute_check = hooks.html_target_attribute_check:main',
        ],
    },
)
