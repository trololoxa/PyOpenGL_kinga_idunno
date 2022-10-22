from Engine.Graphics.main import Main


main = Main()

main.scene.add_object(data=[{'vertices': [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]]}])

main.scene.add_object(data={'num_triangles': 200, 'color': [0, 1, 0, 1], 'center': [0, 0], 'radius': 1},
                      obj_type='filled circle')

main.scene.add_object(data={'num_lines': 9, 'color': [1, 0, 0, 1], 'center': [-1, 2], 'radius': 0.5},
                      obj_type='circle')

main.scene.add_object(data={'color': [0, 0, 1, 1], 'center': [-1, -2], 'scale': [0.5, 2]},
                      obj_type='rectangle')

main.run()
