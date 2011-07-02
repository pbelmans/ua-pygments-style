# -*- coding: utf-8 -*-
"""
    pygments.styles.ua
    ~~~~~~~~~~~~~~~~~~~~~~

    A style based on the University of Antwerp's color scheme
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Whitespace

class UAStyle(Style):
    default_style = ""
    
    # the three main colours, as per Nico Schlömer's
    # great UniversiteitAntwerpenTheme for beamer
    uablue = '#003d64'
    uared = '#7e002f'
    vividbrown = '#d79a46'
    green = '#007e11'
    
    styles = {
        Whitespace:                 '#bbbbbb',
        
        Comment:                    'italic #888888',
        Comment.Preproc:            'noitalic ' + uablue,
        Comment.Special:            'noitalic ' + uablue,
        
        Keyword:                    green,
        Keyword.Constant:           uablue,
        Keyword.Pseudo:             uablue,
        Keyword.Reserved:           'bold ' + uared,
        Keyword.Type:               'bold ' + uared,
        
        Operator.Word:              green,
        
        Name.Attribute:             uablue, 
        Name.Builtin:               uablue,
        Name.Builtin.Pseudo:        'italic ' + vividbrown,
        Name.Class:                 'bold ' + uablue,
        Name.Constant:              vividbrown,
        Name.Decorator:             'italic ' + uared,
        Name.Entity:                'italic ' + vividbrown,
        Name.Exception:             uared,
        Name.Function:              'bold ' + uablue,
        Name.Label:                 'bold ' + green,
        Name.Namespace:             'bold ' + uablue,
        Name.Tag:                   uablue,
        Name.Variable:              'italic',
        
        String:                     'italic #5566aa',
        String.Escape:              'noitalic ' + vividbrown,
        String.Interpol:            uared,
        String.Regex:               '#cc7799',
        Number:                     '#002255',
        
        Error:                      'bg:#F00'
    }

