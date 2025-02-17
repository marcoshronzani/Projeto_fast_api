from http import HTTPStatus

from fastapi.testclient import TestClient

from projeto_fast_api.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange ( Preparação )

    response = client.get('/')  # Act ( Ação )

    assert response.status_code == HTTPStatus.OK  # Assert ( Verificação )

    assert response.json() == {'message': 'Olá Mundooooooo!'}
