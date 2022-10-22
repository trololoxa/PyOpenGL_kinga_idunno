from Engine.Objects.basic.Object import Object
from Engine.Objects.TwoD.Circle import FilledCircle, Circle
from Engine.Objects.TwoD.rectangle import Rectangle


class Scene:
    def __init__(self):
        self.objects = []
        self.active_ids = []
        self.all_ids = []
        self.next_id = 0

    def render(self):
        for i in self.active_ids:
            self.objects[i].render()

    def add_object(self, data, obj_type=''):
        if obj_type.lower() == 'filled circle':
            self.objects += [FilledCircle(data=data)]
        elif obj_type.lower() == 'circle':
            self.objects += [Circle(data=data)]
        elif obj_type.lower() == 'rectangle':
            self.objects += [Rectangle(data=data)]
        else:
            self.objects += [Object(data=data)]
        self.all_ids += [self.next_id]
        self.active_ids += [self.next_id]
        self.next_id += 1
