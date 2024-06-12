from unittest import TestCase

from cwinsdk.shared.guiddef import GUID


class CwinsdkTest(TestCase):
    def test_guid(self):
        guidstr = "50127dc3-0f36-415e-a6cc-4cb3be910b65"
        result = str(GUID.from_str(guidstr))
        self.assertEqual(guidstr, result)

    def test_all_imports(self):
        from cwinsdk import windows  # noqa: F401
