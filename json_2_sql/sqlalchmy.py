from sqlalchemy import create_engine, text
import yaml

with open('../config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

user = config['postgres']['user']
password = config['postgres']['password']
hostname = config['postgres']['host']
database_name = config['postgres']['database']


connection_str = f'postgresql://{user}:{password}@{hostname}/{database_name}'


try:
    engine = create_engine(connection_str)
    connection = engine.connect()
    
    result = connection.execute(text('SELECT * FROM employee2'))
    for row in result:
        print(row)
    print(result)
    # print("connection successfull.")

except:
    print(f"Error")
