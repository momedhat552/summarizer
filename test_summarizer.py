import pytest
from summarizer import parse_sentence_count, get_text


def test_parse_sentence_count_valid():
    assert parse_sentence_count("3") == 3


def test_parse_sentence_count_invalid():
    with pytest.raises(ValueError):
        parse_sentence_count("abc")


def test_get_text_plain_text():
    assert get_text("hello") == "hello"


def test_get_text_from_file(tmp_path):
    f = tmp_path / "note.txt"
    f.write_text("file content", encoding="utf-8")
    assert get_text(str(f)) == "file content"