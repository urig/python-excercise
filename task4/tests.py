import unittest
from task4 import task4

class tests(unittest.TestCase):

    def test_ctor(self):
        house = task4.House()

    def test_house_with_no_rooms(self):
        house = task4.House({})

        self.assertEqual(house.calculate_volume(), 0)

    def test_house_with_rectangle_room(self):
        room = task4.RectangleRoom(5, 20, 5)

        house = task4.House({room})

        self.assertEqual(house.calculate_volume(), 500)

    def test_house_with_circle_room(self):
        room = task4.CircleRoom(5.6418959, 5)

        house = task4.House({room})

        self.assertEqual(round(house.calculate_volume()), 500)

    def test_house_with_triangle_room(self):
        room = task4.TriangleRoom(15.196713713, 5)

        house = task4.House({room})

        self.assertEqual(round(house.calculate_volume()), 500)

    def test_house_with_three_different_rooms(self):
        rectangle_room = task4.RectangleRoom(5, 20, 5)
        circle_room = task4.CircleRoom(5.6418959, 5)
        triangle_room = task4.TriangleRoom(15.196713713, 5)

        house = task4.House({rectangle_room, circle_room, triangle_room})

        self.assertEqual(round(house.calculate_volume()), 1500)


if __name__ == '__main__':
    unittest.main()