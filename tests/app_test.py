
import pytest

from src.app import BankAccount, calculate_discount, is_adult


def test_deposit():
    account = BankAccount("Rayan", 100)

    assert account.deposit(50) is True
    assert account.get_balance() == 150


def test_withdraw():
    account = BankAccount("Rayan", 100)

    assert account.withdraw(30) is True
    assert account.get_balance() == 70


def test_discount():
    assert calculate_discount(100, 10) == 90


def test_is_adult():
    assert is_adult(20) is True
    assert is_adult(15) is False
