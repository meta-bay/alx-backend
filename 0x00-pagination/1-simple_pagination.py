#!/usr/bin/env python3
'''
1-simple_pagination
'''
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page_size) is int and type(page) is int
        assert page > 0
        assert page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        self.dataset()
        if start_idx >= len(self.__dataset):
            return []
        else:
            return self.__dataset[start_idx:end_idx]


def index_range(page: int, page_size: int) -> tuple:
    '''returns a tuple of size two containing
      a start index and an end index'''
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)
