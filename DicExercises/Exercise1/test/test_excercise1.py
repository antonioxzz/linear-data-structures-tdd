import pytest
from dic1.excercise1 import count_words_from_file


@pytest.mark.parametrize('txt_from_file, expected_word_pair_dic', [
    ("hola soy Italo", {
        "hola": 1,
        "soy": 1,
        "Italo": 1,
    })
])
def test__count_words_from_file__return_word_pair_dic__when_read_txt_file(txt_from_file, expected_word_pair_dic):
    word_pair_dic = count_words_from_file(txt_from_file)
    assert expected_word_pair_dic == word_pair_dic
    