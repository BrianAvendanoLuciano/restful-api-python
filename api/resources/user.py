from flask import request, jsonify
from flask_restful import Resource, abort

from extensions import db
from models.users import User
from api.schemas.user import UserSchema

class UserList(Resource):
    def get(self):
        users = User.query.all()
        schema = UserSchema(many=True)
        return {"results": schema.dump(users)}

    def post(self):
        schema = UserSchema()
        validated_data = schema.load(request.json)
        user = User(**validated_data)
        
        db.session.add(user)
        db.session.commit()
        
        return {"msg":"User created", "user": schema.dump(user)}
    
class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        schema = UserSchema()
        
        return {"user": schema.dump(user)}
    
    def put(self, user_id):
        schema = UserSchema(partial=True)    
        user = User.query.get_or_404(user_id)
        user = schema.load(request.json, instance=user)
        
        db.session.add(user)
        db.session.commit()
            
        return {"msg": "User updated", "user": schema.dump(user)}
    
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        
        db.session.delete(user)
        db.session.commit()
            
        return {"message": "User deleted"}