'''Create a conftest.py

Define the fixture functions in this file to make them accessible across multiple test files.
'''
import os
from pathlib import Path
from tempfile import mkdtemp

import pytest
from beetools import rm_tree


class WorkingDir:
    def __init__(self):
        self.dir = Path(mkdtemp(prefix='sqldbwrpr_'))


class EnvVar:
    mysql_userid = os.environ.get('MYSQL_USERID')
    mysql_password = os.environ.get('MYSQL_PASSWORD')
    mysql_admin_userid = os.environ.get('MYSQL_ADMIN_USERID')
    mysql_admin_password = os.environ.get('MYSQL_ADMIN_PASSWORD')
    mysql_dbname = 'sqldbwrpr'
    mysql_host = os.environ.get('MYSQL_HOST')
    mysql_port = os.environ.get('MYSQL_PORT')


class EnvSetUp:
    def __init__(self, p_make_project_ini=False):
        self.dir = WorkingDir().dir
        self.var = EnvVar()
        self.db_user_rights = [
            self.var.mysql_userid,
            self.var.mysql_host,
            '*',
            '*',
            'ALL',
        ]
        pass

    def dump_csv_file(self, tablename, txt):
        filename = self.dir / (tablename + '.csv')
        filename.write_text(txt)
        return filename


@pytest.fixture
def env_setup_self_destruct():
    '''Set up the environment base structure'''
    setup_env = EnvSetUp()
    yield setup_env
    rm_tree(setup_env.dir, p_crash=False)


@pytest.fixture
def working_dir_self_destruct():
    '''Set up the environment base structure'''
    working_dir = WorkingDir()
    yield working_dir
    rm_tree(working_dir.dir, p_crash=False)
