from distutils.core import setup

setup(
    name='createbucket',
    version='0.1.0',
    author='Matt Warren',
    author_email='matt.warren@gmail.com',
    packages=['createbucket'],
    url='https://github.com/mfwarren/createbucket',
    license='LICENSE',
    description='Simple command tool to create S3 Buckets.',
    long_description=open('README.txt').read(),
    install_requires=[
        "boto",
        "inquirer",
    ],
    entry_points={
        'console_scripts': ['createbucket = createbucket.create_s3_bucket:main']
    },
)