from flask import request, make_response, jsonify
from config import app, db, api
from models import Project
from flask_restful import Resource, Api

class Projects(Resource):
    def get(self):
        projects = Project.query.all()
        return make_response(jsonify([project.to_dict for project in projects]), 200)
    
    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify(error="No data was retrieved"), 400)
        
        new_project = Project(
            name = db.Column('name'),
            about = db.Column('about'),
            phase = db.Column('phase'),
            link = db.Column('link'),
            image = db.Column('image')
        )

        db.session.add(new_project)
        db.session.commit()

        return make_response(jsonify(new_project.to_dict()), 201)
    
api.add_resource(Projects, '/projects')

if __name__ == '__main__':
    app.run()


