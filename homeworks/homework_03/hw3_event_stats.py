#!/usr/bin/env python
# coding: utf-8


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        self.users = {}

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        # TODO: реализовать метод
        if user_id in self.users.keys():
            self.users.get(user_id).append(time)
        else:
            self.users[user_id] = [time]

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        # TODO: реализовать метод
        result = []
        for key, value in self.users.items():
            k = 0
            for time_user in value:
                if time - self.FIVE_MIN < time_user <= time:
                    k += 1
            if count == 0 and k == 0:
                continue
            if k == count:
                result.append(key)
            else:
                continue
        return len(result)
