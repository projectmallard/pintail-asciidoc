from setuptools import setup

setup(
    name='pintail-asciidoc',
    version='0.3',
    description='Use AsciiDoc on Pintail sites.',
    packages=['pintail', 'pintail.asciidoc'],
    namespace_packages=['pintail'],
    install_requires=['pintail>=0.3'],
    author='Shaun McCance',
    author_email='shaunm@gnome.org',
    license='GPLv2+',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: XML',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)'
    ],
)
