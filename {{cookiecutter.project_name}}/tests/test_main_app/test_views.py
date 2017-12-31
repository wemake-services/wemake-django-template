# -*- coding: utf-8 -*-


def test_main_page(client, main_heading):
    """This test ensures that main page works."""
    response = client.get('/')

    assert response.status_code == 200
    assert main_heading in str(response.content)
