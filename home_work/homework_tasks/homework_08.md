## Домашнее задание №8

### Задание №1
1) Для ПО ресторана нужно разработать модуль, помогающий контролировать использование фруктов и овощей на кухне.  
2) Создайте абстрактный класс Ingredient с методами get_name() и get_quantity().
3) Создайте два подкласса Vegetable и Fruit, которые наследуют абстрактные методы от Ingredient и реализуют свои собственные версии методов get_name() и get_quantity(). 
   - В методах выводите соответствующие параметры.

### Задание №2 (⭐ задание со звёздочкой)
1. Создайте классовую структуру по описанию
   1. Имеется яблоко со следующими характеристиками:
      -  индекс - принимается при инициализации
      - Стадии созревания (цветение, зеленое, красное) - список хранится в классе, как константа
      - Стадия созревания - создается при инициализации, по умолчанию первое значение из списка стадий
2. Яблоко может:
   - созревать (переходить на следующую стадию созревания)
   - предоставлять информацию о своей зрелости - если яблоко созрело метод возвращает True иначе False

3. Имеется дерево с яблоками:
   - дерево содержит список яблок которые на нем растут - яблоки принимаются при инициализации, как неизвестное кол-во параметров. Сохраняются в список

4. Дерево может:
   - расти вместе с яблоками - т.е. каждое яблоко должно созреть на 1 стадию.
   - предоставлять информацию о зрелости всех яблок - если все яблоки созрели возвращать True иначе False.
   - предоставлять урожай - удалять все яблоки.

5. Имеется садовник, который имеет:
   - имя - принимается при инициализации.
   - растения, за которыми следит - принимаются при инициализации, как неизвестное кол-во параметров. Сохраняются в список

6. Садовник может:
   -  ухаживать за растениями - для этого длякаждого растения нужно вызывать метод роста.
   - собирать урожай - удалять все яблоки - только в том случае если все яблоки созрели. Иначе выдавать предупреждение.

7. Для тестирования:
   - создайте 5 яблок, 1 дерево и 1 садовника
   - используя садовника поухаживайте за деревьями
   - Соберите урожай, когда все яблоки созреют.