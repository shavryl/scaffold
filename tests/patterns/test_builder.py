import pytest
from codesity.patterns.builder import main


def test_main():
    main_ = main()
    assert main_

