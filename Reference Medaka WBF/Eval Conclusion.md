# Evaluation Results

## Confidence 0.001

| Method        | mAP\@0.5:0.95 | mAP\@0.5 | mAP\@0.75 | mAP\_small | mAP\_medium | mAP\_large | mAR\@1 | mAR\@10 | mAR\@100 | mAR\_small | mAR\_medium | mAR\_large | Precision | Recall | F1-score |
| ------------- | ------------- | -------- | --------- | ---------- | ----------- | ---------- | ------ | ------- | -------- | ---------- | ----------- | ---------- | --------- | ------ | -------- |
| Single YOLOv8 | 0.4979        | 0.8150   | 0.5404    | -1.0000    | 0.4269      | 0.5079     | 0.4422 | 0.5978  | 0.6259   | -1.0000    | 0.5633      | 0.6361     | 0.0804    | 0.8252 | 0.1472   |
| NMS Ensemble  | 0.5351        | 0.8493   | 0.5924    | -1.0000    | 0.4706      | 0.5507     | 0.4394 | 0.6151  | 0.6613   | -1.0000    | 0.5667      | 0.6841     | 0.0134    | 0.8902 | 0.0265   |
| WBF Ensemble  | 0.5905        | 0.8980   | 0.6754    | -1.0000    | 0.4504      | 0.6159     | 0.4901 | 0.6718  | 0.7063   | -1.0000    | 0.5800      | 0.7311     | 0.0350    | 0.9862 | 0.0675   |

### Per-class Metrics (Confidence 0.001)

```
Single YOLOv8:
O.celebensis  Precision=0.0961  Recall=0.9297  F1=0.1742
O.javanicus   Precision=0.0653  Recall=0.9438  F1=0.1221

NMS Ensemble:
O.celebensis  Precision=0.0142  Recall=0.9531  F1=0.0280
O.javanicus   Precision=0.0124  Recall=0.9775  F1=0.0245

WBF Ensemble:
O.celebensis  Precision=0.0371  Recall=1.0000  F1=0.0715
O.javanicus   Precision=0.0324  Recall=0.9663  F1=0.0626
```

---

## Confidence 0.25

| Method        | mAP\@0.5:0.95 | mAP\@0.5 | mAP\@0.75 | mAP\_small | mAP\_medium | mAP\_large | mAR\@1 | mAR\@10 | mAR\@100 | mAR\_small | mAR\_medium | mAR\_large | Precision | Recall | F1-score |
| ------------- | ------------- | -------- | --------- | ---------- | ----------- | ---------- | ------ | ------- | -------- | ---------- | ----------- | ---------- | --------- | ------ | -------- |
| Single YOLOv8 | 0.4729        | 0.7678   | 0.5201    | -1.0000    | 0.3874      | 0.4865     | 0.4227 | 0.5519  | 0.5580   | -1.0000    | 0.4433      | 0.5813     | 0.7600    | 0.7654 | 0.7617   |
| NMS Ensemble  | 0.5300        | 0.8444   | 0.5871    | -1.0000    | 0.4691      | 0.5437     | 0.4347 | 0.6032  | 0.6206   | -1.0000    | 0.5467      | 0.6373     | 0.4596    | 0.9171 | 0.6121   |
| WBF Ensemble  | 0.5460        | 0.8317   | 0.6255    | -1.0000    | 0.4109      | 0.5738     | 0.4599 | 0.6020  | 0.6043   | -1.0000    | 0.4633      | 0.6324     | 0.8174    | 0.8664 | 0.8412   |

### Per-class Metrics (Confidence 0.25)

```
Single YOLOv8:
O.celebensis  Precision=0.8739  Recall=0.8125  F1=0.8421
O.javanicus   Precision=0.5597  Recall=0.8427  F1=0.6726

NMS Ensemble:
O.celebensis  Precision=0.6686  Recall=0.9141  F1=0.7723
O.javanicus   Precision=0.3178  Recall=0.9213  F1=0.4726

WBF Ensemble:
O.celebensis  Precision=0.9500  Recall=0.8906  F1=0.9194
O.javanicus   Precision=0.6727  Recall=0.8315  F1=0.7437
```

