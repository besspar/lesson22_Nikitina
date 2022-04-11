# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def mvmntobjbfld(self, field, x_axis, y_axis, direction, is_fly, is_crawl, speed = 1):
        """Функция реализует перемещение юнита по полю.
        """
        if is_fly and is_crawl:
            # выбросим ошибку
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
            if direction == 'UP':
                new_y = y_axis + speed
                new_x = x_axis
            elif direction == 'DOWN':
                new_y = y_axis - speed
                new_x = x_axis
            elif direction == 'LEFT':
                new_y = y_axis
                new_x = x_axis - speed
            elif direction == 'RIGHT':
                new_y = y_axis
                new_x = x_axis + speed
        if is_crawl:
            speed *= 0.5
            if direction == 'UP':
                new_y = y_axis + speed
                new_x = x_axis
            elif direction == 'DOWN':
                new_y = y_axis - speed
                new_x = x_axis
            elif direction == 'LEFT':
                new_y = y_axis
                new_x = x_axis - speed
            elif direction == 'RIGHT':
                new_y = y_axis
                new_x = x_axis + speed

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
