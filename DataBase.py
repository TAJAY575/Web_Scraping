import psycopg2
import configparser

# setup config
config = configparser.ConfigParser()
config.read('config.ini')

DBNAME = config['database']['DbName']
USER = config['database']['User']
HOST = config['database']['Host']
PW = config['database']['PW']

# insertion sql queries
GIZTOPSITEQUERY = '''
insert into tajay.giztop_products 
values (%s, %s, %s);
'''

def connectDb():
    try:
        conn_str = "dbname={} user={} host={} password={}".format(DBNAME, USER, HOST, PW)
        conn = psycopg2.connect(conn_str)
        print("Successfully connected to db!")
        return conn

    except Exception as e:
        print("Failed to connect to db!", e)

def giztopSiteToDb(conn, product_data_list):
    try:
        for product in product_data_list:
            with conn.cursor() as cur:
                cur.execute(GIZTOPSITEQUERY, (product.title, product.price, product.description))
                conn.commit()

        print("Successfully inserted {} products!".format(len(product_data_list)))

    except Exception as e:
        print("Failed to insert all products! -->", e)

if __name__ == "__main__":  
    
    # run
    conn = connectDb()
    cur = conn.cursor()