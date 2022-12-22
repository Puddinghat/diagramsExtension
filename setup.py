from setuptools import setup

setup(
    name="diagram-test",
    version="0.1.0",
    description="a simple test for diagrams as code packages",
    url='',
    author='matthias wilhelm',
    author_email='matthias.wilhelm@live.de',
    license='MIT',
    packages=['customdiagrams','customicons'],
    package_data={'customicons': ['icons/*.png']},
    include_package_data=True,
)