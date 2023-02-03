import pytest
from app.calculations import add,subtract,multiply,divide,BankAccount,InsufficientFunds

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (14,25,39),
    (12,18,30)
])
def test_add(num1, num2, expected):
    assert add(num1,num2) == expected

def test_subtract():
    assert subtract(9,4) == 5

def test_multiply():
    assert multiply(9,4) == 36

def test_divide():
    assert divide(9,3) == 3

def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 70

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance,6) == 55

@pytest.mark.parametrize("deposit, withdraw, expected", [
    (300, 200, 100),
    (1400,500,900),
    (1200,180,1020),
    (200000,30,199970),
])

def test_bank_transaction(zero_bank_account,deposit,withdraw,expected):
    zero_bank_account.deposit(deposit)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == expected

#test exception case
def test_insufficient_funds(zero_bank_account):
    with pytest.raises(InsufficientFunds):
        zero_bank_account.withdraw(200)