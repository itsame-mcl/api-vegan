from server.api import get_ean, is_vegan


def test_get_ean_Nutella():
    actual = get_ean("Nutella")
    assert actual == 3017620422003


def test_get_ean_Camembert_President():
    actual = get_ean("Camembert Président")
    assert actual == 3228021170039


def test_is_vegan_3468570116601():
    actual = is_vegan(3468570116601)
    assert actual == {3468570116601: "yes"}


def test_is_vegan_3256540001305():
    actual = is_vegan(3256540001305)
    assert actual == {3256540001305: "no"}
