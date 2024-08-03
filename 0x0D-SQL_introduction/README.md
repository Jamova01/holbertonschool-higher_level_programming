# 0x0D. SQL - Introduction

This repository contains solutions to tasks and projects for the "0x0D. SQL - Introduction" module as part of the Holberton School curriculum. The focus is on understanding the basics of SQL and databases, with a practical approach using MySQL.

## Concepts

- Databases
- SQL (Structured Query Language)
- MySQL

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without assistance:

- What is a database?
- What is a relational database?
- What does SQL stand for?
- What is MySQL?
- How to create a database in MySQL.
- What do DDL and DML stand for?
- How to `CREATE` or `ALTER` a table.
- How to `SELECT` data from a table.
- How to `INSERT`, `UPDATE`, or `DELETE` data.
- What are subqueries?
- How to use MySQL functions.

## Project Structure
The project directory contains several SQL scripts, each corresponding to a specific task or exercise. Below is a summary of each file and its purpose:

* **0-list_databases.sql:** Lists all databases in the MySQL server.
* **1-create_database_if_missing.sql:** Creates a database named hbtn_0c_0 if it does not exist.
* **2-remove_database.sql:** Deletes the hbtn_0c_0 database if it exists.
* **3-list_tables.sql:** Lists all tables in a specified database.
* **4-first_table.sql:** Creates a table named first_table with columns id and name.
* **5-full_table.sql:** Displays the full description of first_table.
* **6-list_values.sql:** Lists all rows of first_table.
* **7-insert_value.sql:** Inserts a new row into first_table.
* **8-count_89.sql:** Counts the number of records with id = 89.
* **9-full_creation.sql:** Creates second_table and inserts multiple rows.
* **10-top_score.sql:** Lists records of second_table ordered by score.
* **11-best_score.sql:** Lists records with score >= 10 ordered by score.
* **12-no_cheating.sql:** Updates Bob's score to 10 in second_table.
* **13-change_class.sql:** Removes records with score <= 5.
* **14-average.sql:** Computes the average score of records in second_table.
* **15-groups.sql:** Lists the number of records with the same score.
* **16-no_link.sql:** Lists records of second_table with a name, ordered by score.
* **100-move_to_utf8.sql:** Converts the hbtn_0c_0 database and first_table to UTF8.