from setuptools import setup, find_packages
import sys

readme_file = 'README.md'
try:
    long_description = open(readme_file).read()
except IOError:
    sys.stderr.write("[ERROR] Cannot find file specified as ``long_description`` (%s)\n" % readme_file)
    sys.exit(1)

install_requires = []

setup(name='django-geo-spaas',
      version=0.1,
      long_description=long_description,
      zip_safe=False,
      url='#',
      download_url='#',
      packages=find_packages(),
      include_package_data=True,
      install_requires=install_requires,
      test_suite='runtests.runtests',
      classifiers=['Development Status :: 0 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)