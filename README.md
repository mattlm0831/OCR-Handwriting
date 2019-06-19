# OCR-Handwriting Project
<h3> 1. Summary of Design Decisions </h3>
This project will follow an abstraction based design: letters, words, lines, and entire documents. Every document can be broken down into these respective groups of abstraction.<br/><br/>

<strong>(i)   An entire document.<br/>
(ii)  A collection of lines in a document.<br/>
(iii) A collection of words that are consecutively placed on each line.<br/>
(iv)  Single characters that make up the words.<br/>
</strong><br/>
It can be seen that each level abstraction relies on the previous, going all the way down to the individual letters that are on the document. Given the nature of that abstraction Dr. Johnson suggested we start from the ground up, meaning ﬁrst we will be building the data set for letters, and training a model to recognize other letters of similar (1800’s English) style. Our current priority is to build this large data set of characters for our neural network to pull from. After this set is built up we will work on ﬁguring out the optimal design of our model and start to train it. After this section is completed we will have a network that can identify individual characters. From this base level we will then work on the next level of abstraction, that will be able to identify the words in a line. The project will follow a similar style of abstraction based progress until we can use every level to read an entire document.

<h3> 2. Past Progress </h3>
<img src = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/John_Q._Adams.jpg/220px-John_Q._Adams.jpg' alt= "John Quincy Adams"> </img>

Currently the project is in the data collection phase. We have scans of manuscripts from <strong>John Quincy Adams</strong> that we are imaging. The imaging process will conclude shortly after which we will work on building the networks for the various phases of the model. We anticipate a schedule that proceeds as follows:

<br/>
<strong>
(i) Data collection
<br/>(ii)  Model outline
<br/>(iii) Model optimization<br/>
</strong>


<h3>3. Current Progress </h3>
<img src = 'https://github.com/mattlm0831/OCR-Handwriting/blob/master/bin/src/testing/convnet-smallset-ocr-test2/predictions/This_is_d1.png?raw=true' width = 125 height = 150 alt = 'Example image of a prediction'> This is an example of our current model predicting a letter </img>
