# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:30:48 2022

@author: DarkLegacy
"""


from num2words import num2words
  
# Most common usage.
print(num2words(36))
  
# Other variants, according to the type of article.
print(num2words(36, to = 'ordinal'))
print(num2words(36, to = 'ordinal_num'))
print(num2words(36, to = 'year'))
print(num2words(36, to = 'currency'))
  
# Language Support.
print(num2words(360000, lang ='en_IN'))


