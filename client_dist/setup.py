from setuptools import setup, find_packages

setup(name='ICQ_client_study',
      version='0.1.3',
      description='ICQ_client_study',
      author='Evseev Yurii',
      author_email='mousedrw@ya.ru',
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
