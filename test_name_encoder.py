from name_encoder import NameEncoder


def test_encode_names():
    names = ["ab", "cd"]
    encoder = NameEncoder(code=2)
    res = encoder.encode_names(names)
    assert list(res.values()) == ["cd", "ef"]