#Before you can install pyodbc, install microsoft c++ tools. They can be found at https://docs.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170
#Before you can pip install pyodbc, do "pip install wheel"
#'pip install pyodbc' in the terminal
#'pip install sqlalchemy' in the terminal
#This file creates a connection to a Microsoft Access file, reads it and puts it in the MySQL database.

#imports the python packages required to run this script 
import sys
#sys.path.append(r"c:\users\Administrator\appdata\local\packages\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\localcache\local-packages\python39\site-packages")
sys.path.append(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python310")
#We need datetime and date in order to configure the MySQL database to read what is coming out of the MS Access database with the proper dates, but
#   Python does not have these functions built in.
from datetime import date, datetime, timezone
from dateutil import parser
import pytz

#PYODBC is an open source Python module which allows easy access to databases configured to be accessed with the Open Database Connectivity API. 
import pyodbc
import time
#The mysql.connector import statement is running under the assumption that the above import sys statement is configured correctly for
#   the location of PIP. This is used to install a MySQL driver. It is possible that this got lost during some restart or Windows Update and maybe needs to
#   be installed again. 
import mysql.connector

# Getting variables from config.ini which will allow us to log into the mysql database and view its data on the linux environment.
from configparser import ConfigParser
config = ConfigParser()

config.read(r'C:\Users\Administrator\Desktop\MySQL-config.ini')
mysqldb_host = config.get('main', 'mysqldb_host')
username = config.get('main', 'username')
password = config.get('main', 'password')
database = config.get('main', 'database')


#accessDb gets the connectivity to the access file and (theoretically) allows us to view what is currently in the Access DB.
#Change the file path and the file name after "DBQ=". My filename is Loggers change that at the end of the string.
accessDb = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Administrator\AppData\Local\Programs\Solinst\STS_Gold\db\sts_gold.mdb;')

#The cursor will be used as a database cursor from the pyodbc module to read from and write to databases.
cursor = ""
    
#This function reads data from the access file.
#The access file contains logger data which is to be sent to the MySQL database living on the Linux server.
def readAccessTables():
    #Changes tells us how many items were added to the MySQL Database
    changes=0
    accessCursor = accessDb.cursor()

    #By finding which data is currently in the MySQL database, we can compare this to the data in the access DB to find what is new and needs to be
    #   appended onto the MySQL database.

    #Utilizing the config.ini file we used to set these variable, we can login to the database
    mysqlDb=mysql.connector.connect(host = mysqldb_host, user = username, password = password, database = database)
    mysqlCursor=mysqlDb.cursor(buffered=True, dictionary=True)

    #Selects the data from the LevelLogger table
    #Determines the last value inserted into that was inserted into MySQL
    #This function queries the database and selects all data from the LevelLogger by the date and time reported from recent to the most distant past.
    mysqlCursor.execute("SELECT ID, dateTime, levelInMeters FROM levelogger ORDER BY dateTime DESC")
    
    #fetchone takes the first (and most recent) data from the MySQL database. We can use this to determine if there is ANY data newer than this,
    #   informing us of if we need to insert data into the MySQL database or not.
    mysqlRow=mysqlCursor.fetchone()
    #To debug if we are receiving data from the MySQL database. It is also labeled so we know we are looking at data from the MySQL LevelLogger and not the
    #   Access database.
    #print(mysqlRow)
    #print("MySQL LevelLogger")

    #In order to compare the most recent data in the MySQL Database to the most recent data in the Access Database (logging from hardware in Rhinebeck)
    #   we must convert the MySQL date to a Unix integer. Using the built in UNIX_TIMESTAMP function to pull out a Unix STRING, we can begin this process.
    #   But, it will appear as Eastern time converted from UTC. So, we will need to do some work to get the correct time.
    #We also order by the date in descending order to get the most recent data at the top.
    mysqlCursor.execute("SELECT UNIX_TIMESTAMP(dateTime) from levelogger ORDER BY dateTime DESC")
    #Then, we fetch only the most recent row that was queried. 
    mysqlDate = mysqlCursor.fetchone()
    #Using python's built in str() method, we can convert the data we queried into a string. This gives us something looking like
    #("datetime.datetime({UNIX.TIMESTAMP(time)}), so more work needs to be done.
    mysqlDate = str(mysqlDate)
    #By splitting by spaces, we can get a list of strings including anything queried from the MySQL database. Then, we can take ONLY
    #the unix date and split by a trailing bracket as seen below, so we are left with a list of strings where one string is just the date.
    mysqlDate = mysqlDate.split(" ")
    mysqlDate = mysqlDate[1].split("}")
    #The date can now, using python's built in int() function, be converted to an integer to . 
    mysqlDate = int(mysqlDate[0])
    #We can convert the integer representation back to datetime to change the time zone.
    datetime_mysqlDate = datetime.fromtimestamp(mysqlDate)
    #Using the pytz package, the timezone is now changed to UTC and the time will be correct.
    local_mysqlDate = datetime_mysqlDate.astimezone(pytz.timezone('UTC')).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    print(local_mysqlDate, "the local date and time")
    #Now, for comparison to the access date, we can convert this time back to UTC and get the proper integer representation of the time.
    unix_mysqlDate = time.mktime(datetime.strptime(local_mysqlDate, "%Y-%m-%d %H:%M:%S %Z%z").timetuple())
    print(unix_mysqlDate, "the unix time rep of the mysqlDate")
    #This print statement is used for debugging purposes to check that the functions above are working properly.
    

    #But, we still need to convert the Access date to Unix time. We first query the Access database ALSO in descending order.
    #   As an aside, this need only be done one time. Due to the nature of the STS, LevelLogger and RainLogger data exist in channels 2 and 1 respectively.
    #   This means the date cannot be different for each logger and is only converted once.
    accessCursor.execute("select Date_time from logger_data ORDER BY Date_time DESC")
    #Fetches the most recent date from the Access DB
    accessDate = accessCursor.fetchone()[0]
    #Takes the most recent date, and using the built-in Python command to convert to the datetime datatype, does exactly that BY only taking the
    #   Date_time section of the query. If you look at the data the access DB gives us, it will be a date followed by a space and a comma. This is remedied by
    #   telling the program to take the accessDate variable and only use the part labeled Date_time.
    #accessDate = (accessDate.Date_time).strftime('%Y-%m-%d %H:%M:%S')
    print(accessDate, "Date and time according to Access")
    #The time.mktime(var.timetuple()) function is built-in to Python and converts a date in the datetime datatype to its equivalent Unix integer.
    accessDate = time.mktime(accessDate.timetuple())
    #Used for debugging to visually compare MySQL Dates vs Access dates.
    print(accessDate, "the converted int of accessDate")

    #This block of code will be used to check Access data against the last MySQL update so we only import the rows necessary
    #We convert the Unix Timestamp date we used to decide if the database needs to be updated to YYYY-MM-DD HH:MM:SS format (datetime format)
    convertedsqlDate = datetime.fromtimestamp(unix_mysqlDate)
    print(convertedsqlDate, "convertedsqlDate")
    
    
     
    #This if statement checks if the MySQL database has data in it. If not, it simply adds the data from the access database in the order in which it comes out
    #   which will put it in date order properly.
    if mysqlRow==None: 
        #levelogger --> ch2_data_P = level, ch2_data_T = temperature
        #The Access cursor queries the access database to find data. Channel 2 is the levelogger data. It takes the data from both the water level and temperature. 
        accessCursor.execute('select id, Date_time, ch2_data_P, ch2_data_T from logger_data')
        #Using the access cursor to know which rows to add and when to stop, insert the data we selected into the MySQL database. 
        for row in accessCursor.fetchall():
            try:
                #This execute command inserts new data into the LevelLogger table in the MySQL database.
                mysqlCursor.execute(f"INSERT INTO levelogger (id, dateTime, levelInMeters, tempature) VALUES ({row[0]}, \"{row[1]}\", {row[2]}, {row[3]})")
            except Exception as e:
                #If data is duplicated, comment out the exceptions to debug until you are ready to continue. When ready to continue, comment out the break.
                print(e)
                #break
        
    #If the MySQL database does contain data, do everything specified above, but make sure to format it by row and place the IDs after the most recent one
    #   so the data is in order and not in some random spot. 
    else:
        #Compares the dates logically, so if the accessDate is more recent than the mysqlDate, we query the Access database to insert new changes to the MySQL DB.
        if accessDate > unix_mysqlDate:
            accessCursor.execute('select id, Date_time, ch2_data_P, ch2_data_T from logger_data where Date_time > ?', (convertedsqlDate,))
            print(accessCursor.fetchone())
            changes+=1
            #Using the access cursor to know which rows to add and when to stop, insert the data we selected into the MySQL database. 
            for row in accessCursor.fetchall():
                try:
                    #This execute command inserts new data into the LevelLogger table in the MySQL database.
                    mysqlCursor.execute(f"INSERT INTO levelogger (id, dateTime, levelInMeters, tempature) VALUES ({row[0]}, \"{row[1]}\", {row[2]}, {row[3]})")
                except Exception as e:
                    #If data is duplicated, comment out the exceptions to debug until you are ready to continue. When ready to continue, comment out the break.
                    print(e)
                    #break
        #For debugging (to make sure we are entering this else statement if we KNOW there is data in the MySQL database), use the below iterative command.
        #changes+=1
        
    #Using the access cursor to insert the rows we need, this will try to use the MySQL cursor to take the data we selected from the access DB 
    #   and insert it into the LevelLogger tables. 
    #for row in accessCursor.fetchall():
        #try:
            #This execute command inserts new data into the LevelLogger table in the MySQL database.
            #mysqlCursor.execute(f"INSERT INTO levelogger (id, dateTime, levelInMeters, tempature) VALUES ({row[0]}, \"{row[1]}\", {row[2]}, {row[3]})")
        #except Exception as e:
            #If data is duplicated, comment out the exceptions to debug until you are ready to continue. When ready to continue, comment out the break.
            #print(e)
            #break
        
    #This section of code queries the rainlogger table in the MySQL database to find the most recent rainlogger data IN UNIX TIME.
    mysqlCursor.execute("SELECT UNIX_TIMESTAMP(dateTime) FROM rainlogger ORDER BY dateTime DESC")
    #This gives us the most recent data from the rainlogger to compare to the Access Database. This way, if there is ANYTHING newer than this, we 
    #   know we have to add to the MySQL database.
    mysqlRainDate = mysqlCursor.fetchone()
    #Once we have pulled out the most recent date in the MySQL database, we need to convert it to a string.
    #HOWEVER, this will turn the data we queried into a string including spaces and the type of data we pulled.
    mysqlRainDate = str(mysqlRainDate)
    #To combat this issue, we will split the list by spaces. This allows us to see only the integer we need, but a left facing bracket will be part of that string.
    mysqlRainDate = mysqlRainDate.split(" ")
    #So, we will split the rainlogger date by "}" giving us only a string at position 0 in the list of the unix integer.
    mysqlRainDate = mysqlRainDate[1].split("}")
    #Now, we can convert the Unix time string to an integer. This allows us to compare it to the Access date. 
    mysqlRainDate = int(mysqlRainDate[0])    
    #We can convert the integer representation back to datetime to change the time zone.
    datetime_mysqlRainDate = datetime.fromtimestamp(mysqlRainDate)
    #Using the pytz package, the timezone is now changed to UTC and the time will be correct.
    local_mysqlRainDate = datetime_mysqlRainDate.astimezone(pytz.timezone('UTC')).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    print(local_mysqlRainDate, "the local date and time")
    #Now, for comparison to the access date, we can convert this time back to UTC and get the proper integer representation of the time.
    unix_mysqlRainDate = time.mktime(datetime.strptime(local_mysqlRainDate, "%Y-%m-%d %H:%M:%S %Z%z").timetuple())
    print(unix_mysqlRainDate, "the unix time rep of the My SQL RainLogger Date")
    #For debugging, use the print statement above to make sure the date is coming out of the MySQL database and compare visually to the Access date.

    convertedsqlRainDate = datetime.fromtimestamp(unix_mysqlRainDate)
    print(convertedsqlRainDate, "convertedsqlRainDate")
    
    #If the MySQL table is empty, select ALL data from the access database for the rainlogger to port over. Channel 1 tells us
    #   we are taking RAINLOGGER data.
    if mysqlRow==None:
        #This execute command queries the RainLogger data column from the Access Database.
        accessCursor.execute('select ID, Date_time, ch1_data_P from logger_data')
        #Using the access cursor to know which rows to add and when to stop, insert the data we selected into the MySQL database. 
        for row in accessCursor.fetchall():
            try:
                #This execute command inserts the new data into the RainLogger table in the MySQL database.
                mysqlCursor.execute(f"INSERT INTO rainlogger (ID, dateTime, rainFallInMilliMeters) VALUES ({row[0]}, \"{row[1]}\", {row[2]})")
            
            except Exception as e:
                #If data is duplicated, comment out the exceptions to debug until you are ready to continue. When ready to continue, comment out the break.
                print(e)
                #break

    #If the MySQL table has data, select the data which is more recent than any of which is in the MySQL database and order it properly.
    else:
        #Compare the access date to the MySQL rainlogger table date. If the access database has more recent data than that in the MySQL
        #Database, continue to querying the access database. 
        if accessDate > unix_mysqlRainDate:
            #This queries the Access database to find any data item which is more recent than the last one in the MySQL table.
            accessCursor.execute('select ID, Date_time, ch1_data_P from logger_data where Date_time > ?', (convertedsqlRainDate,))
            changes+=1
            #Using the access cursor to know which rows to add and when to stop, insert the data we selected into the MySQL database. 
            for row in accessCursor.fetchall():
                try:
                    #This execute command inserts the new data into the RainLogger table in the MySQL database.
                    mysqlCursor.execute(f"INSERT INTO rainlogger (ID, dateTime, rainFallInMilliMeters) VALUES ({row[0]}, \"{row[1]}\", {row[2]})")
            
                except Exception as e:
                    #If data is duplicated, comment out the exceptions to debug until you are ready to continue. When ready to continue, comment out the break.
                    print(e)
                    #break

    #Using the access cursor to know which rows to add and when to stop, insert the data we selected into the MySQL database. 
    #for row in accessCursor.fetchall():
        #try:
            #This execute command inserts the new data into the RainLogger table in the MySQL database.
            #mysqlCursor.execute(f"INSERT INTO rainlogger (ID, dateTime, rainFallInMilliMeters) VALUES ({row[0]}, \"{row[1]}\", {row[2]})")
            
        #except Exception as e:
            #If data is duplicated, comment out the exceptions to debug until you are ready to continue. When ready to continue, comment out the break.
            #print(e)
            #break

            
    #For debugging, query the Access database and check which data is most recent in the access database to see if it is receiving data from the 
    #   loggers AND also have the ability to directly compare data to the MySQL database to see WHY something isn't working, for example,
    #   if the Access Database has been purged but the MySQL database has not been, this will clue us into that by spitting out IDs
    #   lower than those in the MySQL database from before the current date. The IDs are iterative, so if the date is earlier than the
    #   date in the most recent datapoint in the Access database, something is off. 
    accessCursor.execute('select ID, Date_time, ch2_data_P, ch2_data_T from logger_data ORDER BY Date_time DESC')
    print(accessCursor.fetchone())
    print("Access LevelLogger")
   
    #This debugging block queries the RainLogger column in the same way as the LevelLogger debugging block above for its data to see what the most recent data point is. 
    accessCursor.execute('select ID, Date_time, ch1_data_P from logger_data ORDER BY Date_time DESC')
    print(accessCursor.fetchone())
    print("Access RainLogger")

    #Print out new events by using the changes variable. This is formatted in a way so that the first set of brackets is the time in which we
    #   tried to port over data and the second set is the number of changes. 
    print('{} - {} new events'.format(datetime.now(),changes))

    #Closing the connections
    mysqlDb.commit() #commits the inserts
    mysqlCursor.close()
    mysqlDb.close()

    accessCursor.close()

    #Deletes variables
    del mysqlCursor
    del mysqlDb
    

#calls the readAccessTables function in a forever loop
#The loop will sleep for half an hour to account for delays in the server receiving data from the Solinst field devices.
while True:
    try:
      readAccessTables()
    except Exception as e:
        print(datetime.now())
        print(e)
    time.sleep(1800)
    


############################################### ORIGINAL CODE FOR REFERENCE TO ANY CHANGES MADE ############################################
# #Before you can install pyodbc, install microsoft c++ tools. They can be found at https://docs.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170
# #Before you can pip install pyodbc, do "pip install wheel"
# #'pip install pyodbc' in the terminal
# #'pip install sqlalchemy' in the terminal
# #this filecreates a connection to a microsoft access file, reads it and puts it in the MySQL database.


# import sys
# sys.path.append(r"c:\users\jointstudy\appdata\local\packages\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\localcache\local-packages\python39\site-packages")

# from datetime import date, datetime
# import pyodbc
# import time
# import mysql.connector

# # Getting variables from config.ini
# from configparser import ConfigParser
# config = ConfigParser()

# config.read(r'C:\Users\jointstudy\Desktop\MySQL-config.ini')
# mysqldb_host = config.get('main', 'mysqldb_host')
# username = config.get('main', 'username')
# password = config.get('main', 'password')
# database = config.get('main', 'database')





# #accessDb gets the connectivity to the access file
# #Change the file path and the file name after "DBQ=". My filename is Loggers change that at the end of the string.
# accessDb = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jointstudy\AppData\Local\VirtualStore\Program Files (x86)\Solinst\STS_Gold\db\sts_gold.mdb;')
# cursor = ""




    
# #This function reads data from the access file and calls populateSqlDatabase function
# def readAccessTables():
#     changes=0
#     accessCursor = accessDb.cursor()

#     #Selects the data from the levelLogger table and calls the populateSqlDatbase function
#     mysqlDb=mysql.connector.connect(host=mysqldb_host, user=username, password=password, database=database)
#     mysqlCursor=mysqlDb.cursor(buffered=True, dictionary=True)

#     #Determines the last value inserted into that was inserted into MySQL
#     mysqlCursor.execute("SELECT id, dateTime, levelInMeters FROM levelogger ORDER BY dateTime DESC")
#     mysqlRow=mysqlCursor.fetchone()
#     #print(mysqlRow)

    
#     if mysqlRow==None: 
#         # levelogger --> ch2_data_P = level, ch2_data_T = tempature
#         accessCursor.execute('select ID, Date_time, ch2_data_P, ch2_data_T from logger_data')
#     else:
#         accessCursor.execute('select ID, Date_time, ch2_data_P, ch2_data_T from logger_data where ID > {}'.format(mysqlRow['id']))
#         #debugging
#         #changes+=1
#     for row in accessCursor.fetchall():
#         try:
#             mysqlCursor.execute(f"INSERT INTO levelogger (id, dateTime, levelInMeters, tempature) VALUES ({row[0]}, \"{row[1]}\", {row[2]}, {row[3]})")
#         except Exception as e:
#             #print(e)
#             break
#     mysqlCursor.execute("SELECT id,dateTime FROM rainlogger ORDER BY dateTime DESC")
#     mysqlRow=mysqlCursor.fetchone()
#     #mysqlRow = mysqlCursor.fetchall()
#     print(mysqlRow)
#     print("MySQL")

#     if mysqlRow==None:
#         accessCursor.execute('select ID, Date_time, ch1_data_P from logger_data')
        
#     else:
#         accessCursor.execute('select ID, Date_time, ch1_data_P from logger_data where ID > {}'.format(mysqlRow['id']))
        
#     for row in accessCursor.fetchall():
#         try:
#             mysqlCursor.execute(f"INSERT INTO rainlogger (id, dateTime, rainFallInMilliMeters) VALUES ({row[0]}, \"{row[1]}\", {row[2]})")
#         except Exception as e:
#             break
            
#     #debugging
#     accessCursor.execute('select ID, Date_time, ch2_data_P, ch2_data_T from logger_data')
#     print(accessCursor.fetchone())
#     print("Access")
#     print('{} - {} new events'.format(datetime.now(),changes))

#     #Closing the connections
#     mysqlDb.commit() #commits the inserts
#     mysqlCursor.close()
#     mysqlDb.close()

#     accessCursor.close()

#     #Deletes variables
#     del mysqlCursor
#     del mysqlDb
    

# #calls the readAccessTables function in a forever loop
# #loop will sleep for a half an hour and then call the function again
# while True:
#     try:
#       readAccessTables()
#     except Exception as e:
#         print(datetime.now())
#         print(e)
#     time.sleep(1800)
    
