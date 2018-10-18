from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='DiscordBot',
    version='0.1.0',
    description='Just my sample DiscordBot.',
    long_description=readme,
    author='Santeri Hetekivi',
    author_email='programming@hetekivi.com',
    url='https://github.com/SanteriHetekivi/DiscordBot',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
      'nose',
      'sphinx',
      'python-dotenv',
      'discord.py'
    ],
    dependency_links=[
      'https://github.com/Rapptz/discord.py/archive/rewrite.zip#egg=discord.py'
    ],
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'DiscordBot=DiscordBot:main',
        ],
    },
)

