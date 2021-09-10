from python.code_challenges.hashtable.hashtable import HashTable


def test_can_instantiate_hashtable():

    new_hashtable = HashTable()
    assert new_hashtable
    assert new_hashtable.size == 1024
    assert len(new_hashtable.bucket) == 1024


def test_hash_function_returns_valid_index():

    hashtable = HashTable()
    actual_index = hashtable.hash("app")
    expected = 791
    assert actual_index == expected


def test_hash_function_will_return_a_value_within_range():

    hashtable = HashTable()
    actual = hashtable.hash("test")
    assert actual <= 1024
    assert actual >= 0


def test_hash_function_will_return_similar_value_for_similar_word():

    hashtable = HashTable()
    key_a = "hijk"
    key_b = "kjih"
    assert hashtable.hash(key_a) == hashtable.hash(key_b)


def test_hash_function_will_produce_different_values_for_different_words():

    hashtable = HashTable()
    key_a = "abcd"
    key_b = "efgh"
    assert hashtable.hash(key_a) != hashtable.hash(key_b)


def test_add_works_correctly():

    hashtable = HashTable()
    index = hashtable.hash("spam")
    assert hashtable.bucket[index] is None
    hashtable.add("spam", "eggs")
    bucket = hashtable.bucket[index]
    assert bucket


def test_add_method_will_add_to_linked_list_and_handle_collisions():

    hashtable = HashTable()
    hashtable.add("lmno", 10)
    hashtable.add("onml", 20)
    index = hashtable.hash("lmno")
    count = 0
    current = hashtable.bucket[index].head

    while current:
        count += 1
        current = current.next
    assert count == 2


def test_get_method_returns_value_if_key_present():

    hashtable = HashTable()
    hashtable.add("uvwx", 10)
    assert hashtable.get("uvwx") == 10


def test_get_method_returns_None_for_value_not_present():

    hashtable = HashTable()
    hashtable.add("abcd", 10)
    assert hashtable.get("xyz") is None


def test_get_method_will_account_for_linked_list_with_multiple_values():

    hashtable = HashTable()
    hashtable.add("abcd", 10)
    hashtable.add("dcba", 20)
    hashtable.add("cbad", 30)
    assert hashtable.get("dcba") == 20


def test_contains_returns_true_if_key_is_present():

    hashtable = HashTable()
    hashtable.add("abcd", 10)
    hashtable.add("bcda", 20)
    hashtable.add("abdc", 30)
    assert hashtable.contains("abcd")


def test_contains_returns_false_if_key_is_not_present():

    hashtable = HashTable()
    hashtable.add("lmno", 10)
    hashtable.add("mnoa", 20)
    hashtable.add("lmon", 30)
    assert hashtable.contains("xyz") == False
