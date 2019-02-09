import pytest
import tasks
from tasks import Task
import json


@pytest.fixture(scope='session', params=['tiny',])
def tasks_db_session(tmpdir_factory, request):
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), request.param)
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    # an empty tasks db
    tasks.delete_all()


@pytest.fixture(scope='module')
def author_file_json(tmpdir_factory):

    python_author_data = {
        'Ned': {'City': 'Boston'},
        'Brian': {'City': 'Portland'},
        'Luciano': {'City': 'Sau Paulo'}
    }
    file = tmpdir_factory.mktemp('data').join('author_file.json')
    print('file:{}'.format(str(file)))

    with file.open('w') as f:
        json.dump(python_author_data, f)
    return file


def pytest_addoption(parser):
    parser.addoption("--myopt", action="store_true",
                     help="some boolean option")
    parser.addoption("--foo", action="store", default="bar",
                     help="foo: bar or baz")
