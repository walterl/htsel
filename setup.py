from setuptools import setup

import htsel


with open('README.md') as readme:
    long_description = readme.read()


with open('requirements.txt') as req:
    requirements = [l.strip() for l in req.read().split('\n') if l.strip()]


setup(
    name='htsel',
    version=htsel.__version__,

    author=htsel.__author__,
    author_email=htsel.__email__,

    description=htsel.__summary__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license=htsel.__license__,
    url=htsel.__uri__,
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Lnaguage :: Python :: 3',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML',
    ],

    py_modules=['htsel'],
    entry_points={
        'console_scripts': [
            'htsel = htsel:main',
        ],
    },

    python_requires='>=3',
    install_requires=requirements,
)
