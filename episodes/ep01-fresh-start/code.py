from alpaca.trading.client import TradingClient

from alpaca.trading.requests import MarketOrderRequest

from alpaca.trading.enums import OrderSide, TimeInForce

  

API_KEY = "THE_KEY"

SECRET_KEY = "THE_SECRET"

  

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

  

order_request = MarketOrderRequest(

symbol="SPY",

qty=1,

side=OrderSide.BUY,

time_in_force=TimeInForce.DAY

)

  

order = trading_client.submit_order(order_request)

print(f"Order submitted! ID: {order.id}, Status: {order.status}")
