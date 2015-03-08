import os
from setuptools import setup, find_packages

package = 'dynamic_settings'

setup(
    name='django-dynamic-settings',
    version='0.1.0',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    author='Zabiiaka Vadym',
    author_email='v.zabiiaka@gmail.com',
    url='https://github.com/zvadim/django-dynamic-settings',
    keywords=['django', 'settings', 'dynamic'],
    packages=find_packages(),
    package_data={
        'dynamic_settings': [
            'templates/admin/dynamic_settings/settings/*.html',
        ],
    },
    requires=['django (>=1.3)'],
    license='MIT license',
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