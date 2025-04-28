from flask import Flask

from modules.BudgetModule.routes.budget_routes import budget_bp

from modules.CategoryModule.routes.region_routes import region_bp
from modules.CategoryModule.routes.category_routes import category_bp
from modules.CategoryModule.routes.subcategory_routes import subcategory_bp
from modules.CategoryModule.routes.product_routes import product_bp
from modules.CategoryModule.routes.subcategory_detail_routes import subcategory_detail_bp

from modules.FlowModule.routes.flow_routes import flow_bp
from modules.FlowModule.routes.object_state_routes import object_state_bp
from modules.FlowModule.routes.fos_routes import flow_object_state_bp

from modules.PermissionModule.routes.role_routes import role_bp
from modules.PermissionModule.routes.action_routes import action_bp
from modules.PermissionModule.routes.module_routes import module_bp
from modules.PermissionModule.routes.module_action_routes import module_action_bp
from modules.PermissionModule.routes.permission_routes import permission_bp

from modules.ParameterModule.routes.parameter_routes import parameter_bp
from modules.ParameterModule.routes.pv_routes import pv_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(subcategory_detail_bp)
    app.register_blueprint(region_bp)
    app.register_blueprint(parameter_bp)
    app.register_blueprint(pv_bp)
    app.register_blueprint(role_bp)
    app.register_blueprint(action_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(module_bp)
    app.register_blueprint(module_action_bp)
    app.register_blueprint(subcategory_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(permission_bp)
    app.register_blueprint(budget_bp)
    app.register_blueprint(flow_bp)
    app.register_blueprint(object_state_bp)
    app.register_blueprint(flow_object_state_bp)