from distutils.core import setup

__version__ = '0.0.1'

setup(name='accelerando',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Put datasets into AllegroGraph',
      url='https://github.com/tlevine/accelerando',
      packages=['surf','surf.allegro_franz'],
      install_requires = [],
      tests_require = ['nose'],
      version=__version__,
      license='AGPL',
)
