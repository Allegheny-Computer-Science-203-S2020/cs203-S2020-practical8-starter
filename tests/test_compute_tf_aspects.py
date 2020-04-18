"""Test cases for the aspect-oriented implementation."""

from termfrequency import compute_tf_aspects


def test_read_data_file_and_remove_stopwords_0():
    """Checks that the reading of the small text file and stop word removal works."""
    list_of_words = ["test", "example", "file", "test"]
    frequencies_of_words = compute_tf_aspects.frequencies(list_of_words)
    assert len(frequencies_of_words) == 3
