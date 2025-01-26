
from app.db.sql_client import SQLDB
add_ai_option_sp = """
create or replace function add_ai_option(p_ai_option VARCHAR, p_label_name VARCHAR)
returns void as $$
begin
    insert into ai_options (ai_option, label_name) values (p_ai_option, p_label_name);
end;
$$ language plpgsql;
"""

retrieve_ai_option_sp = """
create or replace function retrieve_ai_option(p_ai_option_uid VARCHAR)
returns record as $$
begin
    return select * from ai_options where ai_option_uid = p_ai_option_uid;
end;
$$ language plpgsql;
"""
retrieve_all_ai_options_sp = """
create or replace function retrieve_all_ai_options()
returns record as $$
begin
    return select * from ai_options;
end;
$$ language plpgsql;
"""


class AIOptionModel(SQLDB):
    def __init__(self, ai_option_uid, ai_option, label_name):
        self.ai_option_uid = ai_option_uid
        self.ai_option = ai_option
        self.label_name = label_name

    # def add_ai_option(self, ai_option, label_name):
    #     conn
# class AiOption:
#     def __init__(self, ai_option_uid, ai_option, label_name):
#         self.ai_option_uid = ai_option_uid
#         self.ai_option = ai_option
#         self.label_name = label_name
