import pytest
import tasks
from tasks import Task




def test_tmpdir(tmpdir):
    # join() extends the path to include a filename
    a_file = tmpdir.join('something.txt')
    # create directory
    a_sub_dir = tmpdir.mkdir('anything')

    # file is created when written
    a_file.write('contents may settle during shipping')

    assert a_file.read() == 'contents may settle during shipping'
    