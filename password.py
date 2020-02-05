import uuid, hashlib, pymysql.cursors

# get user input
password = input("Enter password: ")

#create salt
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
        sql = "INSERT INTO `Passwords` VALUES (%s, %s)"
        
        # execute the SQL command
        cursor.execute(sql, (salt, hashString))

        connection.commit()

finally:
    connection.close()

# get new uesr input
password = input("Enter password: ")

# update hash
hashed_password = hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

# convert to stirng
newHashString = str(hashed_password)

# output statement based on password entered
if hashString == newHashString:
    print("Password is correct!")
else:
    print("Password is incorrect.")



