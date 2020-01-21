import tensorflow as tf

softmax_data = [0.7, 0.2, 0.1]
one_hot_data = [1.0, 0.0, 0.0]

softmax = tf.placeholder(tf.float32)
one_hot = tf.placeholder(tf.float32)

# TODO: Print cross entropy from session
softmaxlog = tf.log(softmax)
cross_entropy = -tf.reduce_sum(tf.multiply(one_hot, softmaxlog))

with tf.Session() as sess:
	softmaxlogdata = sess.run(softmaxlog, feed_dict={softmax: softmax_data})
	print(sess.run(cross_entropy, feed_dict={softmaxlog: softmaxlogdata, one_hot: one_hot_data}))
