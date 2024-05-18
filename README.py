//+------------------------------------------------------------------+
//|                                                   SimpleEA.mq5   |
//|                        Copyright 2024, MetaQuotes Software Corp. |
//|                                        https://www.metaquotes.net|
//+------------------------------------------------------------------+
#include <Trade\Trade.mqh>

//--- deklarasi instance kelas CTrade
CTrade trade;

//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
  {
   //--- initialisasi
   return(INIT_SUCCEEDED);
  }
//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
   //--- deinitialisasi
  }
//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
  {
   //--- mendapatkan harga penutupan dari dua candle terakhir
   double closeCurrent = iClose(_Symbol, _Period, 0);
   double closePrevious = iClose(_Symbol, _Period, 1);
   
   //--- kondisi untuk membuka posisi buy
   if (closeCurrent > closePrevious)
     {
      //--- membuka posisi buy
      trade.Buy(0.1);
     }
  }
//+------------------------------------------------------------------+
