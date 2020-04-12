# Word-Embedding-from-scratch

## About Word Embedding
  
With a humongous amount of data present in text format it becomes difficult to extract information out of it and build application. Understanding how different words are related based on the context they are used is an easy task for us humans. Consider the sentence that 'Apple is a winter fruit', here we are able to differentiate that `Apple` is considered as a fruit rather than the company Apple. At the same time we can suggest other winter fruits like cherry or plums and speak about where they are grown and how much they would cost. Similarly computer also needs a way where they can learn about a topic and where they can understand how different words are related. Word embedding provides a method to work with such textual data.

![alt text](https://res.cloudinary.com/springboard-images/image/upload/q_auto,f_auto,fl_lossy/wordpress/2017/08/wmd-Copy.png)
  
## Objective
  
In this repository I'll be showing you a simple
implementation of `Word Embedding` on your own data
collected using `web scraping` from scratch using **Gensim**'s `word2vec` model.
  

## Dependencies
- Gensim
- Tensorflow
- NLTK
- Python
- Pickle
- Scrapy
- Tensorboard

## Installation
Clone or download the file and run `Word_Embedding.py` file.

**Example** :

`python Word_Embedding.py -d 'Path to dataset'`

![alt text](https://github.com/Shreyas2306/Word-Embedding-from-scratch-with-Tensorboard-Visualisation/blob/master/Screenshot.png)

### Output:
 Words similar to `Profit`.
 
 `model.wv.most_similar (positive= 'Profit')`

![alt text](https://github.com/Shreyas2306/Word-Embedding-from-scratch-with-Tensorboard-Visualisation/blob/master/Output_screenshot.png)


## Note:
To train with your own data, you need to change the URLs in the `Web_scraping.py` and run the`Word_Embedding.py` file.

## Tensorboard Visualisation

With tensorboard we can not only visualize complex neural network graphs but also our Word Embeddings. There's a representation of my word embedding using tensorboard.

![alt text](https://github.com/Shreyas2306/Word-Embedding-from-scratch-with-Tensorboard-Visualisation/blob/master/TensorboardVisualisation.gif)

### How to run `Tensorboard Visualisation` ?

- Run `Tensorboard_visualisation.py` 

  **Example** : `python Tensorboard_visualisation.py -d 'path to dataset'`
  After this type:
    - If you are running on Terminal
    
      `tensorboard --logdir path`
      
      **Note** : Please provide the complete path to `model checkpoint and metadata`.
    - If you are running on Notebook
    
      `!tensorboard --logdir path`
  

