import warnings
warnings.filterwarnings('ignore')

from Word_Embedding import *

import re, string, tensorflow
import tensorflow as tf
from tensorflow.contrib.tensorboard.plugins import projector


class TensorboardVisualisation(WordEmbedding):

    def load_model(self):
        self.path = './model'
        #Loading the trained-model
        self.model = gensim.models.Word2Vec.load(self.path + '/word2vec')
        # print('Successfully Model Loaded !!')

    def data_preparation(self):

        
        self.weights = self.model.wv.vectors[:3072]
        self.index_words = self.model.wv.index2word[:3072]

        self.vocab_size = self.weights[:3072].shape[0]
        self.embedding_dim = self.weights[:3072].shape[1]

        # print('Shape of weights: ',self.weights.shape)
        # print('Vocabulary size: %i'%self.vocab_size)
        # print('Embedding size: %i'%self.embedding_dim)
        
    def visualisation(self):
        #saving metadata
        path = './model/Test'

        #Saving metadata file
        with open(os.path.join(path, 'metadata.tsv'), 'w') as f:
            f.writelines('\n'.join(self.index_words))
        #Required if you re-run without restarting the kernel
        tf.reset_default_graph()


        W = tf.Variable(tf.constant(0.0, shape = [self.vocab_size, self.embedding_dim]), trainable = False, name = 'W')
        embedding_placeholder = tf.placeholder(tf.float32, [self.vocab_size, self.embedding_dim])

        embedding_init = W.assign(embedding_placeholder)

        #Using file writer, we can save our summaries and events to our event files
        writer = tf.summary.FileWriter(path, graph = tf.get_default_graph())
        saver = tf.train.Saver()

        #adding into projector
        config = projector.ProjectorConfig()
        embedding = config.embeddings.add()
        embedding.tensor_name = W.name
        embedding.metadata_path = 'metadata.tsv'
        projector.visualize_embeddings(writer,config)

        #Initialising the session
        with tf.Session() as sess:
            sess.run(embedding_init, feed_dict = {embedding_placeholder:self.weights})
            save_path = saver.save(sess, os.path.join(path, 'model.cpkt'))



tensorboardvisualisation = TensorboardVisualisation(path = args['Dataset'])
tensorboardvisualisation.load_model()
tensorboardvisualisation.data_preparation()
tensorboardvisualisation.visualisation()
