# ealc301-proj
Calculating similarities for ~200 translations of the daodejing

Derick Olson

18 December 2015

H.W. Cheng

**Translating the ****_Laozi_****: Can Textual Analysis Indicate Translation Authority?**

This study analyzes over 180 English translations

 of the Daodejing by focusing on parallel translations 

of the first chapter of the text, along with contextual information

such as translator. Given this information, as well as a set of

reputable translators, it ranks all translations in terms of quality

as defined by the texts of the selected reputable translators.

I chose the Daodejing is an ideal source text for textual analysi because of the widespread availability of its English translations, as well as its short length. The goal of this research is to use well-established translations of a section of the Daodejing in order to train a computational model with which we can evaluate the quality of unknown status translations. We do this by representing each translation as a vector of scores, creating one "master vector" which is an ensemble of well-respected translations, and determining the similarity of each unknown translation vector with this master translation vector.

**Background**

The Daodejing has been called the most translated text besides the Bible, and currently has over 250 translations in Western languages (NOTE:  Goldin 119). Its text is an "anthology of earlier sayings and teachings", from the oral tradition of “Laoist” schools around 300 B.C., as well as additions made by teachers who “composed” and arranged the sayings into chapters (NOTE:  LaFargue 340). The standard traditional Chinese text of the Daodejing is translated from the Wang Pi commentary, although some more recent translations are based on the Ma-wang-tui manuscripts.

The proliferation of the Daodejing has had profound influences in both the east and west. In ancient China, it represented an opposition to the presiding Confucian cultural system. Over the centuries, Daoist commentaries and cults emerged with roots tracing back to the original text. In the West, the Daodejing is popular both among academics as a rich historical document and to the layperson for its lessons. For our purposes, we consider the Daodejing because of the multitude of unique translations into English. 

The more popular of its translations are not without criticism. In his essay "Those Who Don’t Know Speak: Translations of *Laozi* by People Who Do Not Know Chinese," Paul Goldin criticizes four translations of the Daodejing by Americans who do not speak Chinese, but rather rephrased and English version into their own verse. It may seem overly harsh to criticize translations that were marketed to be popular among non-scholars, but Goldin makes the valid point that such translations cheapen the standard of a classic and difficult text by appropriating the palatable parts, while ignoring the rest. In this sense, it sets a double standard for Western classics whose meanings are generally preserved in translation. The translations referred to, by Witter Bynner, Stephan Mitchell, Thomas Miles, and Ursula Le Guin, are addressed in the results section below.

Assuming that we are seeking accuracy in translation, what are the primary factors that we should consider? As noted above, we already have the problem of multiple source texts, many of which have been criticized as having been corrupted during transmission. We briefly follow the survey of translation problems as presented by Michael LaFargue and Julian Pas.

To start, we can examine the difficulties regarding accuracy of translation. First, we have the problem of ambiguous meaning in ancient Chinese. For example, the word *shih* has meanings from "energy", “circumstances”, to “middle course” and “what is within” (NOTE:  LaFargue 280-1). Second, ancient Chinese writing was generally written by scribes, who would not always record the same character for different homophones in a lyric context such as the Daodejing. Finally, ancient Chinese is uninflected, so there are ambiguities in syntax. With these issues, there are several tradeoffs that translators should consider when translating a text.

There are three areas to balance in translation: (1) word-for-word versus clarified for meaning, (2) maintaining historical context versus allowing reader to apply the text to contemporary life, and (3) conveying the ideas of the original text versus conveying the style and feeling of original text (NOTE:  LaFargue 285). 

In the first, we have word-for-word accuracy versus clarity and meaning. A fully-literal translation would still have to deal with single-word ambiguity, but it would not change the word order of the sources document. Clearly, some clarification is likely to be necessary for a successful translation, and we consider successful translations to be those that balance the two well.

Second, we have the balance of historical context versus contemporary applications. This is more of a split between academic and popular culture. For academics, historical context will likely always win out over direct applications to modern life. Conversely, popular translations are meant to be read with a focus on entertainment or spiritual growth, rather than as an historical exercise. In this paper, we value historical accuracy above contemporary applications, as we are seeking the most scholarly authoritative texts.

Finally, we have the two sides of conveying ideas versus style and feeling. This can be difficult, particularly in a text like the Daodejing, because of its focus on non-action and minimal thinking. Moreover, the tone of the text is often called "playful," which is an indicator that a great deal of the meaning of the text comes from its style. These sides are not necessarily mutually exclusive, and it is largely the work and accomplishment of the translator to successfully recreate both the ideas, style, and mood of a text in another language. 

With these problems of translation in mind, we move on to the experiment design and analysis in order to take an alternative approach to translation evaluation.

 **Methodology**

In "On Translating the Tao-te-ching", LaFargue and Livia Kohn closely examine passages from 17 popular translations, eight from 1930s-1960s, and nine from 1970s-1990s. These translations and the translators’ opinions of them form the basis of my definition of “good” texts, against which the other 150+ unknown translations will be evaluated.

