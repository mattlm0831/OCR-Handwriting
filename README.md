# OCR-Handwriting Project
<strong> Summary of Design Decisions </strong><br/>
This project will follow an abstraction based design: letters, words, lines, and entire documents. Every document can be broken down into these respective groups of abstraction.<br/>

<strong>(i)   An entire document.<br/>
(ii)  A collection of lines in a document.<br/>
(iii) A collection of words that are consecutively placed on each line.<br/>
(iv)  Single characters that make up the words.<br/>
</strong><br/>
It can be seen that each level abstraction relies on the previous, going all the way down to the individual letters that are on the document. Given the nature of that abstraction Dr. Johnson suggested we start from the ground up, meaning ﬁrst we will be building the data set for letters, and training a model to recognize other letters of similar (1800’s English) style. Our current priority is to build this large data set of characters for our neural network to pull from. After this set is built up we will work on ﬁguring out the optimal design of our model and start to train it. After this section is completed we will have a network that can identify individual characters. From this base level we will then work on the next level of abstraction, that will be able to identify the words in a line. The project will follow a similar style of abstraction based progress until we can use every level to read an entire document.
