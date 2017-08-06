from setuptools import setup

setup(
  name = 'realtime_talib',
  packages = ['realtime_talib'], # this must be the same as the name above
  version = '0.23',
  description = 'Generate Realtime technical indicators for algotrading/fun',
  author = 'Michael Usachenko',
  author_email = 'meu2@illinois.edu',
  url = 'https://github.com/themichaelusa/realtime_talib', # use the URL to the github repo
  download_url = 'https://github.com/themichaelusa/realtime_talib/archive/0.23.tar.gz', # I'll explain this in a second
  install_requires=['TA-Lib', 'numpy'],
  keywords = ['realtime', 'talib'], # arbitrary keywords
  classifiers = [],
)