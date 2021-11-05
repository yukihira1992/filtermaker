def test_version():
    from filtermaker import __version__
    assert type(__version__) == str
