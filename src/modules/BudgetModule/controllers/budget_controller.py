from flask import  jsonify, request, abort
from modules.BudgetModule.services.budget_services import OBudgetService
from modules.BudgetModule.schemas.budget_schema import OBudgetCreate, OBudgetUpdate
from utils.permission import require_permission
from utils.serialize import serialize_model
from utils.request_utils import get_pagination_params, paginated_response, get_filter_params, http_response
from utils.global_message import GlobalMessages
from http import HTTPStatus
from middleware.auth import require_auth
from database.database import get_db


class BudgetController:

    @staticmethod
    @require_auth
    @require_permission("Acceder", "Presupuesto")
    def list_budgets():
        try:
            limit, offset, order_by = get_pagination_params()
            filter = get_filter_params()
            with get_db() as db:
                service = OBudgetService(db)
                budgets, total = service.get_all(limit=limit, offset=offset, order_by=order_by, filters= filter)
            
                return jsonify(paginated_response(budgets, total, limit, offset, serialize_model)), 200
        except Exception as e:
            return http_response(GlobalMessages.ERROR_GET_ALL, {}, [str(e)], HTTPStatus.INTERNAL_SERVER_ERROR)


    @staticmethod
    @require_auth
    @require_permission("Acceder", "Presupuesto")
    def get_budget(budget_id: int):
        with get_db() as db:
            try:
                service = OBudgetService(db)
                budget = service.get_by_id(budget_id)
                if not budget:
                    return jsonify({'error': 'Product not found'}), 404
                return jsonify(serialize_model(budget))
            except Exception as e:
                return http_response(GlobalMessages.ERROR_GET, {}, [str(e)], HTTPStatus.INTERNAL_SERVER_ERROR)
                

    @require_auth
    @staticmethod
    @require_permission("Crear", "Presupuesto")
    def create_budget():
        with get_db() as db:
            try:
                data = request.get_json()
                service = OBudgetService(db)
                budget_data = OBudgetCreate(**data)
                budget = service.create_budget(budget_data)
                
                return jsonify(serialize_model(budget)), 201
            except Exception as e:
                return http_response(GlobalMessages.ERROR_CREATED, {}, [str(e)], HTTPStatus.INTERNAL_SERVER_ERROR)
            

    @require_auth
    @staticmethod
    @require_permission("Actualizar", "Presupuesto")
    def update_budget(self, budget_id: int):
        try:
            data = request.get_json()
            budget_data = OBudgetUpdate(**data)
            budget = self.service.update_budget(budget_id, budget_data)
            if not budget:
                return jsonify({'error': 'Product not found'}), 404
            return jsonify(serialize_model(budget))
        except Exception as e:
            return http_response(GlobalMessages.ERROR_UPDATED, {}, [str(e)], HTTPStatus.INTERNAL_SERVER_ERROR)
            


    @require_auth
    @staticmethod
    @require_permission("Eliminar", "Presupuesto")
    def delete_budget(self, budget_id: int):
        try:
            budget = self.service.delete_budget(budget_id)
            if not budget:
                abort(404, description="Budget not found")
            return jsonify({"message": "Budget deleted"})
        except Exception as e:
            return http_response(GlobalMessages.ERROR_DELETED, {}, [str(e)], HTTPStatus.INTERNAL_SERVER_ERROR)
            