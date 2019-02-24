#### Reuters
Change directory to Reuters for experimenting on Reuters-21578 dataset. As reuters data is in SGML format, parsing data and creating pickle file of parsed data can be done as follows:

```sh
$ python create_data.py
# We don't save train and test files locally. We split data into train and test whenever needed.
```

Get word vectors for all words in vocabulary: 

```sh
$ python Word2Vec.py 200
# Word2Vec.py takes word vector dimension as an argument. We took it as 200.
```

Get Sparse Document Vectors (SCDV) for documents in train and test set:

```sh
$ python SCDV.py 200 60
# SCDV.py takes word vector dimension and number of clusters as arguments. We took word vector dimension as 200 and number of clusters as 60.
```

Get performance metrics on test set:

```sh
$ python metrics.py 200 60
# metrics.py takes word vector dimension and number of clusters as arguments. We took word vector dimension as 200 and number of clusters as 60.
```
