import uuid
import hashlib
import pymysql.cursors

# get user input
password = input("Enter password: ")

# create salt
salt = str(uuid.uuid4().hex)

# open-source method to ONE-WAY hash a password
hashed_password = hashlib.sha512((password + salt).encode('utf-8')).hexdigest()
# convert to string
hashString = str(hashed_password)

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='fx9785rk',
                             password='',
                             db='fx9785rk_Password',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # insert hash and salt into DB
        sql = "INSERT INTO `Passwords`(`Salt`, `Hash`) VALUES (%s, %s)"

        # execute the SQL command
        cursor.execute(sql, (salt, hashString))

        connection.commit()

        sql = "SELECT * FROM Passwords ORDER BY ID DESC LIMIT 1"
        cursor.execute(sql)
        for result in cursor:
            savedSalt = result.get('Salt')
            savedHash = result.get('Hash')

    # get new user input
    password = input("Enter password: ")

    # update hashed password
    hashed_password = hashlib.sha512(
        (password + savedSalt).encode('utf-8')).hexdigest()

    # convert to string
    newHashString = str(hashed_password)

    # # output statement based on password entered
    if newHashString == savedHash:
        print("Password is correct!")
    else:
        print("Password is incorrect.")

finally:
    connection.close()
