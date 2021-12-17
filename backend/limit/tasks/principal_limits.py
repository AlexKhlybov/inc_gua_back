from app.celery import app
from entity.models import Principal
from ..views import PrincipalLimitsView


@app.task()
def update_principal_limits():
    principals = Principal.objects.all()
    for principal in principals:
        init_params = {}
        init_params['principal_id'] = principal.id
        principal_limits = PrincipalLimitsView(init_params=init_params)
        principal_limits.update()