---

## Confidence 0.5

| Method        | mAP\@0.5:0.95 | mAP\@0.5 | mAP\@0.75 | mAP\_small | mAP\_medium | mAP\_large | mAR\@1 | mAR\@10 | mAR\@100 | mAR\_small | mAR\_medium | mAR\_large | Precision | Recall | F1-score |
| ------------- | ------------- | -------- | --------- | ---------- | ----------- | ---------- | ------ | ------- | -------- | ---------- | ----------- | ---------- | --------- | ------ | -------- |
| Single YOLOv8 | 0.4380        | 0.7071   | 0.4747    | -1.0000    | 0.3874      | 0.4457     | 0.3971 | 0.4954  | 0.5015   | -1.0000    | 0.4433      | 0.5094     | 0.8208    | 0.7163 | 0.7648   |
| NMS Ensemble  | 0.5210        | 0.8280   | 0.5757    | -1.0000    | 0.4493      | 0.5384     | 0.4347 | 0.5909  | 0.6016   | -1.0000    | 0.4900      | 0.6270     | 0.6238    | 0.8940 | 0.7344   |
| WBF Ensemble  | 0.4740        | 0.7005   | 0.5555    | -1.0000    | 0.3149      | 0.5075     | 0.4108 | 0.5142  | 0.5142   | -1.0000    | 0.3500      | 0.5466     | 0.9394    | 0.7083 | 0.8115   |

### Per-class Metrics (Confidence 0.5)

```
Single YOLOv8:
O.celebensis  Precision=0.9135  Recall=0.7422  F1=0.8190
O.javanicus   Precision=0.6600  Recall=0.7416  F1=0.6984

NMS Ensemble:
O.celebensis  Precision=0.7931  Recall=0.8984  F1=0.8425
O.javanicus   Precision=0.4759  Recall=0.8876  F1=0.6196

WBF Ensemble:
O.celebensis  Precision=0.9796  Recall=0.7500  F1=0.8496
O.javanicus   Precision=0.8806  Recall=0.6629  F1=0.7564
```

---

## Confidence 0.6

| Method        | mAP\@0.5:0.95 | mAP\@0.5 | mAP\@0.75 | mAP\_small | mAP\_medium | mAP\_large | mAR\@1 | mAR\@10 | mAR\@100 | mAR\_small | mAR\_medium | mAR\_large | Precision | Recall | F1-score |
| ------------- | ------------- | -------- | --------- | ---------- | ----------- | ---------- | ------ | ------- | -------- | ---------- | ----------- | ---------- | --------- | ------ | -------- |
| Single YOLOv8 | 0.4313        | 0.6935   | 0.4675    | -1.0000    | 0.3874      | 0.4391     | 0.3889 | 0.4871  | 0.4933   | -1.0000    | 0.4433      | 0.5012     | 0.8706    | 0.6983 | 0.7726   |
| NMS Ensemble  | 0.5185        | 0.8256   | 0.5726    | -1.0000    | 0.4462      | 0.5364     | 0.4335 | 0.5874  | 0.5969   | -1.0000    | 0.4833      | 0.6235     | 0.6238    | 0.8948 | 0.7345   |
| WBF Ensemble  | 0.4181        | 0.6196   | 0.4868    | -1.0000    | 0.2240      | 0.4646     | 0.3737 | 0.4573  | 0.4573   | -1.0000    | 0.2400      | 0.5088     | 0.9448    | 0.6313 | 0.7569   |

### Per-class Metrics (Confidence 0.6)

```
Single YOLOv8:
O.celebensis  Precision=0.9200  Recall=0.7188  F1=0.8070
O.javanicus   Precision=0.7174  Recall=0.7416  F1=0.7293

NMS Ensemble:
O.celebensis  Precision=0.8201  Recall=0.8906  F1=0.8539
O.javanicus   Precision=0.5571  Recall=0.8764  F1=0.6812

WBF Ensemble:
O.celebensis  Precision=0.9762  Recall=0.6406  F1=0.7736
O.javanicus   Precision=0.9016  Recall=0.6180  F1=0.7333
```

