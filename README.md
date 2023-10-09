# Generative Design for Drug Discovery (Gen-3D)
Gen-3D is a Generative Data Benchmark design for Drug Discovery. This is code use  a subset of data from DBAASP suited for active learning for generating peptides and scVelo - RNA velocity generalized through dynamical modeling.


# Overview 

DBAASP serves as the central repository for vital information essential for conducting structure-activity relationship studies.

Our prediction service empowers users to determine the antimicrobial potential of queried peptides solely based on their amino acid sequences. These tools are designed to facilitate the precision-driven development of new antibiotics, resulting in significantly reduced production costs.

When using DBAASP, users can seamlessly search for peptide activities specific to target species, receiving search results in the form of a ranked list of activity values.

Furthermore, DBAASP enables the creation of experimentally validated positive (AMP) and negative (non-AMP) peptide sets tailored for specific target species. Consequently, DBAASP offers a machine-learning-driven prediction tool and an effective methodology for crafting innovative antibiotics.


RNA velocity, a powerful technique, allows for the retrieval of directed dynamic information through the utilization of splicing kinetics. Our methodology is based on scVelo, which extends and refines the concept of RNA velocity introduced by La Manno et al. in their 2018 Nature paper. This extension is achieved by relaxing previously held assumptions and employing both stochastic and dynamical models that comprehensively address the intricacies of transcriptional dynamics. As a result, we adapt RNA velocity to accommodate a diverse range of scenarios, including those involving non-stationary populations.