# StoryVoice - Ronan Quinn D15124865

gcpInstance is the machine learning engine of the StoryVoice project.

gcpInstance contains a model called DeepWriting, based on code, called word-rnn-tensorflow which was written for MIT
and is Copyright (c) 2015 Sherjil Ozair https://github.com/hunkim/word-rnn-tensorflow see included LICENSE.md

DeepWriting is installed to a powerful Google Cloud instance to train on the dataset
The dataset is a cleaned, appended text file of the Facebook "Childrens Book Test" dataset
This dataset is a 1.7GB compendium of classic children's literature, drawn from the open source,
volunteer lead Gutenburg Project https://www.gutenberg.org

The GC instance has TensorFlow and NumPy installed as requirements
A very powerful GC instance is used as training on such a large dataset can take days or weeks on a local machine.

Once trained, the model is moved to another, less powerful, and less expensive, GC instance for story generation

Included in the gcpInstance directory, is a sendstory.sh script for running the sample.py story generation
to make it available for the aiyUI installed code

Not included in the directory is the saved, trained model files. This is due to the huge file size of the TensorFlow
training output. The saved, trained model files, are installed on the project's  live GC instance, at ronanq@story-creator.
The model can be made available for download, on request, from a suitable file sharing platform
