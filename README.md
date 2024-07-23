# Минимальный Уникальный Набор Признаков

Данная программа реализует алгоритм для поиска минимального уникального набора признаков, который может идентифицировать каждую сущность в наборе данных. Программа читает данные в формате JSON, находит минимальный уникальный набор признаков и возвращает его в виде CSV-строки.

## Алгоритм

1. **Чтение данных:**
   - Программа читает данные в формате JSON, содержащие список сущностей. Каждая сущность представлена в виде словаря с различными признаками.

2. **Подсчет уникальных значений признаков:**
   - Для каждого признака подсчитывается количество уникальных значений.

3. **Сортировка признаков:**
   - Признаки сортируются по количеству уникальных значений в порядке убывания. Это позволит нам сначала рассматривать ключи, которые имеют большее количество уникальных значений, что увеличивает шансы на быстрое нахождение уникального подмножества.

4. **Поиск минимального уникального набора признаков:**
   - Программа перебирает все возможные комбинации признаков, начиная с наименьших, и проверяет, является ли комбинация возможной: если максимально возможное количество комбинаций уникальных значений всех признаков в подмножестве меньше, чем общее количество сущностей, то текущий набор признаков не может уникально идентифицировать все сущности. Например, если всего сущностей 100, а на данный момент выбраны для проверки два признака с количеством уникальных значений 40 и 2, то всего из этих значений можно составить 80 комбинаций, что меньше 100, а значит не может данный набор признаков однозначно идентифицировать сущность. Если эта проверка пройдена, то далее идет проверка набора непосредственно через сам список. Проходя по списку, мы смотрим, не встречалась ли нам ранее текущая комбинация значений. Если встречалась, то данный набор признаков не подходит, иначе мы его сохраняем и передаем на следующий этап.

5. **Преобразование результата в CSV-строку:**
   - Найденный минимальный уникальный набор признаков преобразуется в CSV-строку с одной колонкой.

## Блок-схемы

![[media/main.png]]
![[media/find_minimal_unique_subset.png]]
![[meida/is_unique_subset.png]]
![[media/list_to_csv_string.png]]
