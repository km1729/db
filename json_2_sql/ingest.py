import psycopg2
import json
import yaml


# Read JSON data from the file
with open('/home/k/projects/db/json_2_sql/employee.json') as file:
    data = json.load(file)

# Read yaml data, Connect to your PostgreSQL database
with open('/home/k/projects/db/config.yaml','r') as config_file:
    config = yaml.safe_load(config_file)

conn = psycopg2.connect(
    dbname=config['postgres']['database'],
    user=config['postgres']['user'],
    password=config['postgres']['password'],
    host=config['postgres']['host']
)

cur = conn.cursor()

# Check if the table 'employee2' exists, and if not, create it
cur.execute(
    "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'employee2');"
)
exists = cur.fetchone()[0]

if not exists:
    # Create the 'employee2' table if it doesn't exist
    cur.execute(
        "CREATE TABLE employee3 (id INTEGER, name VARCHAR(100), department VARCHAR(100), position VARCHAR(100), salary INTEGER);"
    )
    conn.commit()

# Insert data into the 'employee2' table
for item in data:
    try:
        cur.execute(
            "INSERT INTO employee2 (id, name, department, position, salary) VALUES (%s, %s, %s, %s, %s)",
            (item['id'], item['name'], item['department'], item['position'], item['salary'])
        )
    except psycopg2.Error as error:
        conn.rollback()
        print("Failed to insert record into the table", error)

conn.commit()

# Close communication with the database
cur.close()
conn.close()