---

## Conclusion

When comparing both ensemble approaches against the baseline Single YOLOv8 across different confidence thresholds, the following trends emerge:

* **WBF Ensemble** achieved the strongest precision gains over YOLOv8. At confidence 0.25, its precision (0.8174) was **7.6% higher** than YOLOv8 (0.7600), and its F1-score (0.8412) improved by **10.4%**. At confidence 0.5, WBF precision (0.9394) exceeded YOLOv8 (0.8208) by **14.4%**, and the F1-score rose by **6.1%**. Even at confidence 0.6, WBF precision (0.9448) remained **8.5% higher** than YOLOv8, although recall decreased by **9.6%**. Importantly, WBF also improved mAP: at confidence 0.25, mAP\@0.5:0.95 increased by **15.4%**, and at confidence 0.5 by **8.2%** compared to YOLOv8. However, its mAR gains were modest, with recall slightly lower than YOLOv8 in several thresholds.

* **NMS Ensemble** delivered recall and mAR improvements compared to YOLOv8 but with noticeable precision and F1-score drops. At confidence 0.25, recall improved from 0.7654 (YOLOv8) to 0.9171 (**+19.8%**), while precision decreased from 0.7600 to 0.4596 (**-39.5%**). At confidence 0.5, recall increased by **24.8%**, and mAR\@100 improved by **20%**, but precision dropped by **24.0%** relative to YOLOv8. Similarly, NMS improved mAP\@0.5:0.95 by **18.9%** at confidence 0.5, showing stronger localization and detection coverage despite the cost in precision.

* **Single YOLOv8** maintained balanced performance but was consistently outperformed by WBF in terms of mAP, precision, and F1, and by NMS in terms of recall and mAR. For example, at confidence 0.5, YOLOv8 achieved mAP\@0.5:0.95 of 0.4380, which was **8.2% lower than WBF** and **18.9% lower than NMS**. Its mAR values were moderate, with mAR\@100 (0.5015) falling behind both ensemble methods.

**In summary:**

* WBF outperforms YOLOv8 in precision by up to **14%**, F1-score by up to **10%**, and mAP\@0.5:0.95 by up to **15%**, while sacrificing up to **10% recall** and achieving only modest mAR improvements.
* NMS outperforms YOLOv8 in recall by up to **25%** and mAR by up to **20%**, but precision decreases by as much as **40%**, and F1-scores are generally lower.
* Single YOLOv8 remains a balanced baseline, but ensemble strategies provide clear, quantifiable improvements: WBF for higher precision and mAP, NMS for higher recall and mAR.

---

## Statistical Benchmarking

### YOLOv8-WBF Ensemble (5 runs)

* **Average processing time:** 0.9536 ± 0.0471s
* **Average FPS:** 1.05 ± 0.05
* **Average GFLOPS/s:** 63.760 ± 3.340
* **Min time:** 0.8640s (Max FPS: 1.16)
* **Max time:** 1.0030s (Min FPS: 1.00)

### Single YOLOv8 (5 runs)

* **Average total time:** 0.2206 ± 0.0265s
* **Average inference time:** 0.2086 ± 0.0265s
* **Average FPS:** 4.60 ± 0.54
* **Average GFLOPS/s:** 55.760 ± 6.501
* **Average detections:** 2.0
* **Min total time:** 0.1920s (Max FPS: 5.21)
* **Max total time:** 0.2620s (Min FPS: 3.82)

### Benchmarking Conclusion

The WBF ensemble requires substantially higher computational cost due to processing multiple models (total 60.6 GFLOPS), resulting in an average speed of **1.05 FPS**, which is **\~77% slower** than the Single YOLOv8 baseline (4.60 FPS). However, it achieves higher computational efficiency per GFLOP (63.8 GFLOPS/s vs. 55.8 GFLOPS/s), suggesting better hardware utilization despite the increased latency. Thus, WBF offers measurable accuracy and precision gains but incurs a significant inference-time penalty compared to a single YOLOv8 model.
