import psycopg2
# connect to databse
connect=psycopg2.connect(
    dbname="myduka",
    user="postgres",
    host="localhost",
    port=5432,
    password="1234"
)
# cursor to perform databse operation
cur=connect.cursor()
# write a function to fetch products
# def get_products():
#     pquery='select * from products;'
#     cur.execute(pquery)
#     products= cur.fetchall()
#     return products

# get_products()   
# def get_sales():
#     query='select * from sales;'
#     cur.execute(query)
#     sales= cur.fetchall()
#     return sales

# get_sales()   
 

    # create function to fetch all data from db
def get_data(table):
    query=f"select * from {table}"
    cur.execute(query)
    data=cur.fetchall()
    return data
# get_data("products")  
# get_data("sales")  

# insert into db
# def insert_products():
#     query=" insert into products(id,name,buying_price ,selling_price ,stock_quantity)values(2,'chocolate',200,300,100);"
#     cur.execute(query)
#     connect.commit()
# # insert_products()
# # view the update
# get_data("products")
# # insert into sales db
# def insert_sales():
#     query="insert into sales(id,productid,quantity,created_at) values(20,2,200,now())"
#     cur.execute(query)
#     connect.commit()

# get_data("sales")

# def insert_products(a,b,c,d):
#     query="insert into products(id,name,buying_price ,selling_price ,stock_quantity)  values ({a}},{b},{c},{d})"
#     cur.execute(query)
#     connect.commit()
#     insert_products(3,'soda',300,500,110)
#     get_data("products")


# method 2
def insert_products(values):
    query="insert into products(name,buying_price,selling_price,stock_quantity)values(%s,%s,%s,%s)"
    cur.execute(query,values)
    connect.commit()

    # x=(4,"biscuits",100,200,500)
# x=(3,"biscuits",100,200,500)
# insert_products(x)
# get_data("products")
#     # insert_sales
def insert_sales(values):
    insert="insert into sales(productid,quantity,created_at) values(%s,%s,now());"
    cur.execute(insert,values)
    connect.commit()
# z=(21,1,400)
# insert_sales(z)
# get_data("sales")
# writ a query to get sales per product(selling_price*quantity)
def sales_product():
    query= "SELECT products.name, SUM (products.selling_price * sales.quantity)FROM  products JOIN sales on products.productid=sales.productid group by products.name;"
    cur.execute(query)
    data=cur.fetchall()
    return data


def profit():
     query="SELECT products.name,SUM((products.selling_price-products.buying_price)*SALES.quantity)AS profit FROM sales JOIN products  ON sales.productid=products.productid GROUP BY products.name"
     cur.execute(query)
     data=cur.fetchall()
     return data


def recent_sales():
     query="select * from sales ORDER BY sales.created_at DESC LIMIT 10;"
     cur.execute(query)
     data=cur.fetchall()
     return data


def sales_daily():
    query="SELECT DATE(sales.created_at)AS sales_day,SUM(products.selling_price * SALES.quantity)AS sales FROM sales JOIN products ON sales.productid=products.productid GROUP BY sales_day ORDER BY sales_day"
    cur.execute(query)
    data=cur.fetchall()
    return data


def profit_daily():
     query="SELECT DATE(sales.created_at)AS profit_day,SUM((products.selling_price-products.buying_price)*SALES.quantity)AS profit from sales JOIN products on sales.productid=products.productid GROUP BY profit_day order by profit_day;"
     cur.execute(query)
     data=cur.fetchall()
     return data

def insert_user(values):
     query="insert into users(full_name,email,password)values(%s,%s,%s)"
     cur.execute(query,values)
     connect.commit()


def check_email(email):
     query="select*from users where email=%s"
     cur.execute(query,(email,))
     data=cur.fetchall()
     return data


def check_email_password(email,password):
     query="select* from users where email=%s and password=%s"
     cur.execute(query,(email,password,))
     data=cur.fetchall()
     return data
     



