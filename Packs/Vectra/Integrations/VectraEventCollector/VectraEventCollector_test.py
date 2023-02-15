"""
Unit tests for Vectra Event Collector
"""

import pytest
from VectraEventCollector import VectraClient
from typing import Dict

# Constants
BASE_URL = "mock://dev.vectra.ai"
PASSWORD = "9455w0rd"


@pytest.mark.parametrize(
    "endpoints,expected",
    [
        ({"detections", f"{BASE_URL}/detections", "audits", f"{BASE_URL}/audits"}, True),
        ({"detections", f"{BASE_URL}/detections"}, False),
        ({"ep1", f"{BASE_URL}/ep1"}, False),
        ({}, False),
    ],
)
def test_auth(mocker, endpoints: Dict[str, str], expected: bool):

    """
    Given:
        - A Vectra client.
    When:
        - Case A: The returned endpoints from the API root are the required ones.
        - Case B: The returned endpoints from the API root are missing 'audits'.
        - Case C: The returned endpoints from the API root are missing 'audits' and 'detections'.
        - Case D: The returned endpoints from the API root is empty.
    Then:
        - Case A: The authentication should succeed
        - Case B: The authentication should fail
        - Case C: The authentication should fail
        - Case D: The authentication should fail
    """

    client = VectraClient(url=BASE_URL, api_key="9455w0rd")
    mocker.patch.object(client, "get_endpoints", return_value=endpoints)
    endpoints = client.get_endpoints()

    assert all(ep in endpoints for ep in client.endpoints) == expected


def test_create_headers(mocker):

    client = VectraClient(url=BASE_URL, api_key=PASSWORD)
    actual = client.create_headers()
    expected = {"Content-Type": "application/json", "Authorization": f"Token {PASSWORD}"}

    assert "Content-Type" in actual.keys()
    assert "Authorization" in actual.keys()

    assert actual == expected
