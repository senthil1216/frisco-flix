from app import app
import sqlite3
from flask import g

DATABASE = app.config['DATABASE']


def connect_db():
	con = sqlite3.connect(DATABASE)
	g.db = con

def close_db():
	if hasattr(g, 'db'):
		g.db.close()

def close_connection():
	db = getattr(g, '_database' , None)
	if db is not None:
		db.close()

def query_db(query, args=(), one=False):
	db = g.db
	cur = db.execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv
