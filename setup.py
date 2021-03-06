try:
    from setuptools import setup
    from setuptools import find_packages
    packages = find_packages()
except ImportError:
    from distutils.core import setup
    import os
    packages = [x.strip('./').replace('/','.') for x in os.popen('find -name "__init__.py" | xargs -n1 dirname').read().strip().split('\n')]

setup(
    name='simuvex',
    version='6.7.7.27',
    packages=packages,
    install_requires=[
        'angr',
    ],
    description="A compatibility layer for simuvex's removal.",
    url='https://github.com/angr/simuvex',
)
