from flask import Flask, request
from dao import DataAccessObject
from service import check_user,add_user

app = Flask(__name__)

# Employee signup
'''
End point implementation
API Implementation
Backend code 
'''
@app.route('/')
def home():
    return "<h1>App is in the progress, Wait for some time</h1>"

# db = DataAccessObject("localhost","postgres","postgres","9246743691",5432)

@app.route('/createdb', methods=['GET'])
def create_db():
    with DataAccessObject("localhost","postgres","postgres","9246743691",5432) as cursor:
        cursor.execute("""CREATE TABLE employee ("firstName VARCHAR(50),lastName VARCHAR(100), eid INTEGER, Userid VARCHAR(100), password VARCHAR(50),
        mobileno VARCHAR(15), emailid VARCHAR(50), dob VARCHAR(50), address VARCHAR(50), gender VARCHAR(10),doj VARCHAR(50), technology VARCHAR(50))""")
        return "<h2>Table created successfully.</h2>"

@app.route('/esignup/',methods = ['POST'])
def esignup():
    data = request.get_json()
    print("Data : ", data)
    print("Signup operation in Progress")

    is_exists = check_user(data['eid'], data['userid'])
    print(is_exists)
    if is_exists == True:
    # #     # Server side validation

    
    # 1.Check userid, Eid exists in db or not
    #     1. If exists send error message
    #     2. Else pass data to service layer
    
    # #     # Pass data to service layer
        return "The user already exist,please try again with different user."
    else:
        resp = add_user(data['firstname'],data['lastname'],data['eid'],data['userid'],data['password'],data['mobileno'],data['emailid'],data['dob'],data['address'],data['gender'],data['doj'],data['technology'])

        return resp


if __name__ == '__main__':
    app.run()