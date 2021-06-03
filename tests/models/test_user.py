from minsonet.models import User
from pytest import raises


def test_user_constructor():
    pk = 1
    name = "Bob"
    email = "bob@email.com"
    user = User({"pk": pk, "name": name, "email": email})
    assert user.pk == pk
    assert user.name == name
    assert user.email == email


def test_user_name_required():
    with raises(AttributeError) as e_info:
        User({"pk": 1, "email": "bob@email.com"})
        print(f"e_info: {e_info}")


def test_user_assignments():
    pk1 = 1
    name1 = "Bob"
    email1 = "bob@email.com"
    user = User({"pk": pk1, "name": name1, "email": email1})
    assert user.pk == pk1
    assert user.name == name1
    assert user.email == email1

    pk2 = 2
    name2 = "Bob2"
    email2 = "bob2@email.com"
    user.pk = pk2
    user.name = name2
    user.email = email2
    assert user.pk == pk2
    assert user.name == name2
    assert user.email == email2


def test_user_clone():
    pk = 1
    name = "Bob"
    email = "bob@email.com"
    user1 = User({"pk": pk, "name": name, "email": email})

    user2 = User(user1.__dict__)
    pk = 2
    user2.pk = pk

    assert user2.pk == 2
    assert user2.name == name
    assert user2.email == email
