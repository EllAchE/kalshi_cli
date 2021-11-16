from setuptools import setup

setup(
    name='kalshi.cli',
    entry_points={
        'console_scripts': [
            'kalshi = kalshi.cli:main',
        ],
    }
)