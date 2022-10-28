Title: Machine Translation Course, Information, Yearly Results
Slug: machine_translation


<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>


# Academic year 2022-2023

\\[ T(f \rightarrow e) = \arg \max_{e} P(e)P(f|e) \\]

<style>
tr:nth-child(even) {
  background-color: #b2b2b24f!important;
  color: #1e1e1e!important;
}
</style>

# Contents
- [Schedule 2022](#schedule)
- [Roles](#roles)
    - [Author](#role_aut)
    - [Scientific reviewer](#role_sci)
    - [Engineer](#role_ing)
    - [Visionary](#role_vis)
    - [Attendees](#role_att)
- [Project ideas](#projects)
    - [TBA shortly]()
- [Bibliography](#bibliography)


<a name="schedule"></a>
# Schedule of MT classes 2022


|Week |    **Date**   |     **Topic**    | **Materials** |                       **Presenters**                       |
:|:-------------:|:----------------:|:--------------------:|:----------------------------------------------------------:|
|01|  7. Oct. 2022 | Teaching         |      [slides](https://unibucro0.sharepoint.com/:b:/r/sites/MachineTranslation2022/Shared%20Documents/General/Course1_structure.pdf?csf=1&web=1&e=ewkb3A)                |                                                            | 
|02| 14. Oct. 2022 | Teaching         |      [reading](#smt)               |                                                            | 
|03| 21. Oct. 2022 | Teaching         |  [reading](#eval)<br />[MT metrics(video)](https://slideslive.com/38924201/1-metrics-of-mt-quality)                |                                                            | 
|04| 28. Oct. 2022 | Teaching         |                      |                                                            |
|05|  4. Nov. 2022 | Teaching         |                      |                                                            |
|06| 11. Nov. 2022 |  Human and<br />Automatic Evaluation<br />Metrics     |           [**🤔 main paper**](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00437/108866/Experts-Errors-and-Context-A-Large-Scale-Study-of)<br />additional readings<br />[BERTScore](https://arxiv.org/pdf/1904.09675.pdf),<br />[WMT2020 Metrics](https://aclanthology.org/2020.wmt-1.77.pdf),<br />[Significance](https://aclanthology.org/D14-1020.pdf)         |     Rebeca Oprea (engineer),<br />Teodor Dumitrescu (author),<br />Chiruț Veronica (reviewer)                                                       |     
|07| 18. Nov. 2022 |  Data Acquisition            |          TBA            | 	Ahmad Wali (engineer),<br />Daniel Sava (author),<br />Iordăchescu Anca (reviwer)                                                       |
|08| 25. Nov. 2022 |  Language and Translation Models,<br />Smoothing,<br />Beam Search            |         TBA             |     Stan Flavius (author),<br />Bazavan Cristian (engineer),<br />Blăgescu Alex (reviewer),<br /> Stegarescu Ana (visionary)                                                       |
|09|  <del>2.</del> 8. Dec. 2022 |  Neural MT,<br />Vocabulary,<br />Attention,<br />Multilingualilty |          TBA           |     Ranete Cristian (reviewer),<br />Nedelcu Mihai (visionary),<br />Ilicea Anca (author),<br />Mărilă Mircea (engineer)                                                       |
|10|  9. Dec. 2022 |  Tokenizers,<br />Transformers,<br />T5,<br />Multilinguality                |      TBA                |     Bleoţiu Eugen (visionary),<br />Antal Mihaela (reviewer),<br />Istrati Lucian (engineer),<br />Dăscălescu Dana (author)                                                      |
|11| 16. Dec. 2022 |  Diffusion Models<br />(tentative)                |         TBA             |     Zăvelcă Miruna (engineer),<br />Lazăr Dorian (author),<br />Creanga Claudiu (reviewer),<br />Aldea Gabriela (visionary)                                                       |
|12| 23. Dec. 2022 | Projects 🌲      |                      |                                                            |
|13| 13. Jan. 2023 | Projects         |                      |                                                            |
|14| 20. Jan. 2023 | Projects         |                      |                                                            |

<a name="roles"></a>
# Roles

Each person is assigned a role (almost randomly) and must prepare the reading from the **Materials** 
column from the row where their name is added. Materials will be announced shortly.
Consider taking these roles seriously as they account for half of your grade.
Since December, 2 is during a public holiday, we can postpone the presentations for Thursday, December, 8.

<a name="role_aut"></a>
## Author
Pretend you are the main author of the papers, prepare a presentation and talk about:

- Problem definition: present what problems the authors intend to solve and present the context and necessity of why it is important to adress the problems.
- Methodology: present the methodology, the mathematical foundations; find an explanation for why this methodology is suitable for the problems at hand.
- Experimental findings: present the main results, how they compare with previous work.
- Get into as many details as possible; the appendices in the paper should also be covered.

<a name="role_sci"></a>
## Scientific reviewer
You must make a critical evaluation of the paper, not necessarily negative; read the guidelines  and examples from [NIPS](https://neurips.cc/Conferences/2020/PaperInformation/ReviewerGuidelines#Examples)

- Summary and contributions: Briefly summarize the paper and its contributions
- Strengths: Describe the strengths of the work. Typical criteria include: soundness of the claims (theoretical grounding, empirical evaluation), significance and novelty of the contribution, and relevance to the Machine Translatiion community.
- Weaknesses: Explain the limitations of this work along the same axes as above.
- Correctness: Are the claims and method correct? Is the empirical methodology correct?
- Clarity: Is the paper well written?
- Additional feedback, comments, suggestions for improvement and questions for the authors
- Overall score

<a name="role_ing"></a>
## Engineer
Implement something related to the paper either on the same dataset or on a new one;  prepare to share the code and some empirical intuition behind the paper.

- Reproducibility: If the original authors already provide the code, try to run it on a new dataset.
- Comments: Are there enough details to reproduce the major results of this work?
- Efficiency: Measure the time it takes to run the code, provide an assement of how suitable the approach is for being run at scale.

<a name="role_vis"></a>
## Visionary
Propose a follow-up research project or a new application; take into account the previous work and existing work being done; take into account ethics and the socio-economic impact:

- Relation to prior work: Is it clearly discussed how this work differs from previous contributions?
- Have the authors adequately addressed the broader impact of their work, including potential negative ethical and societal implications of their work?
- Does the submission raise potential ethical concerns? This includes methods, applications, or data that create or reinforce unfair bias or that have a primary purpose of harm or injury. If so, please explain briefly.

<a name="role_att"></a>
## Attendees
Everyone must ask a question at the end of the presentations to qualify as being present.
Being present at all the presentations will account for 1 bonus point at the end.


<a name="projects"></a>
# Project ideas
Stay tuned, will be announced shortly...


<a name="bibliography"></a>
# MT Bibliography (expanding...)

\* blog posts, tutorials, visual explanations 

<a name="smt"></a>
## Statistical Machine Translation & Language Models
- [\*Bayes from Scratch](https://allendowney.github.io/ThinkBayes2/)
- [\*Kevin Knight's Workbook](https://kevincrawfordknight.github.io/papers/wkbk.pdf)
- [Koehn's SMT book](https://3lib.net/book/1271436/711d48) (probabilities from scratch)
- [Och's PhD thesis, 2002](https://publications.rwth-aachen.de/record/58741/files/58741.pdf#page=22)
- [Mathematics of SMT](https://aclanthology.org/J93-2003.pdf)
- [Knesser-Ney smoothing, 1995](https://sci-hub.se/10.1109/ICASSP.1995.479394)
- [N-gram Language Models, Jurafsky, SLP](https://web.stanford.edu/~jurafsky/slp3/3.pdf)


<a name="eval"></a>
## Evaluation
- [BLEU, Papineni et al, 2002](https://aclanthology.org/P02-1040.pdf)
- [A Call for Clarity in Reporting BLEU Scores](https://aclanthology.org/W18-6319/), [sacre bleu](https://github.com/mjpost/sacrebleu)
- [BERTScore, 2020](https://arxiv.org/pdf/1904.09675.pdf)
- [Statistical significance tests](https://aclanthology.org/W04-3250.pdf), 2004
- [Statistical significance tests of models' correlation](https://aclanthology.org/D14-1020.pdf), 2014
- [Comparison of metrics, Formicheva & Specia](https://aclanthology.org/J19-3004.pdf), 2018
- [**Lab Notebook**](https://colab.research.google.com/drive/1ZdILLE7kituJlZA-AVUOgq1pM0Ub5kTy?usp=sharing)


<a name="data"></a>
## Data Collection, Alignment
- [bitextor](https://github.com/bitextor/bitextor)
- [Parallel corpora for medium density languages](https://catalog.ldc.upenn.edu/docs/LDC2008T01/ranlp05.pdf), 2005 [hunalign](https://github.com/danielvarga/hunalign)
- [Word Alignment with Markov Chain Monte Carlo](https://ufal.mff.cuni.cz/pbml/106/art-ostling-tiedemann.pdf), 2016, [efmaral](https://github.com/robertostling/efmaral)
- [Word Alignments Without Parallel Training Data](https://aclanthology.org/2020.findings-emnlp.147.pdf), 2020, [SimAlign](https://github.com/cisnlp/simalign)
- [Aligned segments from unclean parallel data](http://nl.ijs.si/jtdh20/pdf/JT-DH_2020_Popovic-et-al_Extracting-correctly-aligned-segments-from-unclean-parallel-data-using-character-n-gram-matching.pdf), 2020
- [Comparison of GIZA++ vs. Neural Word Alignment](https://aclanthology.org/2020.acl-main.146.pdf), 2020
- [Mining Using Distilled Sentence](https://arxiv.org/abs/2205.12654), 2022, [LASER](https://github.com/facebookresearch/LASER)


<a name="neural"></a>
## Neural MT with RNNs & CNNs
- [\*Seq2seq Models With Attention](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)
- [\*Different attention types](https://lilianweng.github.io/posts/2018-06-24-attention/)
- [Learning Long-term Dependencies are Difficult](https://sci-hub.se/10.1109/72.279181), 1994
- [LSTM](http://www.bioinf.jku.at/publications/older/2604.pdf), 1997
- [Neural Probabilisitc Language Model](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf), 2003, also [here](https://www.researchgate.net/profile/Y-Bengio/publication/244436420_New_distributed_probabilistic_language_models/links/546b702c0cf2f5eb18091df1/New-distributed-probabilistic-language-models.pdf)
- [Seq2seq learning with NNs](https://proceedings.neurips.cc/paper/2014/file/a14ac55a4f27472c5d894ec1c3c743d2-Paper.pdf), 2014
- [RNN Encoder-Decoder](http://emnlp2014.org/papers/pdf/EMNLP2014179.pdf), 2014
- [Seq2seq with Attention](https://arxiv.org/abs/1409.0473), 2015
- [More Types of Attention](https://arxiv.org/abs/1508.04025), 2015
- [\*Lab Tutorial](https://colab.research.google.com/github/pytorch/tutorials/blob/gh-pages/_downloads/seq2seq_translation_tutorial.ipynb)


<a name="trans"></a>
## Neural MT with Transformers
- [Attention is all you Need, 2017](https://arxiv.org/pdf/1706.03762.pdf)
- [\*Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [\*Huggingface Transformers Tutorial](https://huggingface.co/course/chapter0/1)
- [TBA]()


<a name="diffusion"></a>
## Neural MT with Diffusion Models
- [TBA]()


<a name="soviet"></a>
## Back to the future
- [Shannon's Autoregressive Language Models](https://sci-hub.se/10.1002/j.1538-7305.1951.tb01366.x), 1950
- [The Future of MT, seen from 1985](https://aclanthology.org/J85-1001.pdf)
- [MT in the USSR, 1984](https://www.jstor.org/stable/30199988?seq=1#metadata_info_tab_contents)
- [Soviet MT overview, Gordin, 2020](https://static1.squarespace.com/static/5275adb7e4b0298e6ac6bc86/t/5ef3eb6693fc2660294da7e2/1593043815386/Gordin-SovietMT.pdf)
- [Survey of MT in USSR, 2010](https://sci-hub.se/10.1080/0907676X.1997.9961304)










