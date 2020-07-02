# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture()
def app (request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password ="secret")
    app.create_group(Group(name="first group", header="hjklouhi", footer="lhb"))
    app.logout()