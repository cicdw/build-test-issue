import build_test


def test_config():
    assert isinstance(build_test.config, str)
