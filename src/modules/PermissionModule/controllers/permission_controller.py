from flask import request, jsonify
from database.database import get_db
from modules.PermissionModule.services.permission_services import PermissionService
from utils.serialize import serialize_model
from utils.request_utils import get_pagination_params, paginated_response, get_filter_params
class PermissionController:

    @staticmethod
    def get_all_permissions():
        try:
            limit, offset, order_by = get_pagination_params()
            filters = get_filter_params()
            with get_db() as db:
                service = PermissionService(db)
                permissions,total = service.get_all(limit, offset, order_by, filters)
                
                return jsonify(paginated_response(permissions, total, limit, offset, serialize_model)), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def get_permission_by_id(id):
        try:
            with get_db() as db:
                service = PermissionService(db)
                permission = service.get_by_id(id)
                if permission:
                    return jsonify(serialize_model(permission)), 200
                return jsonify({'error': 'Permission not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def create_permission():
        try:
            with get_db() as db:
                service = PermissionService(db)
                data = request.json
                permission = service.create(data)
                return jsonify(serialize_model(permission)), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def update_permission(id):
        try:
            with get_db() as db:
                service = PermissionService(db)
                data = request.json
                permission = service.update(id, data)
                if permission:
                    return jsonify(serialize_model(permission)), 200
                return jsonify({'error': 'Permission not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def delete_permission(id):
        try:
            with get_db() as db:
                service = PermissionService(db)
                if service.delete(id):
                    return jsonify({'message': 'Permission deleted'}), 200
                return jsonify({'error': 'Permission not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
