# coding: utf-8

import pymysql
import sys


class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    def transfer(self, source_id, target_id, money):
        try:
            self.check_account_available(source_id)
            # self.check_account_available(target_aaountid)
            self.has_enough_money(source_id, money)
            self.reduce_money(source_id, money)
            self.add_money(target_id, money)

            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def check_account_available(self, source_accountid):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where account_id=%s" % source_accountid
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchall()
            if len(result) != 1:
                raise Exception('账号不存在')
        finally:
            cursor.close()

    def has_enough_money(self, source_accountid, money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where account_id=%s and money>%s" % (source_accountid, money)
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchall()
            if len(result) != 1:
                raise Exception('账号余额不足')
        finally:
            cursor.close()

    def add_money(self, target_aaountid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money = money + %s where account_id=%s" % (money, target_aaountid)
            print(sql)
            cursor.execute(sql)
            result = cursor.rowcount
            if result != 1:
                raise Exception('账号加款失败')
        finally:
            cursor.close()

    def reduce_money(self, source_accountid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money = money - %s where account_id=%s" % (money, source_accountid)
            print(sql)
            cursor.execute(sql)
            result = cursor.rowcount
            if result != 1:
                raise Exception('账号减款失败')
        finally:
            cursor.close()


if __name__ == '__main__':
    source_id = sys.argv[1]
    target_id = sys.argv[2]
    money = sys.argv[3]

    conn = pymysql.connect("localhost", "root", "root", "py_test")

    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(source_id, target_id, money)
    except Exception as e:
        print(e)
    finally:
        conn.close()