Our source corpora is 180 translations of the first chapter of the Daodejing (NOTE:  Translations found at http://www.bopsecrets.org/gateway/passages/tao-te-ching.htm).  We call each of these translations a document. The average document length is just under 100 words long. Because our documents are short, and translating one of just a few source texts, the total number of unique words is likely to be manageably small. For this reason, we can use word frequency to measure similarity between documents.

Given this information, we are ready to implement a document scorer, where a document’s score represents the similarity between the document and some baseline document. We are free to define this baseline document however we please. For our purposes, I chose those texts classified by LaFargue as reputable (see appendix for translators chosen). Rather than select a single document as the base, I chose 15, so that our reputability baseline is made of a range of well known and well respected translators. Thus, our score represents the reputability of the remaining documents.

There are two main stages to this implementation: (1) Parsing, (2) Scoring

In the first part, I began by cleaning the HTML document of the source text, and splitting up each section into a grouping of [TRANSLATOR, DATE, TEXT] where the TEXT section has punctuation removed. The next step is to *stem* (NOTE:  http://www.nltk.org/howto/stem.html) each term, that is, to remove any affixes, so that we can map multiple forms of the same word to the same word-stem.

With parsing and stemming complete, the next step was to build word vectors to represent each document. First, we read every stemmed word from every document in order to get the word frequencies across the entire corpora. 

Now, we have a vector of the form:

*v = [0, 0, 1, … 1, 0, 0]*

Where a ‘0’ represents the absence of a word, whereas a ‘1’ represents the presence of one, where the vector has a slot for every single word in the corpora. Each document can now be represented as a sparse vector.

The next step is to squash the selected authoritative translators into one "master vector", who gets the ‘1’s of each of the authoritative translators. Given this master vector, we can calculate the *cosine similarity* (NOTE:  https://en.wikipedia.org/wiki/Cosine_similarity) of each document vector with the master vector, in order to get a number between [0, 1], where 0.0 indicates zero similarity, and 1.0 indicates the same document as the master. The selected “authoritative translators” are below.

![image alt text](image_0.png)

*Translators selected to create master vector*

**Analysis**

Of the top candidates that were not on the authority list, we have the following seven: Tormond Byrn (uncertain), Bram den Hond (uncertain), Tolbert McCarroll (uncertain), Livia Kohn (Sinologist), John R. Leebrick (uncertain), Derke Bodde(sinologist), and Bao Pu (editor in Hong Kong). Three of these results are reputable sinologists, whereas four are not. This indicates that the current model may have a problem with false positives.

However, if we run through the bottom candidates, none of them appear to be reputable sources, so we do not have false negatives with this model. More scores, as well as additional similarity analysis such as multi-word phrases, and academic terminologies, would likely improve on this classifier.

To summarize, it appears that the classifier is effective in classifying both positive and negative matches, although it gives false positives. To further refine what we mean by a match, the initial intention of translation authority continues to hold, where the test for proper classification is some China-related academic experience or else a native Chinese-speaker with the means to directly translate the text.

![image alt text](image_1.png)![image alt text](image_2.png)

*Top 22 and Bottom 20 Performers. ***_Bold_*** indicates an input "authority"*

Other notable translations include the four criticized by Goldin, below. Although Thomas Miles ranked in the top 50, the other three are in the lower 30% of all translations. Again, it appears that Miles may have been a bit of a false positive in the overall ranking.

![image alt text](image_3.png)

*Translators noted for not speaking Chinese*

**Conclusion**

A further step in this study would be to gather further information on each translator in order to better classify the document. Every entry from the source page includes an translator and date, so one could look up further context for each translator. Furthermore, a more sophisticated classification algorithm could help us further split our translators into more categories, such as those dichotomies put forth by LaFargue (literal vs clear, historicized vs contemporary, idea vs style/mood).

Additionally, comparisons based on word pairs (bigrams), or larger groupings (ngrams) rather than only single words could improve our overall grouping.

There is much more work to be done.  I hope that this served as an example of the potential for programmatic textual analysis to address the problems of evaluating translation decisions, and for addressing other questions in humanities research.

**Bibliography**

Paul Goldin. *After Confucius - Studies in Early Chinese Philosophy*. Honolulu: University of Hawai’i Press. 2005.

Livia Kohn and Michael LaFargue. *Lao-tzu and the Tao-te-ching*. New York: State University of New York Press. 1998.

Michael LaFargue. *Tao and Method: A Reasoned Approach to the Tao Te Ching*. New York: State University of New York Press. 1994.

Tao Hyum Kim. "Other Laozi Parallels in the Hanfeizi". *Sino-Platonic Papers*, 199. 2010.

182 Translations of Chapter One of Daodejing. Bopsecrets. Accessed: 18 December 2015. Source: http://www.bopsecrets.org/gateway/passages/tao-te-ching.htm
