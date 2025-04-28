from flask import Blueprint
from modules.BudgetModule.controllers.budget_controller import BudgetController

budget_bp = Blueprint('budgets', __name__)


budget_bp.get('/budgets')(BudgetController.list_budgets)
budget_bp.get('/budget/<int:budget_id>')(BudgetController.get_budget)
budget_bp.post('/create-budget')(BudgetController.create_budget)
budget_bp.put('/update-budget/<int:budget_id>')(BudgetController.update_budget)
budget_bp.delete('/delete-budget/<int:budget_id>')(BudgetController.delete_budget)
