from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str="zaid"
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,default=5,description='a deecial value reprsenting the cgpa of the students')

new_student = {'age':'34','email':'zaid@gmail.com','cgpa':3}

student = Student(**new_student)

student_dict=dict(student)
print(student_dict['age'])

student_json=student.model_dump_json()
print(student_json)