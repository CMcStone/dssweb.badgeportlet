from setuptools import setup, find_packages
import os

version = '1.2.dev0'

setup(name='dssweb.badgeportlet',
      version=version,
      description="creates a badge portlet based on FSD Member anywhere in the site",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Carol McMasters-Stone',
      author_email='cbeck@ucdavis.edu',
      url='https://github.com/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['dssweb'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'six',
          "plone.app.portlets",
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
