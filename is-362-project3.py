import sqlite3
import pandas as pd

# Replace 'path/to/your/chinook.db' with the actual path where you saved the Chinook database
connection = sqlite3.connect('https://chinookdatabase.codeplex.com/')

# SQL query to join customer, invoice, invoice item, track, and album tables
query = """
SELECT c.LastName, c.FirstName, t.Name AS TrackName, al.Title AS AlbumTitle
FROM Customer c
JOIN Invoice i ON c.CustomerId = i.CustomerId
JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId
JOIN Track t ON il.TrackId = t.TrackId
JOIN Album al ON t.AlbumId = al.AlbumId
ORDER BY c.LastName, c.FirstName;
"""

# Read the SQL query into a DataFrame
df = pd.read_sql_query(query, connection)

# Display the DataFrame
print(df.head())

# Close the connection to the database
connection.close()
