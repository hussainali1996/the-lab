"""
This is models file
"""
from __future__ import unicode_literals

from django.db import models


class Test(models.Model):
    """TEST classs"""

    def test_method(self):
        """Test Mthod"""
        print "This is test method {}".format(self)
