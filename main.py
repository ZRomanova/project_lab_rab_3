from datetime import datetime as dt, timedelta


class Calculator:
    def __init__(self, limit) -> None:
        self.limit = limit
        self.records = []

    def add_record(self, record): # Сохранять новую запись о расходах / пище
        self.records.append(record)

    def get_today_stats(self): # Считать, сколько денег/каллорий потрачено сегодня 
        today = dt.now().strftime('%d.%m.%Y')
        count = 0
        for record in self.records:
            if dt.strftime(record.date, '%d.%m.%Y') == today:
                count += record.amount
        return count

    def get_week_stats(self): # Считать, сколько денег/калорий потрачено за последние 7 дней — метод
        today = dt.now()
        week_ago = today - timedelta(days=7)
        count = 0
        for record in self.records:
            if record.date <= today and record.date >= week_ago:
                count += record.amount
        return count

class CashCalculator(Calculator):
    currency_list = {
        "rub": 1,
        "eur": 65,
        "usd": 60
    }
    
    def get_today_cash_remained(self, currency): # Определять, сколько ещё денег можно потратить сегодня в рублях, долларах или евро — метод
        if self.currency_list.get(currency):
            cash = self.get_today_stats() / self.currency_list[currency]
            limit = self.limit / self.currency_list[currency]
        else:
            currency = "rub"
            cash = self.get_today_stats()
        if cash < limit:
            return 'На сегодня осталось %.2f %s' % (limit - cash, currency)
        elif cash == limit:
            return 'Денег нет, держись'
        else:
            return 'Денег нет, держись: твой долг - %.2f %s' % (limit - cash, currency)

class CaloriesCalculator(Calculator):

    def get_calories_remained(self): # Определять, сколько ещё калорий можно/нужно получить сегодня — метод
        if (self.get_today_stats() < self.limit):
            return 'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более %d кКал' % (self.limit - self.get_today_stats())
        else:
            return 'Хватит есть!'


class Record:
    def __init__(self, **kwargs) -> None:
        self.amount = kwargs.get('amount') if kwargs.get('amount') is not None else 0
        self.date = dt.strptime(kwargs.get('date'), '%d.%m.%Y') if kwargs.get('date') is not None else dt.now()
        self.comment = kwargs.get('comment') if kwargs.get('comment') is not None else ''



# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи
# должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment='кофе'))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др', date='08.12.2022'))

print(cash_calculator.get_today_cash_remained('rub'))
print(cash_calculator.get_today_cash_remained('usd'))
print(cash_calculator.get_today_cash_remained('eur'))
# должно напечататься
# На сегодня осталось 555.00 rub 
print(cash_calculator.get_week_stats())
#3445


calories_calculator = CaloriesCalculator(1000)


calories_calculator.add_record(Record(amount=70, comment='киндер сюрприз'))

print(calories_calculator.get_calories_remained())
# Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более 930 кКал