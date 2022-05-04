from graphviz import Digraph
import random


class Graph:
    def __init__(self):
        self.dict_color = {}
        self.graphics = Digraph('finite_state_machine', filename='NewGraph.gv.pdf')
        self.graphics.attr(rankdir='LR', size='8.5')
        self.graphics.attr('node', shape='doublecircle',style="filled")

    def addNode(self, ip):
        if ip not in self.dict_color:
            self.dict_color[ip] = self.__rand_color()
        self.graphics.node(ip, fillcolor=self.dict_color[ip])

    def addConn(self, src, dst, info):
        self.graphics.edge(src, dst, label=info, color=self.dict_color[src], style="dashed")

    def __rand_color(self):
        r = lambda: random.randint(0, 255)
        str = '#%02X%02X%02X' % (r(), r(), r())
        return str

    def graphView(self):
        self.graphics.view()
        print(self.graphics.source)


if __name__ == '__main__':
    list_ip = ["172.31.255.255", "192.168.1.5", "192.98.78.5", "26.99.578.5", "12.31.255.255"]
    graph = Graph()
    for el in list_ip:
        graph.addNode(el)
    graph.addConn("172.31.255.255", "192.168.1.5", "qwe")
    graph.addConn("172.31.255.255", "192.98.78.5", "asd")
    graph.addConn("12.31.255.255", "192.98.78.5", "zxc")
    graph.addConn("192.98.78.5", "26.99.578.5", "zxc")
    graph.addConn("26.99.578.5", "192.98.78.5", "zxcd")
    graph.addConn("12.31.255.255", "26.99.578.5", "hfk")
    graph.graphView()


