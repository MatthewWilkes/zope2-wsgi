from setuptools import setup, find_packages


setup(name='policy',
    version='1.0dev',
    url='http://localhost',
    license='Private',
    description='Policy',
    author='Company',
    author_email='info@company.com',
    long_description='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'PasteScript',
#        'Plone',
        'Products.ZSQLMethods',
        'repoze.retry',
        'repoze.tm2',
        'repoze.vhm',
        'setuptools',
        'Products.PythonScripts',
        'Products.BTreeFolder2',
        'Products.StandardCacheManagers',
        'WebError',
        'Zope2',
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
    },
)
