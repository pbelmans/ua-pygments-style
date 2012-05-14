""" 
A UA style for Pygments
""" 
from setuptools import setup 

setup( 
    name         = 'ua', 
    version      = '1.1', 
    description  = __doc__, 
    author       = "Pieter Belmans", 
    install_requires = ['pygments'],
    packages     = ['ua'], 
    entry_points = '''
    [pygments.styles]
    ua = ua:UAStyle
    '''
) 
