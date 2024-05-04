import pyqtgraph as pg

class Graph:
    def __init__(self) -> None:
        
        self.y_axis = []
        self.y_axis_title = 'y label not added'
        
        self.x_axis = []
        self.x_axis_title = 'x label not added'
        
        self.graph_title = 'title not added'
        
        self.graph = pg.PlotWidget()
        
        
    
if __name__ == '__main__':
    test = pg.QtGui.QApplication([])
    test_widget = pg.plot()
    