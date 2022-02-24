from desafio_anagrama.main import check_anagram, quantity_in_anagram


# Dadas duas strings, a funcao check_anagram retorna um booleano.
def test_given_two_strings_Anagram_returns_boolean():
    # Colocado em duas strings que são anagramas
    assert check_anagram("muido", "miudo") is True
    # Colocado duas strings que NÃO são anagramas
    assert check_anagram("cansado", "muido") is False


# Dadas duas listas de strings, a funcao quantity_in_anagram
# retorna a quantidade correta que e 6 em int.
def test_anagram_quantity(
    list_words_a_success, list_words_b_success, list_words_b_error
):
    # Colocado duas listas e esperando o retorno 6
    assert (
        quantity_in_anagram(
            param_list_words_a=list_words_a_success,
            param_list_words_b=list_words_b_success,
        )
        == 6
    )

    # Colocado duas listas e esperando o retorno diferente de 6
    assert (
        quantity_in_anagram(
            param_list_words_a=list_words_a_success,
            param_list_words_b=list_words_b_error,
        )
        != 6
    )
