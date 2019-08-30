import pytest
import warnings
import tasks
from tasks import Task
import unittest


def lame_function():
    warnings.warn("Please stop using this", DeprecationWarning)




def test_lame_function(recwarn):
    lame_function()
    assert len(recwarn) == 1
    w = recwarn.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == 'Please stop using this'


def test_lame_function_2():
    with pytest.warns(None) as warning_list:
        lame_function()

    assert len(warning_list) == 1
    w = warning_list.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == 'Please stop using this'


@pytest.fixture()
def tasks_db_non_empty(tasks_db_session, request):
    tasks.delete_all()
    ids = []
    ids.append(tasks.add(Task('One', 'Brian', True)))
    request.cls.ids = ids


@pytest.mark.usefixtures('tasks_db_non_empty')
class TestNonEmpty():

    def test_delete_decreases_count(self):
        assert tasks.count() == 1
        tasks.delete(self.ids[0])
        assert tasks.count() == 0













