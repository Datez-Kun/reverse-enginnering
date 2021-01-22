account = {
	"Username":"x",
	"Password":"x"
}
license = "x"
tradeset = {
	"BaseTrade":"0.01",
	"C1":"5", 							#5-95
	"C2":"95", 							#5-95
	"TradeCount_1":"1",					#1-200
	"TradeCount_2":"10", 					#1-200
	"MultiplyOnWin":"0", 				## 0 untuk OFF 
	"MultiplyOnLose":"0", 				## 0 untuk OFF 
	"MaxBaseTrade":{
		"Toogle":"OFF",						#ON/OFF
		"Max":"0",
		"ResetOnLoseMaxTrade":"OFF", 		# ON/OFF
		"StopOnLoseMaxTrade":"OFF"},			# ON/OFF
	"ClientSeed":"0",				#max 32 digits
}

tools = {
	"AddDelayTrade":"0",				#Delay Per Trade
	"AddDelayTradeWin":"0",				#Delay Per Trade Win
	"AddDelayTradeLose":"0",				#Delay Per Trade Lose
	"RecoveryMultiplier":"1",			# 1 untuk OFF. BaseTrade Lose Terakhir di Kali RecoveryMultiplier
	"RecoveryIncrease":"0",	 			# 0 untuk OFF. BaseTrade Lose Terakhir di Tambah RecoveryIncrease
	"TargetProfit":"0",				#0 untuk OFF
	"StopLoseBalance":"0", 				#0 untuk OFF
	"ForceTC1AfterLose":"OFF",			#ON/OFF
	"ChangeTCAfterLose":{
		"Toogle":"OFF",
		"ChangeTo":"10"},
	"ContinueLastBase":"OFF",			#ON/OFF. Fungsinya Kalau Lose Ingin Lanjutkan Base Terakhir atau Tidak		
	"SmartRecovery":"OFF"				#ON/OFF. Fungsinya Melanjutkan Recovery Sampai Profit Kembali Semula
}
