import pytest
from starlette.testclient import TestClient

from backend.app import app
from backend.database import database

client: TestClient = TestClient(app)


class TestClass(object):
    @pytest.fixture
    async def setup(self):
        # TODO: INIT DB
        # print("Collection not initialized")
        # await database.init()
        # print("Collection initialized")
        pass

    @pytest.mark.asyncio
    async def test_home(self) -> None:
        response = client.get('/')
        assert response.status_code == 200
        assert response.json() == {'message': 'Kalbim ILOMMMM'}

    @pytest.mark.asyncio
    async def test_get_index(self) -> None:
        response = client.get('/get-index')
        assert response.status_code == 200
        # Assert response is an html file
        assert response.headers['content-type'] == 'text/html; charset=utf-8'
        # Assert response html contains header Affirmations
        assert 'Affirmations' in response.text

    # @pytest.mark.asyncio
    # async def test_get_affirmation(self) -> None:
    #     response = client.get('/random-affirmation')
    #     assert response.status_code == 200
    #     assert response.json().get('affirmation') is not None
    #     affirm_text: str = response.json().get('affirmation')
    #     print(affirm_text)
    #     assert len(affirm_text) > 1

    # @pytest.mark.asyncio
    # async def test_post_dealt_issue(self) -> None:
    #     response = client.post('/get-affirmation', json={"text": "life"})
    #     assert response.status_code == 200
    #     assert response.json().get('affirmation') is not None
    #     affirm_text: str = response.json().get('affirmation')
    #     print(affirm_text)
    #     assert len(affirm_text) > 1
