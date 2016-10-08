#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from gensim.corpora import Dictionary
from gensim.corpora import MmCorpus
from preprocessing import TxtCorpus
import os
from gensim import corpora, models, similarities

__author__ = 'zhiyue'
__copyright__ = "Copyright 2016"
__credits__ = ["zhiyue"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "zhiyue"
__email__ = "cszhiyue@gmail.com"
__status__ = "Production"


class TxtSimilar(object):
    def __init__(self, save_path, index_path='index/netbook', num_best=20):
        self.corpus, self.dictionary, self.labels, self.tfidf = TxtSimilar._load(save_path)
        if len(os.listdir(index_path)) > 0:
            self.similarities_index = TxtSimilar.load_index(index_path)
        else:
            self.similarities_index = self.build_index(index_path, self.corpus, len(self.dictionary), num_best)

    def build_index(self, index_path, corpus, num_features, num_best):
        corpus_tfidf = self.tfidf[corpus]
        similarities_index = similarities.Similarity(index_path, corpus_tfidf,
                                                     num_features=num_features,
                                                     num_best=num_best)
        return similarities_index

    @staticmethod
    def load_index(path):
        return similarities.Similarity.load(path)

    def query(self, doc):
        pass

    def save_module(self, path):
        self.tfidf.save(path)

    @staticmethod
    def load_tfidf_module(path):
        return models.TfidfModel.load(path)

    @staticmethod
    def _load(save_path):
        dict_path = os.path.join(save_path, 'corpus.dict')
        mm_path = os.path.join(save_path, 'corpus.mm')
        labels_path = os.path.join(save_path, 'corpus.labels')
        tfidf_module = os.path.join(save_path, 'corpus.tfidf')
        corpus = MmCorpus(mm_path)
        dictionary = Dictionary.load(dict_path)
        labels = TxtCorpus.load_labels(labels_path)
        if os.path.isfile(tfidf_module):
            return corpus, dictionary, labels, TxtSimilar.load_tfidf_module(tfidf_module)
        else:
            return corpus, dictionary, labels, models.TfidfModel(dictionary=dictionary)
