import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(database="ttws2021", user="ttws2021", password="acid", host="bergbussard")
cur = conn.cursor()

# Execute the SQL query
query = """
SELECT
XMLFOREST(title AS "Title", author AS "Author", date AS "Date") AS xml_data
FROM
gutefrage
WHERE
title ~* '^(Was|Wer|Wie|Wo|Wann|Warum|Welche|Wem|Wessen)\s'
LIMIT 10
"""
cur.execute(query)

# Fetch the result
# Fetch all rows
rows = cur.fetchall()

# Construct the XML document
xml_data = '<data>\n'
for row in rows:
    xml_data += '    ' + row[0] + '\n'
    xml_data += '</data>'

# Write the XML data to a file
with open('output.xml', 'w') as file:
    file.write(xml_data)

# Close the database connection
cur.close()
conn.close()
