from flask import request, jsonify
from database.database import get_db
from modules.CategoryModule.services.subcategory_services import SubcategoryService
from utils.serialize import serialize_model
from utils.permission import require_permission
from utils.request_utils import get_pagination_params, paginated_response, get_filter_params
from middleware.auth import require_auth
class SubcategoryController:

    @staticmethod
    @require_auth
    @require_permission("Acceder", "Inventario")
    def get_all_subcategories():
        try:
            limit, offset, order_by = get_pagination_params()
            filters = get_filter_params()
            with get_db() as db:
                service = SubcategoryService(db)
                subcategories, total = service.get_all(limit=limit, offset=offset, order_by=order_by,filters=filters)
                return jsonify(paginated_response(subcategories, total, limit, offset, serialize_model)), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    @require_auth
    @require_permission("Acceder", "Inventario")
    
    def get_subcategory_by_id(id):
        try:
            with get_db() as db:
                service = SubcategoryService(db)
                subcategory = service.get_by_id(id)
                if subcategory:
                    return jsonify(serialize_model(subcategory)), 200
                return jsonify({'error': 'Subcategory not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    @require_auth
    @require_permission("Crear", "Inventario")
    
    def create_subcategory():
        try:
            with get_db() as db:
                service = SubcategoryService(db)
                data = request.json
                subcategory = service.create(data)
                return jsonify(serialize_model(subcategory)), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    @require_auth
    @require_permission("Actualizar", "Inventario")
    
    def update_subcategory(id):
        try:
            with get_db() as db:
                service = SubcategoryService(db)
                data = request.json
                subcategory = service.update(id, data)
                if subcategory:
                    return jsonify(serialize_model(subcategory)), 200
                return jsonify({'error': 'Subcategory not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    @require_auth
    @require_permission("Eliminar", "Inventario")
    
    def delete_subcategory(id):
        try:
            with get_db() as db:
                service = SubcategoryService(db)
                if service.delete(id):
                    return jsonify({'message': 'Subcategory deleted'}), 200
                return jsonify({'error': 'Subcategory not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
