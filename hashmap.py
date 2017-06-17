#!/usr/bin/env python
# coding: utf-8

from __future__ import division


class HashMap():

    def __init__(self, **kwargs):
        # (Extracted from the documentation of CPython dictionary)
        #
        # 8 allows dicts with no more than 5 active entries; experiments
        # suggested this suffices for the majority of dicts (consisting mostly
        # of usually-small dicts created to pass keyword arguments). Making
        # this 8, rather than 4 reduces the number of resizes for most
        # dictionaries, without any significant extra memory use.
        self.size = 8
        self.growth_rate = 2

        self.buckets = [None] * self.size
        self.data = [None] * self.size

        for key, value in kwargs.iteritems():
            self.set(key, value)

    def _handle_collision(self, hashval, key, value):
        # When collision occurs, get the next free slot
        slot = self._next_slot(hashval, key)

        if self.buckets[slot] is None:
            self.buckets[slot] = key
            self.data[slot] = value
        else:
            self.data[slot] = value

    def _resize(self):
        buckets_old = self.buckets[:]
        data_old = self.data[:]

        self.size *= self.growth_rate
        self.buckets = [None] * self.size
        self.data = [None] * self.size

        for key, value in zip(buckets_old, data_old):
            if key:
                self.set(key, value)

    def _hash(self, key):
        if not isinstance(key, str):
            raise Exception("Only string keys can be used.")

        ord_sum = sum(ord(char) for char in key)
        return ord_sum % self.size

    def _rehash(self, hashval):
        return (5 * hashval + 1) % self.size  # Linear Probing

    def _next_slot(self, hashval, key):
        slot = self._rehash(hashval)
        while self.buckets[slot] is not None and self.buckets[slot] != key:
            slot = self._rehash(slot)
        return slot

    def _load_factor(self):
        entries = len(self.keys())
        return entries / self.size

    def set(self, key, value):
        hashval = self._hash(key)

        if self.buckets[hashval] is None:
            self.buckets[hashval] = key
            self.data[hashval] = value

        elif self.buckets[hashval] == key:  # Overwrite value for key
            self.data[hashval] = value

        else:
            self._handle_collision(hashval, key, value)

        # If 2/3rd of table is filled, resize
        if self._load_factor() >= 2/3:
            print "Resizing"
            self._resize()

    def __debug(self):
        print "Size: {}".format(self.size)
        print "Keys: {}".format(self.buckets)
        print "Data: {}".format(self.data)

    def get(self, key):
        if key not in self.buckets:
            raise KeyError

        hashval = self._hash(key)
        existing_key = self.buckets[hashval]
        if existing_key == key:
            return self.data[hashval]

        # Hash collision, check other slots for key
        pos = [index
               for index, keyval in enumerate(self.buckets)
               if keyval == key]
        return self.data[pos[0]]

    def delete(self, key):
        if key not in self.buckets:
            raise KeyError

        self.buckets.remove(key)
        self.data.remove(key)

    def keys(self):
        return list(self.__iter__())

    def items(self):
        return list(self.iteritems())

    def iteritems(self):
        return ((key, val) for key, val in zip(self.buckets, self.data) if key)

    def __iter__(self):
        return (key for key in self.buckets if key)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        return key in self.buckets

    def __str__(self):
        mappings = ["\t'{}': '{}'".format(k, v)
                    for k, v in zip(self.buckets, self.data)
                    if k is not None]
        return """{\n%s\n}""" % ",\n".join(mappings)
