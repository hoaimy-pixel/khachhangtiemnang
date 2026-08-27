import pymysql


def get_connection():

    conn = pymysql.connect(

        host="mysql-3dc52a73-phungmy011105-0b24.c.aivencloud.com",

        port=26399,

        user="avnadmin",

        password="AVNS_r7GsJrhERBM4o2uylsR",

        database="company",

        ssl={
            "ca": "ca.pem"
        }

    )

    return conn
