from setuptools import setup, find_packages


setup(name='avocado-qemu',
      description='Avocado Qemu SubFramwrok',
      version=open("VERSION", "r").read().strip(),
      author='Avocado Developers',
      author_email='avocado-devel@example.com',
      url='http://avocado-framework.github.io/',
      packages=['avocado_qemu'],
      include_package_data=True,
      install_requires=['avocado-framework']
      )
