from src.qr_generator import (
    is_valid_url,
    looks_like_domain,
    normalize_url,
    normalize_file_extension
)


def test_is_valid_url():
    assert is_valid_url("https://amazon.com") is True
    assert is_valid_url("http://google.com") is True
    assert is_valid_url("amazon.com") is False
    assert is_valid_url("not a url") is False


def test_looks_like_domain():
    assert looks_like_domain("amazon.com") is True
    assert looks_like_domain("www.google.com") is True
    assert looks_like_domain("https://amazon.com") is False
    assert looks_like_domain("hello world") is False


def test_normalize_url():
    assert normalize_url("amazon.com") == "https://amazon.com"
    assert normalize_url("https://amazon.com") == "https://amazon.com"
    assert normalize_url("hello") == "hello"


def test_normalize_file_extension():
    assert normalize_file_extension("png") == "png"
    assert normalize_file_extension(".png") == "png"
    assert normalize_file_extension("jpeg") == "jpg"
    assert normalize_file_extension("JPG") == "jpg"