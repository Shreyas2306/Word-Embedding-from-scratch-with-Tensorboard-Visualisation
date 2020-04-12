import warnings
warnings.filterwarnings('ignore')

import gensim
import logging
import argparse

import os



from Web_scrapping import *

logging.basicConfig(format = '%(asctime)s : %(levelname)s : %(message)s ', level = logging.INFO)

class WordEmbedding(WebScraping):

    def __init__(self,path):
        super().__init__(path)
    
    def read_input(self):

        logging.info('reading file {0}...this may take a while'.format(self.path))

        with open(self.path, 'rb') as f:
            for i, line in enumerate(f):
                if (i%10000 == 0):
                    logging.info('read {0} reviews'.format(i))
                
                #perform pre-processing 
                yield gensim.utils.simple_preprocess(line)
    
    
    def model_training(self):

        self.model = gensim.models.Word2Vec(list(self.read_input()), size = 450 , window = 10, min_count = 2, workers = 10)
        self.model.train(list(self.read_input()), total_examples = len(list(self.read_input())), epochs = 10)

        #save model
        model_dir = './model'

        if not os.path.exists(model_dir):
            os.makedirs(model_dir)
        self.model.save(os.path.join(model_dir,'word2vec'))
        
        #if you want to use pre-trained model
        #model = gensim.model.Word2Vec.load(model_dir + '/word2vec')

    
    def results(self):

        w1 = 'profit'
        print(self.model.wv.most_similar(positive = w1))



ap = argparse.ArgumentParser()

ap.add_argument('-d', '--Dataset', help = 'Path to dataset', required = True)

args = vars(ap.parse_args())






wordembedding = WordEmbedding(path = args['Dataset'])
wordembedding.read_input()
wordembedding.model_training()
wordembedding.results()