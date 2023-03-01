import datetime
import uuid
from dataclasses import dataclass
import datetime

from ..config import load_config


import pyqiwi
config = load_config('.env')
wallet = pyqiwi.Wallet(token=config.misc.qiwi_token, number=config.misc.wallet)


class NotEnoughMoney(Exception):
    pass

class NoPaymentFound(Exception):
    pass

@dataclass
class Payment:
    amount: int
    id: str = None

    def create(self):
        self.id = str(uuid.uuid4())

    def check_payment(self):
        transactions= wallet.history(start_date=datetime.datetime.now() - datetime.timedelta(days=2)).get("transactions")
        for transaction in transactions:
            if transaction.comment:
                if str(self.id) in  transaction.comment:
                    if float(transaction.total.amount) >= float(self.amount):
                        return True
                    else:
                        raise NotEnoughMoney
        else:
            raise NoPaymentFound

    @property
    def invoice(self):
        link= "https://oplata.qiwi.com/create?publicKey={pubkey}&amount={amount}&comment={comment}"
        return link.format(pubkey=config.misc.qiwi_p_pub, amount= self.amount, comment= self.id)