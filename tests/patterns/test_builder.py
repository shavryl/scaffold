import pytest
from codesity.patterns.builder import main

# add custom variant
# try add inheritance
# mb check other vars


def test_main():
    main_ = main()
    assert main_

