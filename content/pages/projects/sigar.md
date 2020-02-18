Title: SIGAR - Sistem Inteligent de Generare Automată a Răspunsurilor 
Slug: projects/sigar

# Intelligent Systems for Automatic Response Generation
SIGAR: Project 53BG ⁄ 2016, funded by Romanian National Authority for Scientific Research and Innovation, CNCS/CCCDI – UEFISCDI, PNCDI III (Programul 2 - Creşterea competitivităţii economiei româneşti prin cercetare, dezvoltare şi inovare. Transfer de cunoaștere la agentul economic "Bridge Grant")

## Abstract
In this project, we develop a natural language processing solution for an automatic question-answering system. The solution will be used within the Enterprise Resource Planning systems developed by Pluriva SRL. By applying various preprocessing filters and parsing stages, we extract pairs of question-prototypical answer from a database provided by Pluriva. We use the pairs as to train a machine learning algorithm for text classification. Our solution is built from two main components: (1) a language-independent core, constructed from multiple strong classifiers aggregated into a single optimal response, and (2) a component built as a language-specific extension, which consists of optimized models for Romanian. The NLP tools available for Romanian are scarce and insufficiently robust to be successful when the texts are not written correctly (as it is the case with the ones residing in the database offered by Pluriva), therefore, we extend and develop our own resources specific for this particular dataset. We build tools for diacritic restoration, named entity recognition, and part of speech tagging. 
A question answering machine learning system is a valuable resource for any company that uses customer relationship management software, helping to increase the quality and efficiency of the services, decrease of redundant work for the employees, and possibly reducing the average waiting time to solve a service request. 

---

## Partener
Pluriva SRL este o companie de produse și servicii informatice înființată acum aproape 20 de ani, al carei principal principal produs este un sistem informatic integrat ce acoperă toate fluxurile de business necesare operării unei afaceri. Pluriva ERP are peste 50 de module, grupate în 11 categorii. Pluriva SRL asigura atat servicii, cat si suport tehnic post implementare. Pentru acest lucru, Pluriva a dezvoltat un sistem de achizitionare prin email a cererilor de la utilizatori impreuna cu solutiile identificate si oferite de specialistii proprii la capatul unui intreg lant de activitati. In cei 5 ani de implementare, au fost achizitionate un numar semnificativ de cereri si raspunsuri. Din practică, s-a observat că utilizatorii formulează de multe ori întrebări în limbaj natural, a căror rezolvare este deja descrisă de multe ori într-un raspuns (tichet) deja existent și stocat în baza de date. Pentru a obține o reacție mult mai rapidă la întrebările utilizatorilor, a fost identificata nevoia unei aplicatii care să sugereze automat o posibilă rezolvare, selectând dintre tichetele deja existente. Acest lucru face obiectivul principal al proiectului nostru.


## Obiective

### [Faza 1]('reports/raport-sigar-16.pdf')

##### Activitate 1.1: accesarea și pre-procesarea datelor. 
În scopul realizarii acestei activități următoarele acțiuni au fost planificate și realizate:
- Acces la date și determinarea specificațiilor
- Extragerea datelor și pregătirea acestora pentru procesare statistică și cantitativă a datelor

##### Activitate 1.2: Proiectare software. 
Principala acțiune desfășurată în cadrul acestei activități a fost analiza inițială și evaluarea unui algoritm de topic modelling


### [Faza 2]('reports/raport-sigar-17.pdf')

#### Activitate 2.1: Adnotarea datelor. 
În scopul realizarii acestei activități următoarele acțiuni au fost planificate și realizate:
- Curatare si editare date Pluriva;
- Adnotare date pe categorii;
- Determinarea raspunsurilor prototip.
 
#### Activitate 2.2: Activitati diseminare. 
Principalele acțiuni desfășurate în cadrul acestei activități au fost participarea la conferinte, efectuarea unor stagii de cercetare, diseminarea rezultatelor in intalniri formale si informale, in organizarea unui seminar de cercetare, etc.
 
#### Activitate 2.3: Clasificare automata a subiectelor pe categorii (classification by topic). 
În scopul realizarii acestei activități următoarele acțiuni au fost planificate și realizate:
- Proiectare algoritm;
- Antrenare, testare, evaluare.
 
#### Activitate 2.4: Proiectare modul 1. 
Principalele acțiuni desfășurate în cadrul acestei activități au fost analiza, testarea, si evaluarea subclasificatorilor.
 
#### Activitate 2.5: Dezvoltare agregator. 
Principalele acțiuni desfășurate în cadrul acestei activități au fost analiza, testarea, si evaluarea agregatorului.
 
#### Activitate 2.6: Proiectare si dezvoltare retea neuronala.
Principalele acțiuni desfășurate în cadrul acestei activități au fost analiza, testarea, evaluare retelei precum si integrarea retelei in agregator.


### [Faza 3]('reports/raport-sigar-18.pdf')
 Dezvoltarea modulului de limba română,testarea și evaluarea metodelor proiectate în etapele anterioare. Pentru îndeplinirea acestui obiectiv, au fost planificate următoarele activități:

#### Activitate 3.1: Dezvoltarea de resurse specifice proiectului pentru limba română. În scopul realizării acestei activități următoarele acțiuni au fost planificate și realizate:
- analiza morfologica a datelor
- extragerea părților de vorbire pentru datele disponibile
- finalizarea adnotarilor pentru limba romana

