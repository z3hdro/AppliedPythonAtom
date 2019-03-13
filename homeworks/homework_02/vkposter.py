#!/usr/bin/env python
# coding: utf-8


from heap import MaxHeap
from fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.followers = {}
        self.posted_posts = {}
        self.user_posts = {}

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id not in self.posted_posts:
            self.posted_posts[post_id] = [user_id, []]
        if user_id not in self.user_posts.keys():
            self.user_posts[user_id] = [post_id]
        else:
            if post_id not in self.user_posts.get(user_id):
                self.user_posts.get(user_id).append(post_id)

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id in self.posted_posts:
            if user_id not in self.posted_posts[post_id][1]:
                self.posted_posts[post_id][1].append(user_id)
        if post_id not in self.posted_posts:
            self.posted_posts[post_id] = ["", [user_id]]

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id not in self.followers:
            self.followers[follower_user_id] = [followee_user_id]
        if follower_user_id in self.followers:
            self.followers[follower_user_id].append(followee_user_id)

    def get_recent_posts(self, user_id: int, k: int)-> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        heap_sort = True
        if heap_sort:
            arr = [self.user_posts.get(i) for i in self.followers.get(user_id)
                   if i in self.user_posts.keys()]
            return FastSortedListMerger.merge_first_k(arr, k)
        else:
            recent_posts = []
            for key, value in self.posted_posts.items():
                if value[0] in self.followers[user_id]:
                    recent_posts.append(key)
            recent_posts.sort()
            recent_posts.reverse()
            return recent_posts[:k]

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        heap_sort = True
        if heap_sort:
            arr = [(len(self.posted_posts.get(i)[1]), i)
                   for i in [self.posted_posts.keys()]]
            heap = MaxHeap(arr)
            return [heap.extract_maximum()[1] for i in range(k)]
        else:
            sorted_posts = list(self.posted_posts.keys())
            sorted_posts.sort(key=lambda i: (len(self.posted_posts.get(i)[1]),
                                             i), reverse=True)
            return sorted_posts[:k]
