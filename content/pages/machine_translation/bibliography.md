Title: Machine Translation Learning
Slug: machine_translation/bibliography

<a name="bibliography"></a>
# **MT Bibliography (expanding...)**

\* blog posts, tutorials, visual explanations 

- [Prerequisites: general ML concepts, blogs, tutorials](#prereqs)
- [Statistical Machine Translation & Language Models](#smt)
- [Evaluation](#eval)
- [Data Collection, Alignment](#data)
- [Neural MT with RNNs](#neural)
- [Neural MT with CNNs](#neural_cnn)
- [Tokenizers](#tokenizers)
- [Neural MT with Transformers](#trans)
- [Neural MT with Diffusion Models](#diffusion)
- [Back to the future](#soviet)
- [Other Courses](#courses)


<a name="prereqs"></a>
## Prerequisites: general ML concepts, blogs, tutorials
- [Linear Algebra](https://codingthematrix.com)
- [Multivariate Calculus](https://www.khanacademy.org/math/multivariable-calculus/)
- [Probability Course](https://www.probabilitycourse.com/chapter1/1_4_4_conditional_independence.php)
- [Beautiful Visualizations - Proba and Stats](https://seeing-theory.brown.edu)
- [Bayesian Statistics](https://allendowney.github.io/ThinkBayes2/)
- [Count Bayes Blog](https://www.countbayesie.com/all-posts)
- [Five Minutes Stats](https://stephens999.github.io/fiveMinuteStats/index.html)
- [Expectation Maximization (EM) Foundations](https://www.lri.fr/~sebag/COURS/EM_algorithm.pdf)
- [EM for Gaussian Mixture Models](https://stackoverflow.com/questions/11808074/what-is-an-intuitive-explanation-of-the-expectation-maximization-technique/43561339#43561339)
- [Hidden Markov Models, EM, and Viterbi](https://web.stanford.edu/~jurafsky/slp3/A.pdf)
- [Information Theory, Entropy, KL-Divergence](https://colah.github.io/posts/2015-09-Visual-Information/)
- [Monte Carlo / Metropolis](https://www.algorithm-archive.org/contents/monte_carlo_integration/monte_carlo_integration.html)
- [DS Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)


## Prerequisites, general ML concepts, books
- [Pattern Recognition And Machine Learning](http://users.isr.ist.utl.pt/~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf) - huge book of the early 2000s, excellent coverage of probability distributions, graphical models, Bayesian inference
- [Statistical Foundations of ML](https://gianluca.bontempi.web.ulb.be//mod_stoch/syl.pdf) - course syllabus, good coverage of probabilities, statistical tests, general treatment of ML methods
- [Information Theory, Inference, and Learning Algorithms](https://www.inference.org.uk/itprnn/book.pdf) - huge book of the early 2000s, excellent coverage of information theory and probabilistic inference
- [Math for ML](https://mml-book.github.io/) - when you want to start from the very basics of algebra, geometry, calculus, probabilities
- [Probabilistic Machine Learning Book 1,2,3](https://probml.github.io/pml-book/) - excellent coverage of foundations, and more advanced topics (like diffusion models)
- [Deep Learning Book](https://www.deeplearningbook.org) - good place to understand neural networks


<a name="smt"></a>
## Statistical Machine Translation & Language Models
- [\*Kevin Knight's Workbook](https://kevincrawfordknight.github.io/papers/wkbk.pdf)
- [\*Lena Voita's explanations on LM](https://lena-voita.github.io/nlp_course/language_modeling.html)
- [Koehn's SMT book](https://www2.statmt.org/book/) (SMT from scratch)
- [Knesser-Ney smoothing](https://sci-hub.se/10.1109/ICASSP.1995.479394), 1995, [\*tutorial](http://www.foldl.me/2014/kneser-ney-smoothing/)
- [Och's PhD thesis](https://publications.rwth-aachen.de/record/58741/files/58741.pdf#page=22), 2002
- [Mathematics of SMT](https://aclanthology.org/J93-2003.pdf), 2003
- [N-gram Language Models, Jurafsky, SLP](https://web.stanford.edu/~jurafsky/slp3/3.pdf)
<!-- [**Lab Notebook:** IBM Model 1]() -->

<a name="eval"></a>
## Evaluation
- [BLEU, Papineni et al.](https://aclanthology.org/P02-1040.pdf), 2002
- [Statistical significance tests](https://aclanthology.org/W04-3250.pdf), 2004
- [Statistical significance tests of models' correlation](https://aclanthology.org/D14-1020.pdf), 2014
- [chrF++](https://aclanthology.org/W15-3049/), 2015
- [Comparison of metrics, Formicheva & Specia](https://aclanthology.org/J19-3004.pdf), 2018
- [A Call for Clarity in Reporting BLEU Scores](https://aclanthology.org/W18-6319/), 2018, [sacre bleu](https://github.com/mjpost/sacrebleu)
- [Good translation wrong in context](https://aclanthology.org/P19-1116/), 2019
- [BERTScore](https://arxiv.org/pdf/1904.09675.pdf), 2020
- [Scientific Credibility](https://arxiv.org/pdf/2106.15195.pdf), 2021
- [COMET](https://aclanthology.org/2020.emnlp-main.213/), [more recent paper](https://arxiv.org/abs/2202.05148) 2022 
- [**Lab Notebook:** MT Evaluation](https://colab.research.google.com/drive/1ZdILLE7kituJlZA-AVUOgq1pM0Ub5kTy?usp=sharing)


<a name="data"></a>
## Data Collection, Alignment
- [\*bitextor](https://github.com/bitextor/bitextor)
- [Parallel corpora for medium density languages](https://catalog.ldc.upenn.edu/docs/LDC2008T01/ranlp05.pdf), 2005 [hunalign](https://github.com/danielvarga/hunalign)
- [Word Alignment with Markov Chain Monte Carlo](https://ufal.mff.cuni.cz/pbml/106/art-ostling-tiedemann.pdf), 2016, [efmaral](https://github.com/robertostling/efmaral)
- [Backtranslation](https://aclanthology.org/P16-1009/), 2015
- [Word Alignments Without Parallel Training Data](https://aclanthology.org/2020.findings-emnlp.147.pdf), 2020, [SimAlign](https://github.com/cisnlp/simalign)
- [Aligned segments from unclean parallel data](http://nl.ijs.si/jtdh20/pdf/JT-DH_2020_Popovic-et-al_Extracting-correctly-aligned-segments-from-unclean-parallel-data-using-character-n-gram-matching.pdf), 2020
- [Comparison of GIZA++ vs. Neural Word Alignment](https://aclanthology.org/2020.acl-main.146.pdf), 2020
- [Massively Multilingual Sentence Embeddings](https://aclanthology.org/Q19-1038/), 2019
- [Multilingual Sentence Embeddings](https://aclanthology.org/2020.emnlp-main.365.pdf), 2020
- [Mining Using Distilled Sentence](https://arxiv.org/abs/2205.12654), 2022, [LASER](https://github.com/facebookresearch/LASER)
- [MT for the next 1000 Lang](https://arxiv.org/pdf/2205.03983.pdf), 2022
- [**Lab Notebook:** Using LASER](https://colab.research.google.com/drive/1UP-LxZdaAii7WrUw13GGblhMfas-WRLL?usp=sharing)


<a name="neural"></a>
## Neural MT with RNNs
- [\*Seq2seq Models With Attention](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)
- [\*Seq2seq Models Tutorial](https://lena-voita.github.io/nlp_course/seq2seq_and_attention.html)
- [\*Another tutorial](https://lorenlugosch.github.io/posts/2019/02/seq2seq/)
- [\*Different attention types](https://lilianweng.github.io/posts/2018-06-24-attention/)
- [\*Tutorial on training RNNs](https://www.ai.rug.nl/minds/uploads/ESNTutorialRev.pdf), 2002-2013
- [Learning Long-term Dependencies are Difficult](https://sci-hub.se/10.1109/72.279181), 1994
- [LSTM](http://www.bioinf.jku.at/publications/older/2604.pdf), 1997
- [Neural Probabilisitc Language Model](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf), 2003, also [here](https://www.researchgate.net/profile/Y-Bengio/publication/244436420_New_distributed_probabilistic_language_models/links/546b702c0cf2f5eb18091df1/New-distributed-probabilistic-language-models.pdf)
- [Seq2seq learning with NNs](https://proceedings.neurips.cc/paper/2014/file/a14ac55a4f27472c5d894ec1c3c743d2-Paper.pdf), 2014
- [RNN Encoder-Decoder](http://emnlp2014.org/papers/pdf/EMNLP2014179.pdf), 2014
- [Seq2seq with Attention](https://arxiv.org/abs/1409.0473), 2015
- [More Types of Attention](https://arxiv.org/abs/1508.04025), 2015
- [**Lab Tutorial:** Training an RNN seq2seq](https://colab.research.google.com/drive/1SI4N_-qwM-aWjyKf6kKgVPnp0R6jf-2g?usp=sharing)


<a name="neural_cnn"></a>
## Neural MT with CNNs
- [Language Modeling with Gated Convolutional Networks](https://arxiv.org/abs/1612.08083v3), 2016
- [Convolutional Sequence to Sequence Learning](https://proceedings.mlr.press/v70/gehring17a/gehring17a.pdf), 2017
- [\*Tutorial with code](https://charon.me/posts/pytorch/pytorch_seq2seq_5/)
- [**Lab Tutorial:** Training a CNN seq2seq](https://colab.research.google.com/github/bentrevett/pytorch-seq2seq/blob/master/5%20-%20Convolutional%20Sequence%20to%20Sequence%20Learning.ipynb)

<a name="tokenizers"></a>
## Tokenizers
- [\*Byte Pair Encoding](https://leimao.github.io/blog/Byte-Pair-Encoding/)
- [\*Tokenizers](https://blog.floydhub.com/tokenization-nlp/)
- [\*Understanding Sentencepiece](https://jacky2wong.medium.com/understanding-sentencepiece-under-standing-sentence-piece-ac8da59f6b08)
- [\*EM, Viterbi, Unigram LM](https://everdark.github.io/k9/notebooks/ml/natural_language_understanding/subword_units/subword_units.nb.html)
- [Byte-Pair Encoding Compression](http://www.pennelynn.com/Documents/CUJ/HTML/94HTML/19940045.HTM), 1994
- [Byte-Pair Encoding Tokenization](https://aclanthology.org/P16-1162/), 2015
- [Unigram LM Tokenizer](https://aclanthology.org/P18-1007/), 2018
- [sentencepiece library](https://aclanthology.org/D18-2012.pdf), 2018, [code](https://github.com/google/sentencepiece/)
- [BPE Dropout](https://aclanthology.org/2020.acl-main.170/), 2020
- [**Lab Tutorial:**](https://colab.research.google.com/drive/188kcihidA2i3MbPhKW5lDLqoJDIjvSWT?usp=sharing), [sentencepiece only](https://colab.research.google.com/github/google/sentencepiece/blob/master/python/sentencepiece_python_module_example.ipynb)


<a name="trans"></a>
## \*Transformers - Tutorials
- [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [Lena Voita's Tutorial](https://lena-voita.github.io/nlp_course/seq2seq_and_attention.html#transformer_intro)
- [The Annotated Transformer](http://nlp.seas.harvard.edu/annotated-transformer/)
- [Peter Bloem's Tutorial](http://peterbloem.nl/blog/transformers)
- [Illustrated BERT](https://jalammar.github.io/illustrated-bert/)
- [Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/)
- [Huggingface Transformers Tutorial](https://huggingface.co/course/chapter0/1)
- [Annotated GPT-2](https://amaarora.github.io/2020/02/18/annotatedGPT2.html)
- [Transformer for people outside NLP](https://data-science-blog.com/blog/2020/12/30/transformer/)
- [E2ML School Tutorial](https://e2eml.school/transformers.html)

## Transformers - Essential Readings
- [Attention is all you Need](https://arxiv.org/pdf/1706.03762.pdf), 2017
- [BERT](https://aclanthology.org/N19-1423.pdf), 2019
- [GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf), 2019
- [WMT2021 Baselines and Models](https://aclanthology.org/2021.wmt-1.1.pdf#page=34), 2021
- [**\*Models in huggingface**](https://huggingface.co/docs/transformers/index)


## Other Transformer Models 
- [GPT-3](https://papers.nips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html), 2020, [open gpt flavors](https://www.eleuther.ai/)
- [ELECTRA](https://openreview.net/forum?id=r1xMH1BtvB), 2019, [hgfce](https://huggingface.co/docs/transformers/main/en/model_doc/electra)
- [RoBERTa](https://aclanthology.org/2021.ccl-1.108/), 2019, [hgfce](https://huggingface.co/docs/transformers/main/en/model_doc/roberta)
- [BART](https://aclanthology.org/2020.acl-main.703/), 2020, [hgfce](https://huggingface.co/docs/transformers/main/en/model_doc/bart)
- [mBART](https://aclanthology.org/2020.tacl-1.47.pdf), 2020, [hgfce](https://huggingface.co/docs/transformers/main/en/model_doc/mbart)
- [\*Reformer](https://ai.googleblog.com/2020/01/reformer-efficient-transformer.html), 2020, [hgfce](https://huggingface.co/docs/transformers/main/en/model_doc/reformer)
- [T5](https://jmlr.org/papers/v21/20-074.html), 2020, [hgfce](https://huggingface.co/docs/transformers/main/en/model_doc/t5#overview), [hgfce](https://huggingface.co/docs/transformers/main/en/model_doc/t5)
- [M2M-100](https://jmlr.csail.mit.edu/papers/volume22/20-1307/20-1307.pdf), 2021, [model](https://huggingface.co/facebook/m2m100_1.2B), [hgfce](https://huggingface.co/docs/transformers/main/en/model_doc/m2m_100)
- [**Lab Tutorial:** T5](https://goo.gle/t5-colab)


## Transformers and Explainability
- [Visualizing Attention](https://arxiv.org/pdf/1904.02679.pdf), 2019
- [Is Attention Interpretable?](https://aclanthology.org/P19-1282/), 2019
- [Quantifying Attention Flow in Transformers](https://arxiv.org/pdf/2005.00928.pdf), 2020
- [Transformer Interpretability Beyond Attention](https://openaccess.thecvf.com/content/CVPR2021/papers/Chefer_Transformer_Interpretability_Beyond_Attention_Visualization_CVPR_2021_paper.pdf), 2021, [code](https://github.com/hila-chefer/Transformer-Explainability)


## Machine Translation Frameworks
- [Marian MT](https://aclanthology.org/P18-4020/), 2018
- [OpenNMT](https://opennmt.net/publications/), 2017
- [fairseq](https://aclanthology.org/N19-4009.pdf), 2019
- [JoeyNMT](https://aclanthology.org/D19-3019v1.pdf), 2019
- [Huggingface seq2seq](https://huggingface.co/docs/transformers/main/en/model_summary#sequencetosequence-models)

## Extra Readings on Machine Translation
- [Gender Bias in MT](https://aclanthology.org/P19-1164/), 2019
- [MT Domain Robustness](https://aclanthology.org/2020.amta-research.14/), 2019
- [Fixed Encoder Self-Attention Patterns](https://aclanthology.org/2020.findings-emnlp.49.pdf), 2020
- [Translationese](https://aclanthology.org/2020.acl-main.691.pdf), 2020
- [Character-level NMT](https://aclanthology.org/2020.acl-main.145.pdf), 2021


## Recent / Interesting Research
- [Synchronous Bidirectional Beam Search](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00256/43504/Synchronous-Bidirectional-Neural-Machine), 2019 
- [Specialized Heads Do the Heavy Lifting](https://aclanthology.org/P19-1580/), [code](https://github.com/lena-voita/the-story-of-heads), [tutorial](https://lena-voita.github.io/posts/acl19_heads.html) 2019
- [Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html), 2021
- [Why Beam Search Works](https://aclanthology.org/2020.emnlp-main.170/), 2021
- [What Works Best for Zero-Shot](https://proceedings.mlr.press/v162/wang22u.html), 2022
- [Contrastive Text Generation](https://openreview.net/pdf?id=V88BafmH9Pj), 2022, [code](https://github.com/yxuansu/SimCTG)
- [Induction Heads](https://arxiv.org/abs/2209.11895), 2022
- [Wide Attention vs Depth](https://arxiv.org/abs/2210.00640), 2022
- [The 48 params of BERT](https://arxiv.org/abs/2205.11380), 2022
- [Mixture of Experts](https://arxiv.org/pdf/2112.10684.pdf), 2022
- [The Importance of Attention](https://arxiv.org/abs/2211.03495), 2022

<a name="diffusion"></a>
## Neural MT with Diffusion Models
- [\*Energy-based Models](https://energy-based-model.github.io/Energy-based-Model-MIT/#Home)
- [Translation with DM](https://arxiv.org/abs/2111.01471), 2021
- [Text Generation](https://openreview.net/pdf?id=T0GpzBQ1Fg6), 2021
- [DiffuSeq](https://arxiv.org/abs/2210.08933), 2022


<a name="soviet"></a>
## Back to the future
- [Shannon's Autoregressive Language Models](https://sci-hub.se/10.1002/j.1538-7305.1951.tb01366.x), 1950
- [ALPAC report](https://nap.nationalacademies.org/resource/alpac_lm/ARC000005.pdf), 1966, summary [here](https://blog.pangeanic.com/alpac-report)
- [Statistical Methods and Linguistics](http://www.vinartus.net/spa/95c.pdf), 1995
- [The Future of MT, seen from 1985](https://aclanthology.org/J85-1001.pdf)
- [MT in the USSR, 1984](https://www.jstor.org/stable/30199988?seq=1#metadata_info_tab_contents)
- [Soviet MT overview, Gordin, 2020](https://static1.squarespace.com/static/5275adb7e4b0298e6ac6bc86/t/5ef3eb6693fc2660294da7e2/1593043815386/Gordin-SovietMT.pdf)
- [Survey of MT in USSR, 2010](https://sci-hub.se/10.1080/0907676X.1997.9961304)

<a name="courses"></a>
## Other Courses
- [MT at Charles University](https://ufal.mff.cuni.cz/courses/npfl087#lectures)
- [MT at Johns Hopkins University](http://mt-class.org/jhu/index.html)
- [MT at University of Pennsylvania](http://mt-class.org/penn/syllabus.html)
- [MT at Tartu Ülikool](https://courses.cs.ut.ee/2022/mt/spring/Main/HomePage)
- [Lena Voita's NLP Course](https://lena-voita.github.io/nlp_course)
- [Alfredon Canziani's Deep Learning Course](https://atcold.github.io/didactics.html)
- [Anil Damle and Kilian Weinberger's intro to ML Course](https://www.cs.cornell.edu/courses/cs4780/2021fa/)
- Some also in the [prerequisites](#prereqs)


