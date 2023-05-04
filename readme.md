## HENI Assignment

### Requirements
Python 3.8 Required

### 1 - Parsing Task: 
- There are 2 files for this task
    - `TASKS/parsing_task1_with_lxml.py`
    - `TASKS/parsing_task1_with_scrapy.py`
- Lxml version is fully tested and bug free.
- Scrapy version is just for demonstration purposes.
- Run through following commands
    ```python
    python TASKS/parsing_task1_with_lxml.py
    python TASKS/parsing_task1_with_scrapy.py
    ```

### 2 - Regex Task: 
- Attempted to form single regex for all the use-cases.
- Handled exceptions in case there is no match. 
- Run through following command
    ```python
    python TASKS/regex_task2.py
    ```

### 3 - Scrapy Task: 
- Complete structured project of scrapy framework with monitors and item files included under
    - `HENI/`
- Tried to handle all the use-cases that exist on the website.
- Sample output file is also included as **bearspace_results.csv**
- **Monitors:** Specially included monitors which will help us to track down the flaws in the spider output.
    - I have added a monitor that will be tracking the number of output items and if that is less
     then specific threshold we will be notified.
    - Monitors are similar to unit tests
- Run through following command
    ```python
    scrapy runspider bearspace.py
    ```

### 4 - Sql Task: 
- Used **pandassql** for this task specifically so we can test results locally without the need to install sql
- Run through following command
    ```python
    python TASKS/data_task4.py
    ```


## Definitions (Task4):
**Question: Describe inner join, left join, right join, full join.**

## Inner join: 
- Inner join returns only the matching rows between both the tables, non-matching rows are eliminated.
## Left join: 
- It joins two or more tables, returns all records from the left table, and matching rows from the right-hand table.
## Right join: 
- It is used to join two or more tables, returns all records from the right table, and matching rows from the left-hand table.
## Full join: 
- Full Join or Full Outer Join returns all rows from both the tables (left & right tables), including non-matching rows from both the tables.
