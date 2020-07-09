import sqlite3

# Create table
def createTable():
    conn = sqlite3.connect('musicdb.db')
    c = conn.cursor()

    c.execute('''Create TABLE music (address text)''')

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()

def check():
    conn = sqlite3.connect('musicdb.db')
    c = conn.cursor()
                
    #get the count of tables with the name
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='music' ''')

    #if the count is 1, then table exists
    if c.fetchone()[0] ==1 : 
        return (1)
    else :
        return(0)
                
    #commit the changes to db			
    conn.commit()
    #close the connection
    conn.close()

def  insert(address):
    conn = sqlite3.connect('musicdb.db')
    c = conn.cursor()   
    c.execute("INSERT INTO music(address) VALUES('{}') ".format(address))                              
    # Save (commit) the changes
    conn.commit()

    conn.close()   

def  select():
    conn = sqlite3.connect('musicdb.db')
    c = conn.cursor()                       
    c.execute("SELECT * FROM music")                              
    # Save (commit) the changes
    conn.commit()

    return( c.fetchall())

def delall():
    conn = sqlite3.connect('musicdb.db')

    c = conn.cursor()
    c.execute("DELETE FROM music")
    conn.commit()

    conn.close()

def drop():
    conn = sqlite3.connect('musicdb.db')

    c = conn.cursor()
    c.execute('''DROP TABLE music ''')
    # Save (commit) the changes
    conn.commit()

    conn.close()


if  __name__ == "__main__":
    delall()    
    drop()
    