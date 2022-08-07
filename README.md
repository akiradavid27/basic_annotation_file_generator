# basic_annotation_file_generator
A basic Python script to create either a TXT annotation file used to generate a TFRecords dataset, or a CSV file to use it directly as a Filename/label dataset's annotation file.
# How to use
There are four arguments you can add from the command line interface.
-n: name of the file that will be generated
-p: path to the images folder
-t: specify what type of format the file generated will have (TXT or CSV)
-i: choose whether or not to add the images path (setted in False per default)

Given an image dataset located in a folder of your computer, the script can generate four different types of annotation files.
1. CSV annotation file without specifying the images path
2. CSV annotation file specifying the images path
3. TXT annotation file without specifying the images path
4. TXT annotation file specifying the images path

# Where to use
You can use this script to create a TXT annotation file needed when generating a TFRecords dataset, format mainly found in datasets used to train Deep Learning models. A great example is [emedvedev/attention-ocr](github.com/emedvedev/attention-ocr) repository.

You can also use this script to create a dataset's annotation file in CSV format. The CSV file has the format of (filename,label). This type of file is also used when training Deep Learning models. An example using this type of annotation file is [rsommerfeld/trocr](github.com/rsommerfeld/trocr) repository.
