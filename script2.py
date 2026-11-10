import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score

folder = r"C:\Users\alex_\OneDrive\Bureau\Adelaide Uni\Security Principle\Research Project\scenario10.binetflow"
cols = ["Dur", "TotPkts", "TotBytes", "SrcBytes"]

# TRAIN on scenario 10 (Rbot)
train = pd.read_csv(folder + r"\scenario10.csv")
train["answer"] = train["Label"].str.contains("botnet", case=False, na=False).astype(int)
model = RandomForestClassifier(n_jobs=-1)
model.fit(train[cols].fillna(0), train["answer"])

# TEST on scenario 9 not familiar wiht (Neris) 
test = pd.read_csv(folder + r"\scenario9.csv")
test["answer"] = test["Label"].str.contains("botnet", case=False, na=False).astype(int)
pred = model.predict(test[cols].fillna(0))

print("Accuracy:", round(100*accuracy_score(test["answer"], pred), 2), "%")
print("Recall (botnets caught):", round(100*recall_score(test["answer"], pred), 2), "%")
print("Baseline (all-normal):", round(100*(1-test["answer"].mean()), 2), "%")