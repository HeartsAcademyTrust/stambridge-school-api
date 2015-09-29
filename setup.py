from setuptools import setup

setup(name='HeartAcademyTrust-Api',
      version='1.0',
      description='Django Web Server for all the schools part of the Hearts Academy Trust',
      author='Vasia Shelkov',
      author_email='vasilyshelkov@hotmail.co.uk',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=[
      'Django==1.8',
      'Pillow==2.9.0',
      'django-filter==0.11.0',
      'djangorestframework==3.2.3',
      'django-cors-headers==1.1.0'
      ],
     )
