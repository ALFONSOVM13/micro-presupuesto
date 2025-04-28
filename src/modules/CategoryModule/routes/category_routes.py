from flask import Blueprint
from modules.CategoryModule.controllers.category_controller import CategoryController

category_bp = Blueprint('category', __name__)

category_bp.get('/categories')(CategoryController.get_all)
category_bp.get('/category/<int:category_id>')(CategoryController.get_by_id)
category_bp.post('/create-category')(CategoryController.create)
category_bp.put('/update-category/<int:category_id>')(CategoryController.update)
category_bp.delete('/delete-category/<int:category_id>')(CategoryController.delete)
