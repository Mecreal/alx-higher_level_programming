# 📚 SQL Introduction Tasks

This README documents a series of SQL scripts used for various database operations. These scripts are part of the `alx-higher_level_programming` GitHub repository.

## 📌 Table of Contents
1. [📝 List Databases](#list-databases)
2. [🔧 Create a Database](#create-a-database)
3. [🗑️ Delete a Database](#delete-a-database)
4. [📋 List Tables](#list-tables)
5. [🛠️ First Table](#first-table)
6. [📊 Full Description](#full-description)
7. [🔍 List All in Table](#list-all-in-table)
8. [➕ First Add](#first-add)
9. [🔢 Count 89](#count-89)
10. [🌟 Full Creation](#full-creation)
11. [📈 List by Best](#list-by-best)
12. [🎯 Select the Best](#select-the-best)
13. [🚫 Cheating is Bad](#cheating-is-bad)
14. [📉 Score Too Low](#score-too-low)
15. [📝 Average](#average)
16. [🔎 Number by Score](#number-by-score)
17. [🗣️ Say My Name](#say-my-name)
18. [🌐 Go to UTF8](#go-to-utf8)
19. [🌡️ Temperatures #0](#temperatures-0)
20. [🏙️ Temperatures #1](#temperatures-1)
21. [🔥 Temperatures #2](#temperatures-2)

### 📝 List Databases
- **Script:** `0-list_databases.sql`
- **Description:** Lists all databases on the MySQL server.

### 🔧 Create a Database
- **Script:** `1-create_database_if_missing.sql`
- **Description:** Creates the database `hbtn_0c_0` if it does not already exist.

### 🗑️ Delete a Database
- **Script:** `2-remove_database.sql`
- **Description:** Deletes the database `hbtn_0c_0` if it exists.

### 📋 List Tables
- **Script:** `3-list_tables.sql`
- **Description:** Lists all tables of a specified database.

### 🛠️ First Table
- **Script:** `4-first_table.sql`
- **Description:** Creates a table named `first_table` with columns `id INT` and `name VARCHAR(256)`.

### 📊 Full Description
- **Script:** `5-full_table.sql`
- **Description:** Prints the full description of the `first_table`.

### 🔍 List All in Table
- **Script:** `6-list_values.sql`
- **Description:** Lists all rows in the `first_table`.

### ➕ First Add
- **Script:** `7-insert_value.sql`
- **Description:** Inserts a new row into `first_table` with `id = 89` and `name = Best School`.

### 🔢 Count 89
- **Script:** `8-count_89.sql`
- **Description:** Displays the number of records with `id = 89` in `first_table`.

### 🌟 Full Creation
- **Script:** `9-full_creation.sql`
- **Description:** Creates `second_table` and adds multiple rows with specific values.

### 📈 List by Best
- **Script:** `10-top_score.sql`
- **Description:** Lists all records in `second_table` ordered by score.

### 🎯 Select the Best
- **Script:** `11-best_score.sql`
- **Description:** Lists records in `second_table` with a score >= 10.

### 🚫 Cheating is Bad
- **Script:** `12-no_cheating.sql`
- **Description:** Updates the score of Bob to 10 in `second_table`.

### 📉 Score Too Low
- **Script:** `13-change_class.sql`
- **Description:** Removes all records with a score <= 5 in `second_table`.

### 📝 Average
- **Script:** `14-average.sql`
- **Description:** Computes the average score of all records in `second_table`.

### 🔎 Number by Score
- **Script:** `15-groups.sql`
- **Description:** Lists the number of records for each score in `second_table`.

### 🗣️ Say My Name
- **Script:** `16-no_link.sql`
- **Description:** Lists records in `second_table` with non-empty name values, ordered by descending score.

### 🌐 Go to UTF8
- **Script:** `100-move_to_utf8.sql`
- **Advanced**
- **Description:** Converts the `hbtn_0c_0` database, `first_table`, and the `name` field to UTF8.

### 🌡️ Temperatures #0
- **Script:** `101-avg_temperatures.sql`
- **Advanced**
- **Description:** Displays average temperature by city in descending order.

### 🏙️ Temperatures #1
- **Script:** `102-top_city.sql`
- **Advanced**
- **Description:** Shows top 3 cities' temperatures during July and August.

### 🔥 Temperatures #2
- **Script:** `103-max_state.sql`
- **Advanced**
- **Description:** Displays the max temperature of each state, ordered by state name.
