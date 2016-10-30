Title: SIGAR - Sistem Inteligent de Generare Automată a Răspunsurilor 
Slug: projects/sigar

# Intelligent Systems for Automatic Response Generation
SIGAR: Project 53BG ⁄ 2016, funded by  Romanian National Authority for Scientific Research and Innovation, CNCS/CCCDI – UEFISCDI, PNCDI III (Programul 2 - Creşterea competitivităţii economiei româneşti prin cercetare, dezvoltare şi inovare. Transfer de cunoaștere la agentul economic "Bridge Grant")

## Abstract
In this project, we develop a natural language processing solution for an automatic question-answering system. The solution will be used within the Enterprise Resource Planning systems developed by Pluriva SRL. By applying various preprocessing filters and parsing stages, we extract pairs of question-prototypical answer from a database provided by Pluriva. We use the pairs as to train a machine learning algorithm for text classification. Our solution is built from two main components: (1) a language-independent core, constructed from multiple strong classifiers aggregated into a single optimal response, and (2) a component built as a language-specific extension, which consists of optimized models for Romanian. The NLP tools available for Romanian are scarce and insufficiently robust to be successful when the texts are not written correctly (as it is the case with the ones residing in the database offered by Pluriva), therefore, we extend and develop our own resources specific for this particular dataset. We build tools for diacritic restoration, named entity recognition, and part of speech tagging. 
A question answering machine learning system is a valuable resource for any company that uses customer relationship management software, helping to increase the quality and efficiency of the services, decrease of redundant work for the employees, and possibly reducing the average waiting time to solve a service request. 

