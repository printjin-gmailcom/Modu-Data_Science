# -*- coding: utf-8 -*-
"""iv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q7KcOszfJn0hU5YEZ_MwgKBQx9QdrTIK
"""

# mysql ~ pymysql 사용 #



# mysql -u root -p # 명령프롬프트에서 다운로드

CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';

CREATE DATABASE db;

GRANT ALL ON db.* TO 'user'@'localhost';

mysql -u user -p db

USE db;
CREATE TABLE employee (empname TINYTEXT, salary FLOAT, hired DATE);

DROP TABLE employee;

CREATE TABLE employee (id INT PRIMARY KEY AUTO_INCREMENT,
updated TIMESTAMP, empname TINYTEXT NOT NULL, salary FLOAT NOT NULL, hired DATE);

ALTER TABLE employee ADD INDEX(hired);

DROP INDEX hired ON employee;

ALTER TABLE employee ADD UNIQUE(enpname(255));



INSERT INTO employee VALUES(NULL,NULL,"John Smith",35000,NOW());

SHOW WARNINGS;

INSERT INTO employee VALUES(NULL,NULL,"John Smith",35000,NOW());

INSERT IGNORE INTO employee VALUES(NULL,NULL,"John Smith",35000,NOW());

DELETE FROM employee WHERE salary<11000 AND empname='John Smith';

DELETE FROM employee

DELETE FROM employee WHERE id=387513;

UPDATE employee SET salary=35000 WHERE hired=CURDATE();

UPDATE employee SET salary=salary+1000 WHERE empname="John Smith";

SELECT empname,salary FROM employee WHERE empname="John Smith";

SELECT empname,salary FROM employee;

SELECT * FROM employee WHERE hired>= '2000-01-01' ORDER BY salary DESC;

SELECT(hired>'2001-01-01') AS Recent, AVG (salary) FROM employee GROUP BY (hired>'2001-01-01');

SELECT AVG(salary),MIN(hired),MAX(hired) FROM employee GROUP BY YEAR(hired) HAVING MIN(hired)>'2001-01-01';

CREATE TABLE position (eid INT, description TEXT);
INSERT INTO position (eid,description) VALUES (6,'Imposter'), (1,'Accountant'),(4,'Programmer'),(5,'President');
ALTER TABLE position ADD INDEX(eid);

SELECT employee.empname,position.description
FROM employee,position WHERE employee.id=position.eid
ORDER BY position.description;



# conda install pymysql ~ 아나콘다프롬프트에서 다운도르

import pymysql
conn = pymysql.connect(host="localhost", port=3306, user="dsuser", passwd="badpassw0rd", db="dsdb")
cur = conn.cursor()

query = '''
SELECT employee.empname,position.description FROM employee,position WHERE employee.id=position.eid ORDER BY position.description
'''
n_rows = cur.execute(query)

results = list(cur.fetchall())
results



# conda install pymongo ~ 아나콘다 프롬프트 다운로드

import pymongo as mongo

client1 = mongo.MongoClient()

client2 = mongo.MongoClient("localhost", 27017)

client3 = mongo.MongoClient("mongodb://localhost:27017/")

person1 = {"empname" : "John Smith", "dob" : "1957-12-24"}
person2 = {"_id" : "XVT162", "empname" : "Jane Doe", "dob" : "1964-05-16"}
person_id1 = people.insert_one(person1).inserted_id
person_id1

person1

person_id2 = people.insert_one(person2).inserted_id
person_id2

persons = [{"empname" : "Abe Lincoln", "dob" : "1809-02-12"}, {"empname" : "Anon I. Muss"}]
result = people.insert_many(persons)
result.inserted_ids

everyone = people.find()
list(everyone)

list(people.find({"dob" : "1957-12-24"}))

people.find_one()

people.find_one({"empname" : "Abe Lincoln"})

people.find_one({"_id" : "XVT162"})

people.count()

people.find({"dob": "1957-12-24"}).count()

people.find().sort("dob")

result = people.delete_many({"dob" : "1957-12-24"})
result.deleted_count



