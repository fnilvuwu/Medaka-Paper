Confidence 0.001
| Method          | mAP_0.5:0.95 | mAP_0.5 | mAP_0.75 | mAP_small | mAP_medium | mAP_large | mAR_1 | mAR_10 | mAR_100 | mAR_small | mAR_medium | mAR_large |
|-----------------|--------------|---------|----------|-----------|------------|-----------|-------|--------|---------|-----------|------------|-----------|
| Single YOLOv8   | 0.4979       | 0.8150  | 0.5404   | -1.0000   | 0.4269     | 0.5079    | 0.4422| 0.5978 | 0.6259  | -1.0000   | 0.5633     | 0.6361    |
| NMS Ensemble    | 0.5351       | 0.8493  | 0.5924   | -1.0000   | 0.4706     | 0.5507    | 0.4394| 0.6151 | 0.6613  | -1.0000   | 0.5667     | 0.6841    |
| WBF Ensemble    | 0.5905       | 0.8980  | 0.6754   | -1.0000   | 0.4504     | 0.6159    | 0.4901| 0.6718 | 0.7063  | -1.0000   | 0.5800     | 0.7311    |

Confidence 0.25
| Method          | mAP_0.5:0.95 | mAP_0.5 | mAP_0.75 | mAP_small | mAP_medium | mAP_large | mAR_1 | mAR_10 | mAR_100 | mAR_small | mAR_medium | mAR_large |
|-----------------|--------------|---------|----------|-----------|------------|-----------|-------|--------|---------|-----------|------------|-----------|
| Single YOLOv8   | 0.4729       | 0.7678  | 0.5201   | -1.0000   | 0.3874     | 0.4865    | 0.4227| 0.5519 | 0.5580  | -1.0000   | 0.4433     | 0.5813    |
| NMS Ensemble    | 0.5300       | 0.8444  | 0.5871   | -1.0000   | 0.4691     | 0.5437    | 0.4347| 0.6032 | 0.6206  | -1.0000   | 0.5467     | 0.6373    |
| WBF Ensemble    | 0.5460       | 0.8317  | 0.6255   | -1.0000   | 0.4109     | 0.5738    | 0.4599| 0.6020 | 0.6043  | -1.0000   | 0.4633     | 0.6324    |

Confidence 0.5
| Method          | mAP_0.5:0.95 | mAP_0.5 | mAP_0.75 | mAP_small | mAP_medium | mAP_large | mAR_1 | mAR_10 | mAR_100 | mAR_small | mAR_medium | mAR_large |
|-----------------|--------------|---------|----------|-----------|------------|-----------|-------|--------|---------|-----------|------------|-----------|
| Single YOLOv8   | 0.4380       | 0.7071  | 0.4747   | -1.0000   | 0.3874     | 0.4457    | 0.3971| 0.4954 | 0.5015  | -1.0000   | 0.4433     | 0.5094    |
| NMS Ensemble    | 0.5210       | 0.8280  | 0.5757   | -1.0000   | 0.4493     | 0.5384    | 0.4347| 0.5909 | 0.6016  | -1.0000   | 0.4900     | 0.6270    |
| WBF Ensemble    | 0.4740       | 0.7005  | 0.5555   | -1.0000   | 0.3149     | 0.5075    | 0.4108| 0.5142 | 0.5142  | -1.0000   | 0.3500     | 0.5466    |

Confidence 0.6
| Method          | mAP_0.5:0.95 | mAP_0.5 | mAP_0.75 | mAP_small | mAP_medium | mAP_large | mAR_1 | mAR_10 | mAR_100 | mAR_small | mAR_medium | mAR_large |
|-----------------|--------------|---------|----------|-----------|------------|-----------|-------|--------|---------|-----------|------------|-----------|
| Single YOLOv8   | 0.4313       | 0.6935  | 0.4675   | -1.0000   | 0.3874     | 0.4391    | 0.3889| 0.4871 | 0.4933  | -1.0000   | 0.4433     | 0.5012    |
| NMS Ensemble    | 0.5185       | 0.8256  | 0.5726   | -1.0000   | 0.4462     | 0.5364    | 0.4335| 0.5874 | 0.5969  | -1.0000   | 0.4833     | 0.6235    |
| WBF Ensemble    | 0.4181       | 0.6196  | 0.4868   | -1.0000   | 0.2240     | 0.4646    | 0.3737| 0.4573 | 0.4573  | -1.0000   | 0.2400     | 0.5088    |

Conf 0.001:
Per-class Metrics Summary (Single YOLOv8):
============================================================
category_id category_name  true_positives  false_positives  false_negatives  ground_truth_count  precision  recall  f1_score
          1  O.celebensis             119             1119                9                 128     0.0961  0.9297    0.1742
          2   O.javanicus              84             1203                5                  89     0.0653  0.9438    0.1221
    OVERALL       OVERALL             203             2322               14                 217     0.0807  0.9368    0.1482
  MICRO_AVG     MICRO_AVG             203             2322               14                 217     0.0804  0.9355    0.1481

