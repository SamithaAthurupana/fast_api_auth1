from dataclasses import dataclass
from fastapi import FastAPI,HTTPException
from typing import Dict
from pydantic import BaseModel


app = FastAPI()


class Student(BaseModel):
    id: str
    name: str
    age: int

students: Dict[str, Student] = {}

@app.get("/")
def root():
    return "Student API "

@app.get("/students")
def get_students():
    return list(students.values())

@app.get("/students/{student_id}")
def get_student(student_id : str):
    std = Student(id="1", name="test", age=19)
    students[std.id] = std
    return students.get(student_id)

@app.post("/students")
def create_student(student: Student):
    students[student.id] = student
    return {"message": "successfully Created student", "student": student}

@app.put("/students/{student_id}")
def update_student(student_id:str, student: Student):
    if student_id not in students.keys():
        raise HTTPException(status_code=404, detail="Student id not found!")
    students[student_id] = student
    return {"message": "successfully updated successfully", "student": student }

@app.delete("/students/{student_id}")
def delete_student(student_id:str):
    if student_id not in students.keys():
        raise HTTPException(status_code=404, detail="Student id not found to delete!")
    deleted_std = students.pop(student_id)

    return {"message": "successfully deleted", "student": deleted_std }