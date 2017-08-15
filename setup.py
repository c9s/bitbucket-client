from setuptools import setup

requirements = [
    'requests',
    'oauthlib',
    'requests_oauthlib',
    'click',
    'PyYAML',
    'pprint',
    'tabulate'
]
test_requirements = [ ]
setup(name='bitbucket',
      version='0.0.1',
      description='bitbucket client',
      author='Yo-An lin',
      author_email='yoanlin93@gmail.com',
      packages=['bitbucket'],
      install_requires=requirements,
      tests_require=test_requirements
      )
