import py, pytest

from tests.base import BaseTest


class TestFlakeySetup(BaseTest):

    @pytest.mark.destructive
    def test_flakey_setup(self):
        pass