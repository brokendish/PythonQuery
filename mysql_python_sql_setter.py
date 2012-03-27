#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import MySQLdb as msl
import mysql_python_set_user_data as UsrData

"""
SQLを発行する
"""
class SqlSetter:
	
	def __init__(self,UsrData):
		self.schemaNm=UsrData.schm
		self.userNm=UsrData.usr
		self.pwssWd=UsrData.pwd

	def setSql(self,sqlStr):
		ret_all=[]
		connect=msl.connect(passwd=self.pwssWd, user=self.userNm, db=self.schemaNm)
		
		print sqlStr			#SQLを標準出力（デバグ用）

		#クエリを使用して結果を取得
		connect.query(sqlStr)
		ret=connect.use_result()
		while(True):
			"""
			fetch_row(1,1):
				  0 -- tuples (default)
			          1 -- dictionaries, key=column or table.column if duplicated
				  2 -- dictionaries, key=table.column
			"""
			#get_row=ret.fetch_row(1,1) #結果を辞書形式（連想配列）で返す
			get_row=ret.fetch_row(1,1) 	#結果を２次元配列で返す	
			if not get_row: break
			ret_all.insert(0,get_row[0])
		

		connect.close()				#接続を切る

		return ret_all

	def setSql2(self,sqlStr):
		ret_all=[]
		connect=msl.connect(passwd=self.pwssWd, user=self.userNm, db=self.schemaNm)
		
		print sqlStr			#SQLを標準出力（デバグ用）

		#カーソルを使って全体を取得する場合（メモリリークが起きることがあるみたい）
		cur=connect.cursor()
		#結果を辞書形式（連想配列）で返す
		#cur=connect.cursor(msl.cursors.DictCursor)
		cur.execute(sqlStr)		#SQL実行
		ret_all = cur.fetchall()	#フェッチオール（全部取得しておく）
		cur.close()			#カーソルを閉じる
		connect.close()			#接続を切る


		return ret_all
	
	"""
	ヘッタを付けてタブ区切りにする(CSV出力用)
	"""
	def getRetTabStruct(self,ret_str):
		cati = ""		
		key_list=ret_str[0].viewkeys()				#辞書型のキー（項目名）を取得
		for head in key_list:
			cati = cati + head + "\t"			#タブ区切りで繋ぐ
		cati = cati + "\n"					#項目名を繋げ終わったら改行
	
		for strr in ret_str:					#データ内容を取得
			for get_key in key_list:

				if not isinstance(strr[get_key],str):
					strr[get_key]=str(strr[get_key])#文字型に変換
	
				cati = cati + strr[get_key] + "\t" 	#タブ区切りで繋ぐ
	
			cati = cati + "\n"				#文字列を連結

		return cati

	"""
	ヘッタを付け2次元配列にする  作成中！作成中！作成中！作成中！
	"""
	def getRetStruct(self,ret_str):
		cati=[[]]
		key_list=ret_str[0][1].viewkeys()		#辞書型のキー（項目名）を取得
		for head in key_list:
			cati.insert(0,head)			#ヘッタ部分を配列に挿入
	
		t=1
		for strr in ret_str:					#データ内容を取得
			for get_key in key_list:

				if not isinstance(strr[get_key],str):
					strr[get_key]=str(strr[get_key])#文字型に変換
	
				cati.insert(t,head)			#データ部分を配列に挿入
				t=t+1

		return cati


