from Engine.Graphics.main import Main


main = Main()
main.scene.add_object(data=[{'vertices': [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]],
                             'colors': [[1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1]],
                             'obj_type': 'quad'}])

main.run()
