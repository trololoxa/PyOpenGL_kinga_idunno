from Engine.Objects.basic.Primitive import Primitive


class Object:
    def __init__(self, data, draw_func=None, type_list_change=None, process_data=True):
        if process_data:
            data = self.process_data(data)
        self.primitives = []
        if type(data) == list:
            for primitive in data:
                self.primitives += [Primitive(data=primitive, draw_func=draw_func, type_list_change=type_list_change)]
        elif type(data) == dict:
            self.primitives += [Primitive(data=data, draw_func=draw_func, type_list_change=type_list_change)]
        self.collider = None
        self.active_collider = False

    def process_data(self, data):
        new_data = []
        for sdata in data:
            try:
                vertices = sdata['vertices']
            except KeyError:
                raise Exception('Primitive data dont have vertices data')

            try:
                obj_type = sdata['obj_type']
                print(obj_type)
                if obj_type not in Primitive.type_list:
                    print(f'Primitive data have wrong primitive type name: "{obj_type}" \n'
                          f'Trying to find type using vertices')
                    if len(vertices) == 4:
                        print('Using type "Quad"')
                        obj_type = 'quad'
                    elif len(vertices) == 3:
                        print('Using type "Triangle"')
                        obj_type = 'triangle'
                    else:
                        raise Exception('Unknown primitive type')
            except KeyError:
                print(f'Primitive data dont have primitive type \nTrying to find type using vertices')
                if len(vertices) == 4:
                    print('Using type "Quad"')
                    obj_type = 'quad'
                elif len(vertices) == 3:
                    print('Using type "Triangle"')
                    obj_type = 'triangle'
                else:
                    raise Exception('Primitive data dont have primitive type')

            try:
                colors = sdata['colors']
            except KeyError:
                print('Primitive data dont have colors data, continuing without colors')
                colors = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]

            try:
                normals = sdata['normals']
            except KeyError:
                print('Primitive data dont have normals data, continuing without normals')
                normals = [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]]

            vertices = vertices
            colors = colors
            normals = normals
            obj_type = Primitive.type_list[obj_type]
            new_sdata = {'obj_type': obj_type,
                         'colors': colors,
                         'normals': normals,
                         'vertices': vertices}

            new_data += [new_sdata]
        return new_data

    def render(self):
        for prim in self.primitives:
            prim.draw()

    def deactivate_collider(self):
        self.active_collider = False

    def activate_collider(self):
        self.active_collider = True
