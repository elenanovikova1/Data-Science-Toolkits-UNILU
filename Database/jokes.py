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


# Create the new database jokes with the columns id and joke

cursor.execute("""
    CREATE TABLE ms3_jokes (
        id SERIAL PRIMARY KEY,
        joke TEXT
    );
""")

conn.commit()


# Insert some jokes into the table

cursor.execute("""
INSERT INTO ms3_jokes (joke)
VALUES
    ('Why do programmers prefer dark mode? Because light attracts bugs!'),
    ('Why did the programmer quit his job? He didn''t get arrays!'),
    ('How many programmers does it take to change a light bulb? None, that''s a hardware problem!'),
    ('Why don''t programmers like nature? It has too many bugs!'),
    ('Why did the coder go broke? Too many bits and not enough bytes!'),
    ('What''s a programmer''s favorite hangout spot? The Foo Bar!'),
    ('Why do Java developers wear glasses? Because they don''t see sharp!'),
    ('How does a programmer shower? They open the water, lather, rinse, and repeat (in a loop).'),
    ('Why did the function go to therapy? It had too many issues!'),
    ('Why do programmers prefer dark chocolate? Because it''s bitter, like their code reviews!');
""")

conn.commit()

cursor.close()
conn.close()
