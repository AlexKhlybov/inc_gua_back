from app.celery import app
from ..models import LimitFZ
from ..views import FZLimitsView


@app.task()
def update_fz_limits():
    fzs = LimitFZ.objects.all()
    for fz in fzs:
        init_params = {}
        init_params['fz_id'] = fz.id
        fz_limits = FZLimitsView(init_params=init_params)
        fz_limits.update()
