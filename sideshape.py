class shape:
      def no_of_sides(self):
          print("this shape has many sides")
class Square(shape):
      def no_of_sides(self):
          print("A square has 6 sides")

s1 =shape()
s2 =Square()

s1.no_of_sides()
s2.no_of_sides()
