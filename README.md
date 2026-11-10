# Botnet_Attack_Analysis
Testing how well machine learning really detects DDOS botnet attacks
As part of ADELAIDE UNIVERSITY / Security Principles Research Project
Critical analysis and reproduction of : https://inass.org/wp-content/uploads/2022/05/2022083148-2.pdf
## What is it ? 
Just a Random Forest Detector built (around 20 lines) to test the paper's main claim that : 
- Flow features can detect 99.99% of botnet activity
## The three experiments
| Script | Experiment | Result |
|--------|-----------|--------|
| `script.py`  | Reproduce the claim (train + test on scenario 10, Rbot) | 99.98% accuracy |
| `script2.py` | Train on Rbot, test on an unseen family (scenario 9, Neris) | recall 0.02% (fails) |
| `script3.py` | Train on both families mixed | recall ~86% (fixed) |
## Main finding
Accuracy is misleading. It works good for one type of botnet attack but a trained model is failing with another botnet acting differently.
Mixing families during model training fixes it but dilutes the recall. 
## Data
Not included (large files). Download from the CTU-13 dataset:
Rbot and Neris are different two different botnet
- Scenario 10 (Rbot): https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-51/
- Scenario 9 (Neris): https://mcfp.felk.cvut.cz/publicDatasets/CTU-Malware-Capture-Botnet-50/
## How to run
```
pip install pandas scikit-learn
python script.py
```
Do not forget to change the file path at the top of each script to point to your downloaded data or it is not going to work =)

