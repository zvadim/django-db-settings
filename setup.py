from setuptools import setup, find_packages
import os

package = 'db_settings'

setup(
    name='django-db-settings',
    version='0.1',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    author='Zabiiaka Vadim',
    author_email='v.zabiiaka@gmail.com',
    packages=find_packages(),
    package_data = {
        'db_settings': [
            'templates/admin/db_settings/settings/*.html',
        ],
    },
    requires = ['django (>=1.3)'],
    license = 'MIT license',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)