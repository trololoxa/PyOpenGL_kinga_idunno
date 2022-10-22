from OpenGL.GL import GL_QUADS, GL_TRIANGLES, glBegin, glEnd, glUniform2f, glColor4f, GL_TRIANGLE_FAN, \
    GL_LINE_LOOP  # Basic
from OpenGL.GL import glVertex3f, glNormal3f  # 3D
from OpenGL.GL import glVertex2f  # 2D


class Primitive:
    type_list = {'quad': [GL_QUADS, 4], 'triangle': [GL_TRIANGLES, 3], 'tri_fan': [GL_TRIANGLE_FAN, 0],
                 'line_loop': [GL_LINE_LOOP, 0]}

    def __init__(self, data, draw_func=None, type_list_change=None):
        if draw_func is None:
            draw_func = self.basic_draw_func
        if type_list_change is not None:
            self.type_list[type_list_change[0]][1] = type_list_change[1]
        self.draw_func = draw_func
        self.data = data

    def draw(self):
        self.draw_func(data=self.data)

    def basic_draw_func(self, data):
        """
        data structure:
        {
        'obj_type': [GL_QUADS, 4],
        'colors': [[1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1]],
        'normals': [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
        'vertices': [[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]]
        }
        """
        glBegin(data['obj_type'][0])
        for i in range(data['obj_type'][1]):
            glColor4f(data['colors'][i][0], data['colors'][i][1], data['colors'][i][2], data['colors'][i][3])
            glNormal3f(data['normals'][i][0], data['normals'][i][1], data['normals'][i][2])
            glVertex3f(data['vertices'][i][0], data['vertices'][i][1], data['vertices'][i][2])
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