============================================================
Per-class Metrics Summary (NMS Ensemble):
============================================================
category_id category_name  true_positives  false_positives  false_negatives  ground_truth_count  precision  recall  f1_score
          1  O.celebensis             122             8464                6                 128     0.0142  0.9531    0.0280
          2   O.javanicus              87             6914                2                  89     0.0124  0.9775    0.0245
    OVERALL       OVERALL             209            15378                8                 217     0.0133  0.9653    0.0263
  MICRO_AVG     MICRO_AVG             209            15378                8                 217     0.0134  0.9631    0.0264

============================================================
Per-class Metrics Summary (WBF Ensemble):
============================================================
category_id category_name  true_positives  false_positives  false_negatives  ground_truth_count  precision  recall  f1_score
          1  O.celebensis             128             3322                0                 128     0.0371  1.0000    0.0715
          2   O.javanicus              86             2571                3                  89     0.0324  0.9663    0.0626
    OVERALL       OVERALL             214             5893                3                 217     0.0347  0.9831    0.0671
  MICRO_AVG     MICRO_AVG             214             5893                3                 217     0.0350  0.9862    0.0677

============================================================

================================================================================
EVALUATION RESULTS COMPARISON
================================================================================
       method  mAP_0.5:0.95  mAP_0.5  mAP_0.75  mAP_small  mAP_medium  mAP_large  mAR_1  mAR_10  mAR_100  mAR_small  mAR_medium  mAR_large
Single YOLOv8        0.4979   0.8150    0.5404    -1.0000      0.4269     0.5079 0.4422  0.5978   0.6259    -1.0000      0.5633     0.6361
 NMS Ensemble        0.5351   0.8493    0.5924    -1.0000      0.4706     0.5507 0.4394  0.6151   0.6613    -1.0000      0.5667     0.6841
 WBF Ensemble        0.5905   0.8980    0.6754    -1.0000      0.4504     0.6159 0.4901  0.6718   0.7063    -1.0000      0.5800     0.7311

PRECISION Comparison Across Methods:
================================================================================
method         NMS Ensemble  Single YOLOv8  WBF Ensemble
category_name                                           
MICRO_AVG            0.0134         0.0804        0.0350
O.celebensis         0.0142         0.0961        0.0371
O.javanicus          0.0124         0.0653        0.0324
OVERALL              0.0133         0.0807        0.0347

RECALL Comparison Across Methods:
================================================================================
method         NMS Ensemble  Single YOLOv8  WBF Ensemble
category_name                                           
MICRO_AVG            0.9631         0.9355        0.9862
O.celebensis         0.9531         0.9297        1.0000
O.javanicus          0.9775         0.9438        0.9663
OVERALL              0.9653         0.9368        0.9831

F1_SCORE Comparison Across Methods:
================================================================================
method         NMS Ensemble  Single YOLOv8  WBF Ensemble
category_name                                           
MICRO_AVG            0.0264         0.1481        0.0677
O.celebensis         0.0280         0.1742        0.0715
O.javanicus          0.0245         0.1221        0.0626
OVERALL              0.0263         0.1482        0.0671

Conf 0.5:
Per-class Metrics Summary (Single YOLOv8):
============================================================
category_id category_name  true_positives  false_positives  false_negatives  ground_truth_count  precision  recall  f1_score
          1  O.celebensis              95                9               33                 128     0.9135  0.7422    0.8190
          2   O.javanicus              66               34               23                  89     0.6600  0.7416    0.6984
    OVERALL       OVERALL             161               43               56                 217     0.7867  0.7419    0.7587
  MICRO_AVG     MICRO_AVG             161               43               56                 217     0.7892  0.7419    0.7648

============================================================
Per-class Metrics Summary (NMS Ensemble):
============================================================
category_id category_name  true_positives  false_positives  false_negatives  ground_truth_count  precision  recall  f1_score
          1  O.celebensis             115               30               13                 128     0.7931  0.8984    0.8425
          2   O.javanicus              79               87               10                  89     0.4759  0.8876    0.6196
    OVERALL       OVERALL             194              117               23                 217     0.6345  0.8930    0.7310
  MICRO_AVG     MICRO_AVG             194              117               23                 217     0.6238  0.8940    0.7348

