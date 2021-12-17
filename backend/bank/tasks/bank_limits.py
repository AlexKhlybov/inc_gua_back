from app.celery import app
from ..models import Bank
from ..views import BankLimitsView


@app.task()
def update_bank_limits():
    banks = Bank.objects.all()
    for bank in banks:
        init_params = {}
        init_params['bank_id'] = bank.id
        bank_limits = BankLimitsView(init_params=init_params)
        bank_limits.update()
