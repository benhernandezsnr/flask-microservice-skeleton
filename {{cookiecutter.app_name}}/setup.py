from setuptools import find_packages, setup

setup(
    name='flask-microservice',
    version='0.1',
    description='Flask Microservice Skeleton',
    author='',
    author_email='',
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    install_requires=[
        'Flask-Script==2.0.5',
        'Flask-SQLAlchemy',
        'Flask==0.10.1'
    ],
    include_package_data=True,
    zip_safe=False,
)
