from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='LunaDB',
      version='0.5.2',
      description='Lightweight REST Sever framework, based on bottle',
      author='Christian Schweigel',
      author_email='',
      url='https://github.com/swip3798/LunaDB',
      packages=['AJAS'],
      long_description = long_description,
      long_description_content_type="text/markdown",
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3 :: Only",
          "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
          "Operating System :: OS Independent",
          "Development Status :: 3 - Alpha"
      ],
      install_requires=['bottle==0.12.16']
)