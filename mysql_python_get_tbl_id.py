#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import MySQLdb as msl
import mysql_python_set_user_data as UsrData

"""
指定スキーマのテーブル一覧を取得
"""
class GetTableId:
	
	def __init__(self,UsrData):
		self.schemaNm=UsrData.schm
		self.userNm=UsrData.usr
		self.pwssWd=UsrData.pwd

	"""
	テーブルID取得
	"""
	def getTblId(self):
		connect=msl.connect(passwd=self.pwssWd, user=self.userNm, db=self.schemaNm)
		cur=connect.cursor()
		sql_str = 'select table_name from INFORMATION_SCHEMA.TABLES where table_schema=' + '"' + self.schemaNm + '"'
		print	sql_str

		cur.execute(sql_str)
		ret_all = cur.fetchall()
		
		for inrec in ret_all:
			#print inrec[0],inrec[1],inrec[3],inrec[4]
			print inrec[0]
		
		cur.close()
		connect.close()

		return ret_all

	"""
	カラム名取得
	"""
	def getColumns(self,tblid):
		connect=msl.connect(passwd=self.pwssWd, user=self.userNm, db=self.schemaNm)
		cur=connect.cursor()
		sql_str = 'select COLUMN_NAME from INFORMATION_SCHEMA.columns where table_schema=' + '"' + self.schemaNm + '"' + ' and TABLE_NAME = ' + '"' + tblid + '"' + ' order by ordinal_position desc'

		print	sql_str

		cur.execute(sql_str)
		ret_all = cur.fetchall()
		
		for inrec in ret_all:
			#print inrec[0],inrec[1],inrec[3],inrec[4]
			print inrec[0]
			
		
		cur.close()
		connect.close()

		return ret_all

	"""
	プライマリキー取得
	"""
	def getKeyColumns(self,tblid):
		connect=msl.connect(passwd=self.pwssWd, user=self.userNm, db=self.schemaNm)
		cur=connect.cursor()
		#文字連結に｜｜が使えないので「concat」使用：Mysql依存
		sql_str = 'select concat("[",CONSTRAINT_NAME,"]::",COLUMN_NAME) from INFORMATION_SCHEMA.KEY_COLUMN_USAGE where table_name = ' + '"' + tblid + '"'


		print	sql_str

		cur.execute(sql_str)
		ret_all = cur.fetchall()
		
		for inrec in ret_all:
			#print inrec[0],inrec[1],inrec[3],inrec[4]
			print inrec[0]
			
		
		cur.close()
		connect.close()

		return ret_all

	"""
	スキーマ情報取得
	"""
	def getSchema(self):
		connect=msl.connect(passwd=self.pwssWd, user=self.userNm, db=self.schemaNm)
		cur=connect.cursor()
		sql_str = 'select SCHEMA_NAME from INFORMATION_SCHEMA.SCHEMATA'

		print	sql_str

		cur.execute(sql_str)
		ret_all = cur.fetchall()
		
		for inrec in ret_all:
			#print inrec[0],inrec[1],inrec[3],inrec[4]
			print inrec[0]
			
		
		cur.close()
		connect.close()

		return ret_all

