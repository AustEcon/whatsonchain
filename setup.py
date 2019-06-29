from setuptools import find_packages, setup

with open('whatsonchain/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('= ')[1].strip("'")
            break

setup(
    name='whatsonchain',
    version=version,
    description='Whatsonchain API.',
    long_description=open('README.rst', 'r').read(),
    author='AustEcon',
    author_email='AustEcon0922@gmail.com',
    maintainer='AustEcon',
    maintainer_email='AustEcon0922@gmail.com',
    url='https://github.com/AustEcon/whatsonchain',
    download_url='https://github.com/AustEcon/whatsonchain/tarball/{}'.format(version),
    license='MIT',

    keywords=[
        'bitcoinsv',
        'bsv',
        'bitcoin sv',
        'cryptocurrency',
        'payments',
        'tools',
        'wallet',
        'whatsonchain'
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],

    install_requires=['requests'],
    extras_require={},
    tests_require=['pytest'],

    packages=find_packages(),
    entry_points={},
)
