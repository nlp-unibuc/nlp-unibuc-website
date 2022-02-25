Title: Resources

- <a href="#HistoricalLinguistics">Resources and Tools for Computational Historical Linguistics</a> 
- <a href="#NeuralTS">Neural Text Simplification Models</a> 
- <a href="#ENNTT">Europarl Corpus of Native, Non-native and Translated Texts - ENNTT</a> 
- <a href="#Wittgenstein">A Visual Representation of Wittgenstein's Tractatus Logico-Philosophicus</a> 
- <a href="#RoDet">Romanian Determiners Lexicon - RoDetLexicon 1.1</a>  
- <a href="#SpeechText">Comparing Speech and Text Classification of Native and Non-native English</a>
- <a href="#LangSim">Degrees of Similarity Between Romanian and Related Languages</a>
- <a href="#NER">Cross-lingual Named Entity Recognition</a> 
- <a href="#pejor">A Computational Exploration of Pejorative Language in Social Media</a> 

-------

<a name="HistoricalLinguistics"></a>
## [Resources and Tools for Computational Historical Linguistics]()
- The Java code for automatically identifying and producing related words for historical linguistics: [link](https://github.com/alinaciobanu/cognates).
- The translations used for dictionary-based identification of cognates: [link](https://drive.google.com/file/d/1wzUHAOfew-erprHblYFNqwwupUslZiG3/view).
- The input and output files for experiments on identification and production of relate words: [link](https://drive.google.com/file/d/1jXvzmbcLjP0ZhVhQIXFpuQ5XqUXrJQDb/view).

-------

<a name="NeuralTS"></a>
## [Neural Text Simplification Models](https://github.com/senisioi/NeuralTextSimplification)
- We present the first attempt at using sequence to sequence neural networks to model text simplification (TS). Unlike the previously proposed automated methods, our neural text simplification (NTS) systems are able to simultaneously perform lexical simplification and content reduction. An extensive human evaluation of the output has shown that NTS systems achieve good grammaticality and meaning preservation of output sentences and higher level of simplification than the state-of-the-art automated TS systems.
- Follow the steps, in order to generate simplified text:

	1. Checkout [our repository](https://github.com/senisioi/NeuralTextSimplification) including the submodules: `git clone --recursive https://github.com/senisioi/NeuralTextSimplification.git`
	2. Download the pre-trained released models [NTS](https://drive.google.com/open?id=0B_pjS_ZjPfT9dEtrbV85UXhSelU) and [NTS-w2v](https://drive.google.com/open?id=0B_pjS_ZjPfT9ZTRfSFp4Ql92U0E) (this may take a while): `python src/download_models.py ./models`
	3. Run translate.sh from the scripts dir: `cd src/scripts && ./translate.sh`


-------

<a name="ENNTT"></a>
## [Europarl Corpus of Native, Non-native and Translated Texts - ENNTT](https://github.com/senisioi/enntt-release)

- A complete description of this resource is available [here](http://www.lrec-conf.org/proceedings/lrec2016/summaries/902.html): **A Corpus of Native, Non-native and Translated Texts**, LREC, 2016, [PDF](http://www.lrec-conf.org/proceedings/lrec2016/pdf/902_Paper.pdf)
- For the raw corpus, please check the dataset available [here](https://github.com/nlp-unibuc/nlp-unibuc-website/releases/download/v1.0/ENNTT.tar.gz)
- For the experiments presented in the ACL 2016 paper, please check the dataset available [here](https://github.com/nlp-unibuc/nlp-unibuc-website/releases/download/v2.0/ACL2016.tar.gz)
- For the experiments presented in the [LREC 2016](http://www.lrec-conf.org/proceedings/lrec2016/summaries/902.html) paper, please check the dataset available [here](https://github.com/nlp-unibuc/nlp-unibuc-website/releases/download/v1.2/LREC2016_experiment.tar.gz)
### Short description:
- This is a monolingual English corpus of native, non-native and (human) translated texts extracted from the [European Parliament](http://www.statmt.org/europarl/). The translated texts from different source languages represent a subset of the [Haifa Corpus of Translationese](http://arxiv.org/abs/1509.03611). We preserved the same annotation style and included an ID and the EU state that each member of the European Parliament represents.
- We hope this dataset will facilitate a unified comparative study of translations and language produced by highly fluent non-native speakers, two closely-related phenomena that have only been studied in isolation so far.


-------

<a name="Wittgenstein"></a>
## [A Visual Representation of Wittgenstein's Tractatus Logico-Philosophicus](http://tractatus.gitlab.io/)
- [This work](http://www.gitxiv.com/posts/rNgtXTaiLWDE4HK6n) is the result of our collaboration with Anca Bucur, Ph.D. candidate, from the [Center of Excellence in Image Study](http://cesi.ro/fr/info/general.htm).
- We compile a multilingual parallel corpus from different versions of Wittgenstein's Tractatus Logico-Philosophicus, including the original in German and translations into English, Spanish, French, and Russian. Using this corpus, we compute a similarity measure between propositions and render [a visual network of relations](http://tractatus.gitlab.io/) for different languages.

-------

<a name="SpeechText"></a>
## [Comparing Speech and Text Classification of Native and Non-native English](https://github.com/senisioi/speech-text-features)
- We provide a comparison of speech and text classification of native and non-native English using a subset of the International Corpus Network of Asian Learners of English ([ICNALE](http://language.sakura.ne.jp/icnale/))
- The analysis is reported in the paper Nisioi, S., **Comparing Speech and Text Classification on ICNALE**, LREC 2016

-------

<a name="RoDet"></a>
## [Romanian Determiners Lexicon - RoDetLexicon 1.1](/resources/RoDetLexicon.pdf)
- The first version of Romanian Determiners Lexicon ([RoDetLexicon 1.1](/resources/RoDetLexicon.pdf)) specifies the relevant features for determiners studied so far during the research project "The structure and interpretation of Romanian Determiner Phrase in Discourse Representation Theory: the determiners". The importance of determiners comes from both syntax and semantics. From the point of view of syntactic theory, specifying the determiner’s relevant features naturally leads to the determination of the parameters of syntactic variation in the Determiner Phrase domain. From the discursive perspective, determinants have a fundamental role, being the most important constituents when it comes to establishing the logical structure of the sentence or of the discourse.
- The feature matrix of each determiner contains morpho-syntactic and semantic features, as they emerged from the studies developed during the project, such as: syntactic category, selectional features, phi-features (person, number, gender), definiteness, quantificational features, cardinality, focus, topic, deixis, proximity, contrastive, location, anaphoric, cataphoric or classifier.
- More details are available [this](http://www.unibuc.ro/depts/limbi/limbi_moderne/docs/2015/noi/16_14_13_26RoDetLexicon.pdf) paper.

-------

<a name="LangSim"></a>
## [Degrees of Similarity Between Romanian and Related Languages](/resources/rosim.pdf)
- More details are available in Ciobanu, A.M. and Dinu, L.P.,  **An Etymological Approach to Cross-Language Orthographic Similarity. Application on Romanian**, EMNLP 2014 [PDF](http://emnlp2014.org/papers/pdf/EMNLP2014112.pdf)

-------

<a name="NER"></a>
## [Cross-lingual Named Entity Recognition](https://github.com/senisioi/clwe-ner)
- Experiments on named entity translation using word embeddings are described in Şulea, O. M., Nisioi, S., and Dinu, L. P.,:, **Using Word Embeddings to Translate Named Entities**, LREC2016
- This resource is an annotated parallel corpus of named entities, currently work in progress

-------

<a name="pejor"></a>
## [A Computational Exploration of Pejorative Language in Social Media](https://aclanthology.org/2021.findings-emnlp.296/)
- More details about this resource can be found in Dinu, L. P., Iordache, I. B., Uban, A. S., Zampieri, M.: **A Computational Exploration of Pejorative Language in Social Media**, Findings of the Association for Computational Linguistics: EMNLP 2021.
- the dataset can be downloaded via this [link](https://drive.google.com/file/d/1ArQLZCbCpb9eHudqetapCv3oN0nA5Tc_).



