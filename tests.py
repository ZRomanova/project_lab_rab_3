import pytest

from main import CashCalculator, CaloriesCalculator, Record

@pytest.fixture()
def cash_calc():
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145, comment='кофе'))
    cash_calculator.add_record(Record(amount=300, comment='Чаи гонять'))
    cash_calculator.add_record(Record(amount=2000, comment='Еда в дорогу'))
    return cash_calculator.get_today_cash_remained()

@pytest.fixture()
def cal_calc():
    calories_calculator = CaloriesCalculator(1500)
    calories_calculator.add_record(Record(amount=1234, comment='БИГ ЖРАЧКА.'))
    calories_calculator.add_record(Record(amount=42, comment='Молоко', ))
    calories_calculator.add_record(Record(amount=130, comment='Овсянка', ))
    return calories_calculator.get_calories_remained()

def test_cashCalc(cash_calc):
    assert cash_calc == 'Денег нет, держись: твой долг - 1445.00 rub'

def test_CalCalc(cal_calc):
    assert cal_calc == 'Хватит есть!'
