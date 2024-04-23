def test_principal_teachers_bad_principal(client, h_teacher_1):
    response = client.get(
        '/principal/teachers',
        headers=h_teacher_1
    )

    assert response.status_code == 403
    data = response.json

    assert data['error'] == 'FyleError'
    assert data['message'] == 'requester should be a principal'


def test_teacher_assignments_bad_teacher(client, h_principal):
    response = client.get(
        '/teacher/assignments',
        headers=h_principal
    )

    assert response.status_code == 403
    data = response.json

    assert data['error'] == 'FyleError'
    assert data['message'] == 'requester should be a teacher'


def test_health(client):
    response = client.get('/')

    assert response.status_code == 200
    data = response.json

    assert data['status'] == 'ready'
    assert data['time']


def test_not_found(client):
    response = client.get('/not_found')

    assert response.status_code == 404
    data = response.json

    assert data['error'] == 'NotFound'
    assert (
        data["message"]
        == "404 Not Found: The requested URL was not found on the server. "
        "If you entered the URL manually please check your spelling and try again."
    )
