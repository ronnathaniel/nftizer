
import setuptools

PACKAGE = 'nftizer'
VERSION = '0.0.0-dev'
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name=PACKAGE,
    version=VERSION,
    author="ronnathaniel",
    author_email="rnathaniel7@gmail.com",
    short_description="NFT it.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['nftizer'],
    package_data={'nftizer': ['*.pem']},
    python_requires=">=3.6",
    install_requires=required,
    include_package_data=True,
    url="https://github.com/ronnathaniel/how",
    project_urls={
        "Bug Tracker": "https://github.com/ronnathaniel/how/issues"
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=[
        'python',
        'python3',
        'how',
        'howto',
        'howdoi',
        'stackoverflow',
    ],

)