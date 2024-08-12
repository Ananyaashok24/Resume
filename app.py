from flask import Flask, render_template,request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/create', methods=['GET','POST'])


def create():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['resumes']
    collection = db['sub']
    if request.method == 'POST':
        try:
            # Retrieve form data
            name = request.form.get('name')
            phone = request.form.get('phone')
            address = request.form.get('address')
            degree = request.form.getlist('degree')
            college = request.form.getlist('college_school')
            percentage_cgpa = request.form.getlist('percentage_cgpa')
            skills=request.form.getlist('skills',[])
            project_title = request.form.getlist('project_title[]')
            project_description = request.form.getlist('project_description[]')
            accomplishment = request.form.getlist('accomplishment')
            hobbies = request.form.getlist('hobbies')

            # Validate form data (add your validation logic here)

            # Construct document
            document = {
                "name": name,
                "phone": phone,
                "address": address,
                "education": [],
                "skills":[],
                "project": [],
                "accomplishment": [],
                "hobbies": []
            }

            # Add education details to document
            for i in range(len(degree)):
                education_entry = {
                   
                    "degree": degree[i],
                    "college_school": college_school[i],
                    "percentage_cgpa": percentage_cgpa[i]
                }
                document["education"].append(education_entry)
                
                
            for i in range(len(skills)):
                skills_entry = {
                    "title":skills[i],
                    }
                document["skills"].append(skills_entry)
            for i in range(len(project_title)):
                project_entry = {
                    "title": project_title[i],
                    "description": project_description[i]
                }
                document["project"].append(project_entry)
            for i in range(len(accomplishment)):
               accomplishment_entry = {
                    "accomplishment": accomplishment[i],
                    
                }
               document["accomplishment"].append(accomplishment_entry)
                
            for i in range(len(hobbies)):
                hobbies_entry = {
                    "hobbies": hobbies[i],
                    
                }
                document["hobbies"].append(hobbies_entry)
            # Insert document into MongoDB
            collection.insert_one(document)
            
            return "Form submitted successfully!"
        except Exception as e:
            return str(e), 400
     

 
    return render_template('test.html')
    
@app.route('/view', methods=['GET'])


def view():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['resumes']
    collection = db['sub']
    document = collection.find_one({})
    print("Hello",document)
 
    name = document["name"]
    phone = document["phone"]
    address = document["address"]
   
    education = document["education"]
    skills=document["skills"]
    projects=document["project"]
    accomplishment=document["accomplishment"]
    hobbies=document["hobbies"]
    
    return render_template('index.html',name=name,phone=phone,address=address,education=education,skills=skills,projects=projects,accomplishment=accomplishment,hobbies=hobbies)


