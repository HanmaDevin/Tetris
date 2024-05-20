class Color:
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    
    @classmethod
    def getCellColor(self):
        return [self.dark_grey, self.green, self.red, self.orange, self.yellow, self.purple,
                self.cyan, self.blue]