class Parser:
    def __init__(self):
        pass
    
    def stat_text_to_value(self, stat):
        try:
            return float(stat)
        except:
            return str(stat)