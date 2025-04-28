from flask import request, jsonify
from database.database import get_db
from modules.PermissionModule.services.module_action_services import ModuleActionService
from utils.serialize import serialize_model
from utils.request_utils import get_pagination_params, paginated_response, get_filter_params
from middleware.auth import require_auth
class ModuleActionController:

    @staticmethod
    def get_all_module_actions():
        try:
            with get_db() as db:
                service = ModuleActionService(db)
                filters = get_filter_params()
                limit, offset, order_by = get_pagination_params()
                records, total = service.get_all(limit, offset, order_by, filters)

                return jsonify(paginated_response(records, total, limit, offset, serialize_model)), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def get_module_action_by_id(id):
        try:
            with get_db() as db:
                service = ModuleActionService(db)
                record = service.get_by_id(id)
                if record:
                    return jsonify(serialize_model(record)), 200
                return jsonify({'error': 'Module-Action relation not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def create_module_action():
        try:
            with get_db() as db:
                service = ModuleActionService(db)
                data = request.json
                record = service.create(data)
                return jsonify(serialize_model(record)), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def update_module_action(id):
        try:
            with get_db() as db:
                service = ModuleActionService(db)
                data = request.json
                record = service.update(id, data)
                if record:
                    return jsonify(serialize_model(record)), 200
                return jsonify({'error': 'Module-Action relation not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @staticmethod
    def delete_module_action(id):
        try:
            with get_db() as db:
                service = ModuleActionService(db)
                if service.delete(id):
                    return jsonify({'message': 'Module-Action relation deleted'}), 200
                return jsonify({'error': 'Module-Action relation not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
