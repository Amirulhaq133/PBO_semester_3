import turtle


class Myturtle:
    def __init__(self, color, shape):
        self.t = turtle.Turtle()
        self.t.color(color)
        self.t.shape(shape)
    
    def maju(self, gerak):
        self.t.forward(gerak)

    def putar_kanan(self,belok):
        self.t.right(belok)

    def membuat_Segitiga(self, ukuran):
        for _ in range(3):
            self.maju(ukuran)
            self.putar_kanan(120)

    def selesai(self):
        turtle.done()

turtle1 = Myturtle("black","turtle")
turtle1.membuat_Segitiga(150)
turtle1.selesai()


    
    
