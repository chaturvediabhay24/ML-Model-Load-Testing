import tensorflow as tf
tf.keras.backend.clear_session()
from tensorflow.python.framework import ops
ops.reset_default_graph()
from tensorflow.python.keras.backend import set_session
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import regularizers
import tensorflow.keras.utils as ku
from tensorflow.keras.callbacks import ModelCheckpoint
import numpy as np 
total_words=100
max_sequence_len=11

# global model
sess=tf.Session()
set_session(sess)

# global model
model = Sequential()
model.add(Embedding(total_words, 100, input_length=max_sequence_len-1))
model.add(Bidirectional(LSTM(150, return_sequences = True)))
model.add(Dropout(0.2))
model.add(LSTM(100))
model.add(Dense(total_words/2, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
model.add(Dense(total_words, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())

import os
chk_path='tmp/cp.ckpt'
chk_dir=os.path.dirname(chk_path)

cp_callback=ModelCheckpoint(chk_path, save_weights_only=True,
                                              verbose=1)

model.load_weights(chk_path)

# global graph
graph =  tf.compat.v1.get_default_graph()

def prediction(seed_text,next_words):



	tokenizer = Tokenizer()
	data = open('sonnets.txt').read()

	corpus = data.lower().split("\n")


	tokenizer.fit_on_texts(corpus)
	total_words = len(tokenizer.word_index) + 1


	# create input sequences using list of tokens
	input_sequences = []
	for line in corpus:
	    token_list = tokenizer.texts_to_sequences([line])[0]
	    for i in range(1, len(token_list)):
	        n_gram_sequence = token_list[:i+1]
	        input_sequences.append(n_gram_sequence)


	# pad sequences 
	max_sequence_len = max([len(x) for x in input_sequences])
	input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))


	# create predictors and label
	predictors, label = input_sequences[:,:-1],input_sequences[:,-1]

	label = ku.to_categorical(label, num_classes=total_words)

	#############################################


	# seed_text = "Help me Obi Wan Kenobi, you're my only hope"
	# next_words = 100


	for _ in range(next_words):
		token_list = tokenizer.texts_to_sequences([seed_text])[0]
		token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
# 		global sess
# 		global graph

		with graph.as_default():
			set_session(sess)
			predicted = model.predict_classes(token_list, verbose=0)
		output_word = ""
		for word, index in tokenizer.word_index.items():
			if index == predicted:
				output_word = word
				break
		seed_text += " " + output_word
	return (seed_text)
