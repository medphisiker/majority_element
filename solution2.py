from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Функция ищет элемент массива, который встречается больше половины
        раз в массиве, используя алгоритм Бойера-Мура.

        Если такой элемент существует, - возвращает его.
        Если такого элемента нет, - возвращает -1.

        Временная сложность O(n) - два прохода по массиву.
        Пространственная сложность O(1) - используем только несколько переменных.

        Args:
            array (list[int]): массив целых чисел.

        Returns:
            int: значение элемента, который встречается больше половины
                раз в массиве или -1, если такого элемента нет.
        """
        if not nums:
            return -1

        # поиск самого часто встречающегося элемента
        candidate = None
        count = 0

        for number in nums:
            if count == 0:
                candidate = number
                count = 1
            else:
                if number == candidate:
                    count += 1
                else:
                    count -= 1

        # проверка кандидата, что встречается больше половины
        # раз в массиве
        count = 0
        for number in nums:
            if number == candidate:
                count += 1

        if count > len(nums) / 2:
            return candidate
        else:
            return -1
