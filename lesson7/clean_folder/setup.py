from setuptools import setup


setup(name='clean_folder',
      version='0.1.1',
      description='A program for cleaning folders.',
      author='Ihor Bukata',
      author_email='gotoff@meta.ua',
      packages=['clean_folder'],
      install_requires = [],
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:parse_folder']})
