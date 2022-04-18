"""This module contains the security-related functions for the Smg88 package.

Most of the objects in this module have their metaclass being of this class, namely 'Security'
This means that each binding (such as methods or properties) each have a security level from 0 to 69, where 0 is the most secure and 69 is the least secure.
"""


class Security(type):
  ...
