from flask import Flask,render_template,url_for,request,session,logging,redirect,flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from passlib.hash import sha256_crypt


db_connection_string = "mysql+pymysql://acsk3llfsqc6ng908fk3:pscale_pw_NYXbNN1rUSIJ5YukeSwqnWDdbxoHXbSO1Dy2G2adhdT@gcp.connect.psdb.cloud/account_book?charset=utf8mb4"
#mysql+pymysql://username:password@localhost/databasename

##db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


db=scoped_session(sessionmaker(bind=engine))