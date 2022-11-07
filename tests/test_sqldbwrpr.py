'''Testing sqldbwrpr__init__()'''

# from pathlib import Path
# from beetools.beearchiver import Archiver
import fixtures
from sqldbwrpr.sqldbwrpr import MySQL


class TestSqlDbWrpr:
    def test_mysql__init__(self, env_setup_self_destruct):
        env_setup = env_setup_self_destruct
        my_sql_db = MySQL(
            p_user_name=env_setup.var.mysql_admin_userid,
            p_password=env_setup.var.mysql_admin_password,
            p_user_rights=env_setup.db_user_rights,
            p_recreate_db=True,
            p_db_name=env_setup.var.mysql_dbname,
            p_db_structure=fixtures.DB_STRUCTURE,
            p_batch_size=1,
            p_admin_username=env_setup.var.mysql_admin_userid,
            p_admin_user_password=env_setup.var.mysql_admin_password,
            p_db_port=env_setup.var.mysql_port,
        )
        my_sql_db.close()
        assert my_sql_db.success
        assert my_sql_db.bar_len == 50
        assert my_sql_db.batch_size == 1
        assert isinstance(my_sql_db.char_fields, dict)
        assert my_sql_db.conn
        assert my_sql_db.cur
        assert my_sql_db.db_name == 'sqldbwrpr'
        assert my_sql_db.db_structure == fixtures.DB_STRUCTURE
        assert my_sql_db.delimiter == ','
        assert my_sql_db.fkey_ref_act == {
            'C': 'CASCADE',
            'R': 'RESTRICT',
            'D': 'SET DEFAULT',
            'N': 'SET NULL',
        }
        assert my_sql_db.host_name
        assert my_sql_db.idx_type == {'U': 'UNIQUE', 'F': 'FULLTEXT', 'S': 'SPATIAL'}
        assert my_sql_db.msg_width == 50
        assert my_sql_db.non_char_fields == {
            'Rating': ['Date', 'Rating', 'OrgMemberId'],
            'Member': [
                'Race',
                'RegDateTime',
                'Picture',
                'ActiveStatus',
                'BirthYear',
                'DOB',
            ],
            'Country': [],
            'Organization': ['OrgId', 'RegFee', 'OpenTrading'],
            'MemberOrg': ['OrgId'],
        }
        assert my_sql_db._password == 'NotSecurePassword'
        assert my_sql_db.re_create_db
        assert not my_sql_db.silent
        assert my_sql_db.sort_order == {'A': 'ASC', 'D': 'DESC'}
        assert my_sql_db.table_load_order == [
            'Rating',
            'Country',
            'Member',
            'Organization',
            'MemberOrg',
        ]
        assert my_sql_db.user_name == 'root'
        assert my_sql_db.get_db_field_types() is None
        assert my_sql_db.db_port == '3308'
        pass

    def test_mysql_timport_csv(self, env_setup_self_destruct):
        env_setup = env_setup_self_destruct
        my_sql_db = MySQL(
            p_host_name=env_setup.var.mysql_host,
            p_user_name=env_setup.var.mysql_admin_userid,
            p_password=env_setup.var.mysql_admin_password,
            p_recreate_db=True,
            p_db_name=env_setup.var.mysql_dbname,
            p_db_structure=fixtures.DB_STRUCTURE,
            p_batch_size=1,
            p_db_port=env_setup.var.mysql_port,
        )
        tablename = 'Country'
        filename = env_setup.dump_csv_file(tablename, fixtures.TBL_TXT_COUNTRY)
        my_sql_db.import_csv(tablename, str(filename))
        my_sql_db.cur.execute(
            'SELECT {} FROM {}'.format(
                ','.join(my_sql_db.db_structure[tablename]),
                tablename,
            )
        )
        assert my_sql_db.cur.fetchall() == fixtures.TBL_TUP_COUNTRY
        pass

    # end timport_csv
