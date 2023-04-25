import pandas as pd
from sqlalchemy import create_engine
from creds import PASSWORD

def load_to_demo(df, table_name, schema="schema1"):
    db_url = "demo-db.cau5jmehluun.us-east-2.rds.amazonaws.com"
    username = 'admin'
    # allan_dict = {
    #     "AllanID": [2, 3, 4],
    #     "AllanType": ["shaved", "murderer", "farting"],
    #     "AllanDate": ["today", "tomorrow", "lastweek"]
    # }
    # df = pd.DataFrame(allan_dict)
    
    # Create a MySQL engine
    engine = create_engine(f'mysql://{username}:{PASSWORD}@{db_url}/{schema}')

    # Write the DataFrame to MySQL
    df.to_sql(table_name, engine, if_exists='append', index=False)

load_to_demo()

load_to_demo(df)
