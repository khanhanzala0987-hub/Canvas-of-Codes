import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="company_db"
)

cursor = mydatabase.cursor()

hi = "create table employees (empid int auto_increment, empname varchar(50), department varchar(30), salary decimal(10,2), hire_date DATE, email varchar(100), primary key (empid),key (department))"

# hi = "create table department (deptid int auto_increment, department varchar(30), PRIMARY KEY (deptid), FOREIGN KEY (department) REFERENCES employees(department))"

# hi = "INSERT INTO employees (empname,department,salary,hire_date,email) VALUES ('Tom','Accounts',30000.10,CURRENT_DATE(),'tommyboss99atgmailcom')"

# hi = "INSERT INTO department (department) VALUES ('IT')"

# hi = "UPDATE employees SET salary = 70000.00 WHERE empname = 'John Doe'"

hi = "UPDATE employees SET department = 'HR' WHERE empname = 'Sarah Lee'"

cursor.execute(hi)

mydatabase.commit()