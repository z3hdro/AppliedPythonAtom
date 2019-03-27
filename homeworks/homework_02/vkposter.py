#!/usr/bin/env python
# coding: utf-8


from collections import defaultdict, Counter

from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.users_posts = defaultdict(list)
        self.posts_reads = Counter()
        self.user_reads = defaultdict(set)
        self.followers = defaultdict(set)

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        # посты добавляются подряд, нельзя добавить свежий пост раньше старого
        self.users_posts[user_id].append(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        # тут считаем только уникальные прочтения, реализовано через set - это быстрее
        if post_id not in self.user_reads[user_id]:
            self.posts_reads[post_id] += 1
            self.user_reads[user_id].add(post_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        # сделано через сет
        self.followers[follower_user_id].add(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int)-> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        # формируем список списков (он будет сортированным из-за того как добавляли) и мерджим
        all_recent_posts = [self.users_posts[i][-k:] for i in self.followers[user_id]]
        return FastSortedListMerger.merge_first_k(all_recent_posts, k)

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        # можно написать оптимальнее - завести кучу размера k, и добавлять в нее, когда элементов в куче будет больше k
        # удалять последний элемент и продолжать добавлять.
        # таким образом пройдя все посты мы сохраним k самых свежих и популярных.
        # затем отсортируем только k постов и вернем их.
        # а можно вот так влоб решить:
        # return [i[0] for i in sorted(self.posts_reads.most_common(), key=lambda x: (x[1], x[0]), reverse=True)[:k]]
        # либо просто все в кучу засунуть:
        res = []
        h = MaxHeap([])  # если kых элементов несколько нужно взять самый свежий.
        for i in self.posts_reads:
            h.add((self.posts_reads[i], i))
        while (len(res) < k and len(h.array) > 0):
            res.append(h.extract_maximum()[1])
        return res
