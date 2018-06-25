from setuptools import find_packages, setup

setup(
    name='PyIntern',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    desciption='System to manage Interships',
    author='Lays Rodrigues',
    author_email='lays.rodrigues@kde.org',
    install_requires=[
        'Django==2.0.4',
        'django-taggit==0.22.2',
    ])
