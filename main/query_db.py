import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(database="ttws2021", user="ttws2021", password="acid", host="bergbussard")
cur = conn.cursor()

# Execute the SQL query
query = """
SELECT
XMLFOREST(title AS "Title", text AS "Text", author AS "Author", date AS "Date", url AS "URL") AS xml_data
FROM
gutefrage
WHERE
to_tsvector('simple', title) @@ to_tsquery('simple', 'Was|Wer|Wie|Wo|Wann|Warum|Welche|Wem|Wessen')
AND NOT to_tsvector('simple', title) @@ to_tsquery('simple', 'Ich|mein|meinen|mir|mich|ihr')
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
with open('./data/output.full.xml', 'w') as file:
    file.write(xml_data)

# Close the database connection
cur.close()
conn.close()
