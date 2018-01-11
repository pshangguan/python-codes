from flask import Flask

empDB=[
 {
 'id':'101',
 'name':'Saravanan S',
 'title':'Technical Leader'
 },
 {
 'id':'201',
 'name':'Rajkumar P',
 'title':'Sr Software Engineer'
 }
 ]

@app.route('/empdb/employee',methods)
def getAllEmp():
    return jsonify({'emps':empDB})
