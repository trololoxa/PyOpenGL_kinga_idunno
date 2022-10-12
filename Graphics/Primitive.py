from OpenGL.GL import GL_QUADS, GL_TRIANGLES, glBegin, glEnd, glVertex3f, glColor4f, glNormal3f, glUniform2f


class Primitive:
    type_list = {'quad': [GL_QUADS, 4], 'triangle': [GL_TRIANGLES, 3]}

    def __init__(self, data):
        try:
            vertices = data['vertices']
        except KeyError:
            raise Exception('Primitive data dont have vertices data')

        try:
            obj_type = data['obj_type']
            if obj_type not in self.type_list:
                print(f'Primitive data have wrong primitive type name: "{obj_type}" \nTrying to find type vertices')
                if len(vertices) == 4:
                    print('Using type "Quad"')
                    obj_type = 'quad'
                elif len(vertices) == 3:
                    print('Using type "Triangle"')
                    obj_type = 'triangle'
                else:
                    raise Exception('Unknown primitive type')
        except KeyError:
            raise Exception('Primitive data dont have primitive type')

        try:
            colors = data['colors']
        except KeyError:
            print('Primitive data dont have colors data, continuing without colors')
            colors = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        try:
            normals = data['normals']
        except KeyError:
            print('Primitive data dont have normals data, continuing without normals')
            normals = [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]]

        self.data = data
        self.vertices = vertices
        self.colors = colors
        self.normals = normals
        self.obj_type = self.type_list[obj_type]

    def draw(self):
        glBegin(self.obj_type[0])
        for i in range(self.obj_type[1]):
            glColor4f(self.colors[i][0], self.colors[i][1], self.colors[i][2], self.colors[i][3])
            glNormal3f(self.normals[i][0], self.normals[i][1], self.normals[i][2])
            glVertex3f(self.vertices[i][0], self.vertices[i][1], self.vertices[i][2])
        glEnd()

    def update_data(self, update_data, operation_id=1):
        """
        :param update_data: data
        :param operation_id: 1: data = update_data,
        2: data += update_data
        """
        if operation_id == 1:
            self.__init__(update_data)
        elif operation_id == 2:
            for key in update_data:
                if key == 'obj_type':
                    continue
                for i in range(len(update_data[key])):
                    for j in range(len(update_data[key][i])):
                        self.data[key][i][j] += update_data[key][i][j]
                        self.__init__(self.data)

