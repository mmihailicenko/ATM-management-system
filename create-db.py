# import sqlite3
#
# con = sqlite3.connect('application.db')
#
# cur = con.cursor()
#
# # Create table
# # cur.execute('''CREATE TABLE blogs
# #                (id text not null primary key, date text, title text, content text, public integer)''')
# cur.execute('''create table atms(
# 	                id text not null constraint atms_pk primary key,
# 	                name text,
# 	                location text,
# 	                blocked int default 0);''')
#
# # Inserting rows of data
# cur.execute("INSERT INTO atms VALUES ('RT87i7', 'n-bank', '1st Avenue', 0)")
# cur.execute("INSERT INTO atms VALUES ('RT87i8', 'y-bank', '5th Avenue', 1)")
#
# con.commit()
#
# con.close() todo: a working solution ought to be found
