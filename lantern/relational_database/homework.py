from typing import List

import psycopg2


# conn = psycopg2.connect(dbname='cursor_db', user='cursor',
# password='very_secret_password', host='localhost')
# cursor = conn.cursor()


def task_1_add_new_record_to_db(con) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contact_name': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """
    with con.cursor() as cursor:
        #     dic = {
        #     'customer_name': 'Thomas',
        #     'contact_name': 'David',
        #     'address': 'Some Address',
        #     'city': 'London',
        #     'postalcode': '774',
        #     'country': 'Singapore',
        # }
        cursor.execute("""INSERT INTO Customers( CustomerName,
           ContactName, Address,City,PostalCode,Country)
           values ('Thomas', 'David', 'Some Address', 'London', '774', 'Singapore');
       """)


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    cur.execute("SELECT * FROM Customers;")
    list1 = cur.fetchall()
    return list1


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute("SELECT * FROM Customers WHERE Country = 'Germany';")
    list2 = cur.fetchall()
    print(list2)
    return list2


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """
    cur = con.cursor()
    # with con.cursor() as cursor:
    cur.execute("""UPDATE Customers SET CustomerName='Johnny Depp'
         WHERE CustomerID = 1;""")


def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    with con.cursor() as cursor:
        cursor.execute("""DELETE FROM Customers WHERE CustomerName='Wolski';""")


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    cur.execute("SELECT Country FROM Suppliers;")
    list2 = cur.fetchall()
    print(list2)
    return list2


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    cur.execute("""
    SELECT Country FROM Suppliers
    ORDER BY Country DESC""")
    list2 = cur.fetchall()
    print(list2)
    return list2


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    cur.execute("""
           SELECT COUNT(CustomerName), City 
            FROM Customers
            GROUP BY City
            ORDER BY City ASC;
        """)
    list2 = cur.fetchall()
    print(list2)
    return list2


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    cur.execute("""
               SELECT COUNT(Country), Country
                FROM Customers
                GROUP BY Country
                HAVING COUNT(Country) > 10
                ORDER BY COUNT(Country) DESC, Country ASC ;
            """)
    list2 = cur.fetchall()
    print(list2)
    return list2


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    cur.execute("""
                SELECT * FROM Customers 
                ORDER BY CustomerName
                LIMIT 10
            """)
    list2 = cur.fetchall()
    print(list2)
    return list2


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    cur.execute("""
                        SELECT * FROM Customers
                        OFFSET 11;
                    """)
    list2 = cur.fetchall()
    print(list2)
    return list2


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    cur.execute("""SELECT * FROM Suppliers 
    WHERE (Country = 'USA' AND Country = 'UK' AND Country ='Japan');""")
    list2 = cur.fetchall()
    print(list2)
    return list2


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """

    cur.execute("""
    SELECT ProductName FROM Products
    LEFT JOIN Suppliers
    on products.supplierid= suppliers.supplierid
    WHERE Country = 'Sweden';""")
    list2 = cur.fetchall()
    print(list2)
    return list2


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    cur.execute("""
      SELECT ProductID,ProductName,Unit,Price,Suppliers.Country, Suppliers.City,
    Suppliers.SupplierName
    FROM Products
    LEFT OUTER JOIN Suppliers ON Products.SupplierID= Suppliers. SupplierID;""")
    list2 = cur.fetchall()
    print(list2)
    return list2


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    cur.execute("""
          SELECT CustomerName,ContactName,Country,Orders.OrderId
        FROM Customers
        LEFT OUTER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;""")
    list2 = cur.fetchall()
    print(list2)
    return list2


def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    cur.execute("""
           SELECT Customers.CustomerName,Customers.Address,Customers.Country AS CustomerCountry,Suppliers.Country 
           AS SupplierCountry,Suppliers.SupplierName   
           FROM Customers
           FULL OUTER JOIN Suppliers             
           ON Customers.Country = Suppliers.Country
           Order by CustomerCountry,SupplierCountry;""")
    list2 = cur.fetchall()
    print(list2)
    return list2
