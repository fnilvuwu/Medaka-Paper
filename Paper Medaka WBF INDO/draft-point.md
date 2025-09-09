# Abstract

Medaka (Oryzias) fish, such as the Java medaka (Oryzias javanicus) and Celebes medaka (Oryzias celebensis), play vital roles in maintaining biodiversity and balance in the aquatic ecosystem of Indonesia. They serve as bioindicators of environmental health and are extensively researched in ecotoxicology. In this study, a manually annotated dataset of 1,247 Medaka images gathered from various aquatic environments is used to assess the performance of YOLOv8 and an ensemble approach employing Weighted Box Fusion (WBF).5 models were trained and validated using 5-fold cross-validation.With an mAP@0.5:0.95 of 0.5905, the YOLOv8-WBF ensemble significantly outperformed the best single model by 18.6\% (0.4979). With precision gains of up to 82\% at ideal confidence thresholds, the ensemble method showed superior bounding box localisation and classification reliability, especially for small and visually challenging fish instances. Although computational efficiency dropped by about 4.3× when compared to single models, the improved accuracy offers significant value for offline ecological monitoring and conservation workflows where detection reliability is prioritised.This work sets a benchmark for ensemble-based aquatic species detection systems and contributes to more robust biodiversity monitoring protocols by improving overall detection consistency across environmental variations and reducing missed detections of rare species by 23\%.


# 1. Introduction


