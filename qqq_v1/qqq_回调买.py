class Strategy(StrategyBase):

    def initialize(self): # 初始化
        declare_strategy_type(AlgoStrategyType.SECURITY)
        self.trigger_symbols()
        self.custom_indicator()
        self.global_variables()

    def trigger_symbols(self):  # 定义驱动标的
        self.驱动标的1 = declare_trig_symbol()

    def global_variables(self):  # 定义全局变量
        self.recent_low = show_variable(0.0, GlobalType.FLOAT)
        self.recent_high = show_variable(0.0, GlobalType.FLOAT)
        self.出售数量 = show_variable(0, GlobalType.INT)

    def custom_indicator(self):  # 
        pass

    def handle_data(self):  # K线推送、Tick推送、固定时间间隔、指定时刻，这4种事件会触发handle_data()函数
        self.action_7336516098799848496_invoke()  # 执行路径1

    def action_7336516098799848496(self):
        crt_price =  current_price(symbol=self.驱动标的1, price_type=THType.FTH)
        
        if self.recent_high <= 0:
            self.recent_high = crt_price
        
        if self.recent_low <= 0:
            self.recent_low = crt_price
        
        print("low_price:", self.recent_low)
        print("high price:", self.recent_high)
        # 如果回调了2%，就买入
        
        if self.recent_high > 0 and self.recent_high > crt_price * 1.03:
                place_limit(symbol=self.驱动标的1, price=crt_price, qty=1000, side=OrderSide.BUY, time_in_force=TimeInForce.GTC)
                self.recent_high = crt_price
            
        
        
        
        self.出售数量 = max_qty_to_sell(symbol=self.驱动标的1) * 0.07
        
        #如果上涨3%，就卖
        if self.recent_low > 0 and self.recent_low < crt_price * 0.96:    
            place_limit(symbol=self.驱动标的1, price=crt_price * 0.97,qty=self.出售数量 , side=OrderSide.SELL, time_in_force=TimeInForce.GTC) 
            self.recent_low = crt_price
            
        
        
        if crt_price < self.recent_low:
            self.recent_low = crt_price
            
        if crt_price > self.recent_high:
            self.recent_high = crt_price
            
            
        print("low_price:", self.recent_low)
        print("high price:", self.recent_high)

    def action_7336516098799848496_invoke(self):  # 自编码动作
        self.action_7336516098799848496()