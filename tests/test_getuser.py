import pytest
import uuid
from utils.apis import APIS
created_repo_name=None


@pytest.fixture(scope='module')
def apis():
    return APIS()


def test_get_profile(apis):
    response=apis.get('user')
    print(response.json())
    assert response.status_code==200
    assert len(response.json())>0

def test_get_repos(apis):
    response=apis.get('user/repos')
    print(response.json())
    assert response.status_code==200
    assert len(response.json())>0


def test_create_repo(apis,load_user_data):
    global created_repo_name
    created_repo_name=f"test_repo-{uuid.uuid4().hex[:6]}"
    new_repo={
        "name":created_repo_name,
        "description": load_user_data["new_repo"]["description"],
        "private": load_user_data["new_repo"]["private"]


    }
    response=apis.post('user/repos',new_repo)
    print(response.json())
    assert response.status_code == 201


def test_update_repo(apis, load_user_data):
    username=load_user_data["username"]
    updated_repo_name = f"test_repo-{uuid.uuid4().hex[:6]}"
    updated_repo = {
        "description": load_user_data["updated_repo"]["description"],
    }
    response = apis.patch(f'repos/{username}/{created_repo_name}',updated_repo)
    print(response.json())
    assert response.status_code == 200



def test_delete_repo(apis,load_user_data):
    username=load_user_data["username"]

    response=apis.delete(f'repos/{username}/{created_repo_name}')
    assert response.status_code==204