============================================================
Per-class Metrics Summary (WBF Ensemble):
============================================================
category_id category_name  true_positives  false_positives  false_negatives  ground_truth_count  precision  recall  f1_score
          1  O.celebensis              96                2               32                 128     0.9796  0.7500    0.8496
          2   O.javanicus              59                8               30                  89     0.8806  0.6629    0.7564
    OVERALL       OVERALL             155               10               62                 217     0.9301  0.7065    0.8030
  MICRO_AVG     MICRO_AVG             155               10               62                 217     0.9394  0.7143    0.8115

============================================================

================================================================================
EVALUATION RESULTS COMPARISON
================================================================================
       method  mAP_0.5:0.95  mAP_0.5  mAP_0.75  mAP_small  mAP_medium  mAP_large  mAR_1  mAR_10  mAR_100  mAR_small  mAR_medium  mAR_large
Single YOLOv8        0.4380   0.7071    0.4747    -1.0000      0.3874     0.4457 0.3971  0.4954   0.5015    -1.0000      0.4433     0.5094
 NMS Ensemble        0.5210   0.8280    0.5757    -1.0000      0.4493     0.5384 0.4347  0.5909   0.6016    -1.0000      0.4900     0.6270
 WBF Ensemble        0.4740   0.7005    0.5555    -1.0000      0.3149     0.5075 0.4108  0.5142   0.5142    -1.0000      0.3500     0.5466

PRECISION Comparison Across Methods:
================================================================================
method         NMS Ensemble  Single YOLOv8  WBF Ensemble
category_name                                           
MICRO_AVG            0.6238         0.7892        0.9394
O.celebensis         0.7931         0.9135        0.9796
O.javanicus          0.4759         0.6600        0.8806
OVERALL              0.6345         0.7867        0.9301

RECALL Comparison Across Methods:
================================================================================
method         NMS Ensemble  Single YOLOv8  WBF Ensemble
category_name                                           
MICRO_AVG            0.8940         0.7419        0.7143
O.celebensis         0.8984         0.7422        0.7500
O.javanicus          0.8876         0.7416        0.6629
OVERALL              0.8930         0.7419        0.7065

F1_SCORE Comparison Across Methods:
================================================================================
method         NMS Ensemble  Single YOLOv8  WBF Ensemble
category_name                                           
MICRO_AVG            0.7348         0.7648        0.8115
O.celebensis         0.8425         0.8190        0.8496
O.javanicus          0.6196         0.6984        0.7564
OVERALL              0.7310         0.7587        0.8030

Conf 0.6:
Per-class Metrics Summary (Single YOLOv8):
============================================================
category_id category_name  true_positives  false_positives  false_negatives  ground_truth_count  precision  recall  f1_score
          1  O.celebensis              92                8               36                 128     0.9200  0.7188    0.8070
          2   O.javanicus              66               26               23                  89     0.7174  0.7416    0.7293
    OVERALL       OVERALL             158               34               59                 217     0.8187  0.7302    0.7681
  MICRO_AVG     MICRO_AVG             158               34               59                 217     0.8229  0.7281    0.7726

============================================================
Per-class Metrics Summary (NMS Ensemble):
============================================================
category_id category_name  true_positives  false_positives  false_negatives  ground_truth_count  precision  recall  f1_score
          1  O.celebensis             114               25               14                 128     0.8201  0.8906    0.8539
          2   O.javanicus              78               62               11                  89     0.5571  0.8764    0.6812
    OVERALL       OVERALL             192               87               25                 217     0.6886  0.8835    0.7676
  MICRO_AVG     MICRO_AVG             192               87               25                 217     0.6882  0.8848    0.7742

============================================================
Per-class Metrics Summary (WBF Ensemble):
============================================================
category_id category_name  true_positives  false_positives  false_negatives  ground_truth_count  precision  recall  f1_score
          1  O.celebensis              82                2               46                 128     0.9762  0.6406    0.7736
          2   O.javanicus              55                6               34                  89     0.9016  0.6180    0.7333
    OVERALL       OVERALL             137                8               80                 217     0.9389  0.6293    0.7535
  MICRO_AVG     MICRO_AVG             137                8               80                 217     0.9448  0.6313    0.7569

============================================================

================================================================================
EVALUATION RESULTS COMPARISON
================================================================================
       method  mAP_0.5:0.95  mAP_0.5  mAP_0.75  mAP_small  mAP_medium  mAP_large  mAR_1  mAR_10  mAR_100  mAR_small  mAR_medium  mAR_large
Single YOLOv8        0.4313   0.6935    0.4675    -1.0000      0.3874     0.4391 0.3889  0.4871   0.4933    -1.0000      0.4433     0.5012
 NMS Ensemble        0.5185   0.8256    0.5726    -1.0000      0.4462     0.5364 0.4335  0.5874   0.5969    -1.0000      0.4833     0.6235
 WBF Ensemble        0.4181   0.6196    0.4868    -1.0000      0.2240     0.4646 0.3737  0.4573   0.4573    -1.0000      0.2400     0.5088

