from flask import request, jsonify
from modules.PermissionModule.services.role_services import RoleService
from database.database import get_db
from utils.serialize import serialize_model
from utils.request_utils import get_pagination_params, paginated_response,get_filter_params

class RoleController:

    @staticmethod
    def get_all():
        limit, offset, order_by = get_pagination_params()
        filters = get_filter_params() 
        with get_db() as db:
            service = RoleService(db)
            roles, total = service.get_all(limit, offset, order_by, filters)
            return jsonify(paginated_response(roles, total, limit, offset, serialize_model)), 200
            
    @staticmethod
    def get_by_id(role_id):
        with get_db() as db:
            service = RoleService(db)
            role = service.get_by_id(role_id)
            if not role:
                return jsonify({'error': 'Role not found'}), 404
            return jsonify(serialize_model(role)), 200

    @staticmethod
    def create():
        try:
            data = request.json
            with get_db() as db:
                service = RoleService(db)
                role = service.create(data)
                return jsonify(serialize_model(role)), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def update(role_id):
        try:
            data = request.json
            with get_db() as db:
                service = RoleService(db)
                role = service.update(role_id, data)
                if not role:
                    return jsonify({'error': 'Role not found'}), 404
                return jsonify(serialize_model(role)), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def delete(role_id):
        with get_db() as db:
            service = RoleService(db)
            success = service.delete(role_id)
            if not success:
                return jsonify({'error': 'Role not found'}), 404
            return jsonify({'message': 'Role deleted'}), 200
