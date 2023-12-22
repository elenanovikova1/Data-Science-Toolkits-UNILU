import psycopg2

# Connection parameters
host = 'localhost'
port = 5432
user = 'postgres'
password = 'mypassword'
default_db = 'mydatabase'


# Establish a connection to Server
conn = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=default_db,
)

cursor = conn.cursor()


# Chose a random joke from the list

cursor.execute("""
    SELECT id, joke
    FROM ms3_jokes
    ORDER BY RANDOM()
    LIMIT 1;
""")

random_joke = cursor.fetchone()

# Print the random joke

if random_joke:
    joke_id, joke = random_joke
    print(f"Joke #{joke_id}: {joke}")

# Close the cursor and connection to the database

cursor.close()
conn.close()