PRECISION Comparison Across Methods:
================================================================================
method         NMS Ensemble  Single YOLOv8  WBF Ensemble
category_name                                           
MICRO_AVG            0.6882         0.8229        0.9448
O.celebensis         0.8201         0.9200        0.9762
O.javanicus          0.5571         0.7174        0.9016
OVERALL              0.6886         0.8187        0.9389

RECALL Comparison Across Methods:
================================================================================
method         NMS Ensemble  Single YOLOv8  WBF Ensemble
category_name                                           
MICRO_AVG            0.8848         0.7281        0.6313
O.celebensis         0.8906         0.7188        0.6406
O.javanicus          0.8764         0.7416        0.6180
OVERALL              0.8835         0.7302        0.6293

F1_SCORE Comparison Across Methods:
================================================================================
method         NMS Ensemble  Single YOLOv8  WBF Ensemble
category_name                                           
MICRO_AVG            0.7742         0.7726        0.7569
O.celebensis         0.8539         0.8070        0.7736
O.javanicus          0.6812         0.7293        0.7333
OVERALL              0.7676         0.7681        0.7535

Conf 0.25:
============================================================
Per-class Metrics Summary (Single YOLOv8):
============================================================
category_id category_name  true_positives  false_positives  false_negatives  ground_truth_count  precision  recall  f1_score
          1  O.celebensis             104               15               24                 128     0.8739  0.8125    0.8421
          2   O.javanicus              75               59               14                  89     0.5597  0.8427    0.6726
    OVERALL       OVERALL             179               74               38                 217     0.7168  0.8276    0.7574
  MICRO_AVG     MICRO_AVG             179               74               38                 217     0.7075  0.8249    0.7617

============================================================
Per-class Metrics Summary (NMS Ensemble):
============================================================
category_id category_name  true_positives  false_positives  false_negatives  ground_truth_count  precision  recall  f1_score
          1  O.celebensis             117               58               11                 128     0.6686  0.9141    0.7723
          2   O.javanicus              82              176                7                  89     0.3178  0.9213    0.4726
    OVERALL       OVERALL             199              234               18                 217     0.4932  0.9177    0.6224
  MICRO_AVG     MICRO_AVG             199              234               18                 217     0.4596  0.9171    0.6123

============================================================
Per-class Metrics Summary (WBF Ensemble):
============================================================
category_id category_name  true_positives  false_positives  false_negatives  ground_truth_count  precision  recall  f1_score
          1  O.celebensis             114                6               14                 128     0.9500  0.8906    0.9194
          2   O.javanicus              74               36               15                  89     0.6727  0.8315    0.7437
    OVERALL       OVERALL             188               42               29                 217     0.8114  0.8610    0.8315
  MICRO_AVG     MICRO_AVG             188               42               29                 217     0.8174  0.8664    0.8412

============================================================

================================================================================
EVALUATION RESULTS COMPARISON
================================================================================
       method  mAP_0.5:0.95  mAP_0.5  mAP_0.75  mAP_small  mAP_medium  mAP_large  mAR_1  mAR_10  mAR_100  mAR_small  mAR_medium  mAR_large
Single YOLOv8        0.4729   0.7678    0.5201    -1.0000      0.3874     0.4865 0.4227  0.5519   0.5580    -1.0000      0.4433     0.5813
 NMS Ensemble        0.5300   0.8444    0.5871    -1.0000      0.4691     0.5437 0.4347  0.6032   0.6206    -1.0000      0.5467     0.6373
 WBF Ensemble        0.5460   0.8317    0.6255    -1.0000      0.4109     0.5738 0.4599  0.6020   0.6043    -1.0000      0.4633     0.6324

PRECISION Comparison Across Methods:
================================================================================
method         NMS Ensemble  Single YOLOv8  WBF Ensemble
category_name                                           
MICRO_AVG            0.4596         0.7075        0.8174
O.celebensis         0.6686         0.8739        0.9500
O.javanicus          0.3178         0.5597        0.6727
OVERALL              0.4932         0.7168        0.8114

RECALL Comparison Across Methods:
================================================================================
method         NMS Ensemble  Single YOLOv8  WBF Ensemble
category_name                                           
MICRO_AVG            0.9171         0.8249        0.8664
O.celebensis         0.9141         0.8125        0.8906
O.javanicus          0.9213         0.8427        0.8315
OVERALL              0.9177         0.8276        0.8610

F1_SCORE Comparison Across Methods:
================================================================================
method         NMS Ensemble  Single YOLOv8  WBF Ensemble
category_name                                           
MICRO_AVG            0.6123         0.7617        0.8412
O.celebensis         0.7723         0.8421        0.9194
O.javanicus          0.4726         0.6726        0.7437
OVERALL              0.6224         0.7574        0.8315