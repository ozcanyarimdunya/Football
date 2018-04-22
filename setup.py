from setuptools import find_packages, setup

EXCLUDE_FROM_PACKAGES = ['tests', 'tests.core']

setup(
    name='Football',
    version='1.1.0',
    url='https://github.com/ozcanyarimdunya/Football',
    license='MIT',
    author='ozcanyarimdunya',
    author_email='ozcanyd@gmail.com',
    description='Simple football scraper',
    python_requires='>=3.6',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    scripts=['football/bin/rating.py'],
    entry_points={'console_scripts': ['rating = football.core.management:execute_from_command_line']},
    install_requires=['PyQt5', 'requests', 'beautifulsoup4'],
    zip_safe=False,
)
