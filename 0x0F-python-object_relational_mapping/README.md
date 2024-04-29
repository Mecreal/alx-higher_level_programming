
# Project: Python Object Relational Mapping

This project involves using Python modules such as `MySQLdb` and `SQLAlchemy` to interact with MySQL databases. The focus is on creating, querying, and updating databases using Python scripting.

## Table of Contents
1. [Install Dependencies](#install-dependencies)
2. [Setup Database](#setup-database)
3. [Scripts Description](#scripts-description)

## Install Dependencies
- **Python Virtual Environment**
  ```shell
  $ sudo apt-get install python3.8-venv
  $ python3 -m venv venv
  $ source venv/bin/activate
  ```
- **MySQLdb Module (version 2.0.x)**
  - Ensure MySQL 8.0 is installed.
  - Install the required packages:
    ```shell
    sudo apt-get install python3-dev
    sudo apt-get install libmysqlclient-dev
    sudo apt-get install zlib1g-dev
    sudo pip3 install mysqlclient
    ```
  - Test the installation:
    ```python
    $ python3
    >>> import MySQLdb
    >>> MySQLdb.version_info
    ```
- **SQLAlchemy Module (version 1.4.x)**
  ```shell
  $ sudo pip3 install SQLAlchemy
  ```

## Setup Database
- Create and set up the MySQL database `hbtn_0e_0_usa` and `hbtn_0e_4_usa` using the provided SQL scripts.

## Scripts Description
1. **0-select_states.py**
   - Lists all states from the `hbtn_0e_0_usa` database.
   - Arguments: `mysql username`, `mysql password`, `database name`.
   - Example Usage:
     ```shell
     $ ./0-select_states.py root root hbtn_0e_0_usa
     ```

2. **1-filter_states.py**
   - Lists all states with names starting with 'N' from `hbtn_0e_0_usa`.
   - Usage similar to the above script.

3. **2-my_filter_states.py**
   - Displays all values in `states` table where name matches the argument.
   - Takes an additional argument for the state name.
   - Example:
     ```shell
     $ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
     ```

4. **3-my_safe_filter_states.py**
   - Similar to the previous script but safe from SQL injections.

5. **4-cities_by_state.py**
   - Lists all cities from `hbtn_0e_4_usa` database.
   - Arguments: `mysql username`, `mysql password`, `database name`.

6. **5-filter_cities.py**
   - Lists all cities of a given state using the `hbtn_0e_4_usa` database.
   - Arguments: `mysql username`, `mysql password`, `database name`, `state name`.

7. **model_state.py**
   - Contains the class definition of a `State` and an instance `Base = declarative_base()` for SQLAlchemy.

8. **6-model_state.py**
   - Creates the `states` table in `hbtn_0e_6_usa` database using SQLAlchemy.

9. **7-model_state_fetch_all.py**
   - Lists all State objects from `hbtn_0e_6_usa` using SQLAlchemy.

10. **8-model_state_fetch_first.py**
    - Prints the first State object from `hbtn_0e_6_usa`.

11. **9-model_state_filter_a.py**
    - Lists all State objects containing 'a' from `hbtn_0e_6_usa`.

12. **10-model_state_my_get.py**
    - Prints the State object with the given name from `hbtn_0e_6_usa`.

13. **11-model_state_insert.py**
    - Adds the State "Louisiana" to `hbtn_0e_6_usa` and prints its new id.

14. **12-model_state_update_id_2.py**
    - Changes the name of a State object where `id = 2` to "New Mexico" in `hbtn_0e_6_usa`.

15. **13-model_state_delete_a.py**
    - Deletes all State objects with a name containing 'a' from `hbtn_0e_6_usa`.

16. **model_city.py, 14-model_city_fetch_by_state.py**
    - `model_city.py` contains the class definition of a City.
    - `14-model_city_fetch_by_state.py` prints all City objects from `hbtn_0e_14_usa`.



