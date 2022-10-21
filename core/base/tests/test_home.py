from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.fixture
def response_home(client):
    """Fixture to views.home
    Args:
        client (fixture): Fixture that acces http a view or function
    Returns:
        Fixture: Return fixture can acces a views.
    """   
    return client.get(reverse("base:home"))
    



def test_status_code_response_home(response_home):
    """Test to assert status_code from Fixure 'response_home'
    Args:
        response_home (_type_): Fixture
    """
    assert response_home.status_code == HTTPStatus.OK