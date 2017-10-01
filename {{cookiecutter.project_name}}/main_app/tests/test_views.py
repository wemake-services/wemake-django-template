# -*- coding: utf-8 -*-


def test_main_page(client):
    """
    This test ensures that main page works.
    """
    response = client.get('/')

    assert response.status_code == 200
    assert '<h1>wemake-django-template</h1>' in str(response.content)
