import uuid, hashlib, pymysql.cursors

password = input("Enter password: ")
salt = str(uuid.uuid4().hex) 

# open-source method to ONE-WAY hash a password
hashed_password = hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

hashString = str(hashed_password)

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='fx9785rk',
                             password='Pernambucano.wolf',
                             db='fx9785rk_Password',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select all Students
        sql = "INSERT INTO `Passwords` VALUES (%s, %s)"
        
        # execute the SQL command
        cursor.execute(sql, (salt, hashString))

        connection.commit()

finally:
    connection.close()

password = input("Enter password: ")

hashed_password = hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

newHashString = str(hashed_password)

if hashString == newHashString:
    print("Password is correct!")
else:
    print("Password is incorrect.")



