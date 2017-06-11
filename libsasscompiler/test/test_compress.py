
import os
from unittest import TestCase

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "libsasscompiler.test.demoapp.demoapp.settings")


class TestCustiom(TestCase):
    def test_wathever(self):
        a = True
        self.assertTrue(a)
