from setuptools import find_packages, setup
import setuptools

try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements

# Read in the README for the long description on PyPI
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

reqs = parse_requirements("requirements.txt", session=False)
install_requires = [str(ir.req) for ir in reqs]

setup(
      name='mphyspy',
      version='0.1.9.6',
      description='Python3 library for calculating college modern physics',
      long_description=readme,
      long_description_content_type="text/markdown",
      url='https://github.com/eunchan1001/mphyspy.git',
      author='eunchan1001',
      author_email='eunchan1001@gmail.com',
      license='MIT',
      install_requires=install_requires,
      packages=find_packages(),
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          'Programming Language :: Python :: 3.7',
          ],
      zip_safe=False)
