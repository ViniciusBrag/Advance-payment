from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.fixture
def resp_payment(client, db):
    return client.get(reverse('payments:payments'))

def test_resp_payment_status_code(resp_payment):
    assert resp_payment.status_code == HTTPStatus.FOUND