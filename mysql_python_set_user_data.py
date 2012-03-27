#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
ユーザの接続情報を保持する
"""
class UserData():
	def __init__(self,usr,pwd,schm):
		self.usr = usr
		self.pwd = pwd
		self.schm = schm