#### Activitate 3.2: Activitati diseminare. 
Principalele acțiuni desfășurate în cadrul acestei activități au fost participarea la conferinte, efectuarea unor stagii de cercetare, diseminarea rezultatelor in intalniri formale si informale, in organizarea unui seminar de cercetare, etc. 

#### Activitate 3.3: Evaluare si testare module pentru limba romana
În scopul realizarii acestei activități următoarele acțiuni au fost planificate și realizate:
- analiza datelor fara diacritice
- detectarea entitatilor in romana
- evaluare, testare, ajustare

#### Activitate 3.4: Finalizarea modulelor,evaluarea, ajustarea rezultatelor.
Principalele acțiuni desfășurate în cadrul acestei activități au fost finalizarea resurselor pentru generarea răspunsurilor, testarea, evaluarea și ajustarea metodelor dezvoltate în etapele anterioare, întocmire rapoarte finale.

## Publicații
1. Alina Maria Ciobanu, Sergiu Nisioi, Liviu P. Dinu. Vanilla Classifiers for Distinguishing between Similar Languages. In Proc. Third Workshop on NLP for Similar Languages, Varieties and Dialects (VarDial3), co-located with COLING 2016, december 11-16, 2016, Osaka, Japan, pages 235-242.
2. Anca Bucur, Sergiu Nisioi. A Visual Representation of Wittgenstein’s Tractatus Logico-Philosophicus. In Proc. Language Technology Resources and Tools for Digital Humanities (LT4DH), co-located with COLING 2016, december 11-16, 2016, Osaka, Japan, pages 71-75, ISBN978-4-87974-708-2
3. Sergiu Nisioi, Sanja Štajner, Simone Paolo Ponzetto and Liviu P. Dinu, 2017. Exploring Neural Text Simplification Models. In Proc. of the 55th Annual Meeting of the Association for Computational Linguistics, ACL 2017, p 85-91, Vancouver, Canada, July 30 - August 4.
4. Alina Ciobanu, Liviu P. Dinu, and Andrea Sgarro, 2017. Towards a Map of the Syntactic Similarity of Languages. In Proc18th International Conference on Computational Linguistics and Intelligent Text Processing (CICLing 2017), Budapest, Hungary, Aprile 17-23, 2017(proceedings in curs de aparitie la Springer LNCS)
5. Alina Maria Ciobanu, Liviu P. Dinu, 2017. Romanian Word Production: an Orthographic Approach Based on Sequence Labeling. In Proc18th International Conference on Computational Linguistics and Intelligent Text Processing (CICLing 2017), Budapest, Hungary, Aprile 17-23, 2017(proceedings in curs de aparitie la Springer LNCS)
6. Marcos Zampieri, Alina Maria Ciobanu, Liviu P. Dinu. Native Language Identification on Text and Speech. Proceedings of the 12th Workshop on Innovative Use of NLP for Building Educational Applications (co-located with EMNLP 2017), pages 398–404 Copenhagen, Denmark, September 8, 2017.
7. Alina Maria Ciobanu, Marcos Zampieri, Shervin Malmasi, Liviu P. Dinu. Including Dialects and Language Varieties in Author Profiling.Working Notes of CLEF 2017 - Conference and Labs of the Evaluation Forum, Dublin, Ireland, September 11-14, 2017, {CEUR} Workshop Proceedings, vol. 1866
8. Cornelia Caragea, Liviu P. Dinu, Bogdan Dumitru, 2018. Exploring Optimism and Pessimism in Twitter Using Deep Learning. In Proc. EMNLP 2018, Brussels, Belgium, 2018 (to appear)
9. Sergiu Nisioi, Anca Bucur, Liviu P Dinu, 2018. Lexical Analysis and Content Extraction from Customer-Agent Interactions. Proceedings of the 2018 EMNLP Workshop W-NUT: The 4th Workshop on Noisy User-generated Text, pages 132–136 Brussels, Belgium, 2018
10. Alina Ciobanu, Liviu P. Dinu, 2018. Ab Initio: Latin Proto-word Reconstruction. In Proc.COLING 2018 (main conference), p. 1604-1614, Santa Fe, USA, 2018
11. Alina Ciobanu, Liviu P. Dinu, 2018. Simulating Language Evolution: A Tool for Historical Linguistics. In Proc.COLING 2018 (demo section), pp68-72, Santa Fe, USA, 2018 
12. Anca Bucur, 2018. Posthumanism, Technology, and Monstrous Life Forms. In Proceedings of ISEA 2018 - 24th International Symposium on Electronic Art, p 313-316, Durban, South Africa, 2018.
13. Bogdan Dumitru, Alina Ciobanu, Liviu P Dinu, 2018. ALB at SemEval-2018 Task 10: A System for Capturing Discriminative Attributes. In Proc SemEval 2018 (SemEval@NAACL-HLT 2018), task 10, p. 963-967, New Orleans, USA, 2018
14. Maria Sulea, Bogdan Dumitru, Liviu P. Dinu. Full Inflection Learning Using Deep Neural Networks, CICLing 2018, Hanoi, Vietnam, 2018
15. Liviu P Dinu, Ana Uban, 2018. Analyzing Stylistic Variation across Different Political Regimes, CICLing 2018, Hanoi, Vietnam, 2018
16. Sanja Stajner, Sergiu Nisioi, 2018. A Detailed Evaluation of Neural Sequence-to-Sequence Models for In-domain and Cross-domain Text Simplification. Proceedings of 11th edition of the Language Resources and Evaluation Conference (LREC 2018), p. 3026-3033, 7-12 May 2018, Miyazaki (Japan) .