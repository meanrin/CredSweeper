import pytest

from credsweeper.config import Config
from credsweeper.credentials import LineData
from credsweeper.utils import Util


class TestConstants:

    @pytest.mark.parametrize("line", ["melon = 'banAna'", "melon : 'banAna'", "melon := 'banAna'"])
    def test_separator_common_p(self, config: Config, file_path: pytest.fixture, line: str) -> None:
        pattern = Util.get_keyword_pattern("melon")
        line_data = LineData(config, line, 1, file_path, pattern)
        assert line_data.value == "banAna"

    @pytest.mark.parametrize("line, value",
                             [["'password': b'password'", "password"], ["'password': r'password'", "password"],
                              ["\\'password\\': \\'password\\'", "password"],
                              ["'password': 'ENC(lqjdoxlandicpfpqk)'", "ENC(lqjdoxlandicpfpqk)"],
                              ["'password': 'ENC[lqjdoxlandicpfpqk]'", "ENC[lqjdoxlandicpfpqk]"]])
    def test_keyword_pattern_common_p(self, config: Config, file_path: pytest.fixture, line: str, value: str) -> None:
        pattern = Util.get_keyword_pattern("password")
        line_data = LineData(config, line, 1, file_path, pattern)
        assert line_data.value == value
