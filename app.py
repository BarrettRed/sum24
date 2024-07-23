import csv
import io
import json
from itertools import combinations


def is_unique_subset(entities, attributes):
    """
    Проверяет, уникален ли набор признаков для каждой сущности.

    Аргументы:
    entities -- список сущностей (словарей).
    attributes -- список признаков (ключей), которые нужно проверить.

    Возвращает:
    True, если набор признаков уникален для каждой сущности, иначе False.
    """
    seen = set()
    for entity in entities:
        identifier = tuple(entity.get(attr, "") for attr in attributes)
        if identifier in seen:
            return False
        seen.add(identifier)
    return True


def find_minimal_unique_subset(entities, attributes):
    """
    Ищет минимальный набор признаков, который уникально идентифицирует
    каждую сущность. Поиск осуществляется на основе перебора всех возможных
    сочетаний признаков до первого набора, удовлетворяющего
    заданным условиям.

    Аргументы:
    entities -- список сущностей (словарей).
    attributes -- словарь с признаками и количеством уникальных
    значений для каждого признака.

    Возвращает:
    Список признаков, который минимально и уникально идентифицирует
    каждую сущность.
    """
    total_entities = len(entities)
    attribute_list = list(attributes)

    for n in range(1, len(attribute_list) + 1):
        for subset in combinations(attribute_list, n):
            # Проверка произведения уникальных значений
            possible_unique_values = 1
            for attr in subset:
                possible_unique_values *= attributes[attr]
            """
            Если максимально возможное количество комбинаций
            уникальных значений всех признаков в подмножестве
            меньше, чем общее количество сущностей, то текущий
            набор признаков не может уникально идентифицировать
            все сущности.
            """
            if possible_unique_values < total_entities:
                break

            if is_unique_subset(entities, subset):
                return subset

    return []


def list_to_csv_string(ls):
    """
    Преобразует список в CSV-строку с одной колонкой.

    Аргументы:
    ls -- список значений.

    Возвращает:
    CSV-строку с одним столбцом, содержащим значения из списка.
    """
    output = io.StringIO()
    writer = csv.writer(output)
    for attr in ls:
        writer.writerow([attr])
    return output.getvalue()


def main(json_string):
    """
    Основная функция для поиска минимального набора признаков, уникально
    идентифицирующих каждую сущность, и преобразования результата в CSV-строку.

    Аргументы:
    json_string -- строка в формате JSON с исходными данными.

    Возвращает:
    CSV-строку с минимальным уникальным набором признаков.
    """
    entities = json.loads(json_string)

    # Получение списка всех признаков и подсчет уникальных значений
    attributes = {}
    for entity in entities:
        for key, value in entity.items():
            if key not in attributes:
                attributes[key] = set()
            attributes[key].add(value)
    attributes = {key: len(values) for key, values in attributes.items()}

    """
    Сортировка признаков по количеству уникальных значений по убыванию.
    Это позволит нам сначала рассматривать ключи, которые имеют большее
    количество уникальных значений, что увеличивает шансы на быстрое нахождение
    уникального подмножества.
    """
    attributes = dict(
        sorted(
            attributes.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )

    # Поиск минимального уникального набора признаков
    minimal_unique_subset = find_minimal_unique_subset(
                                entities, attributes)

    return list_to_csv_string(minimal_unique_subset)


if __name__ == "__main__":
    with open('file.json', 'r', encoding='utf-8') as file:
        json_string = file.read()

    result_csv = main(json_string)
    print(result_csv)
