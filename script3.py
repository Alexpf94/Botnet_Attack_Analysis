import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score

folder = r"C:\Users\alex_\OneDrive\Bureau\Adelaide Uni\Security Principle\Research Project\scenario10.binetflow"
cols = ["Dur", "TotPkts", "TotBytes", "SrcBytes"]

s10 = pd.read_csv(folder + r"\scenario10.csv")
s9  = pd.read_csv(folder + r"\scenario9.csv")
for d in (s10, s9):
    d["answer"] = d["Label"].str.contains("botnet", case=False, na=False).astype(int)

# two families into one table
both = pd.concat([s10[cols + ["answer"]], s9[cols + ["answer"]]], ignore_index=True)
both[cols] = both[cols].fillna(0)

X_train, X_test, y_train, y_test = train_test_split(
    both[cols], both["answer"], test_size=0.30, random_state=42, stratify=both["answer"])

model = RandomForestClassifier(n_jobs=-1)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Accuracy:", round(100*accuracy_score(y_test, pred), 2), "%")
print("Recall (botnets caught):", round(100*recall_score(y_test, pred), 2), "%")
print("Baseline (all-normal):", round(100*(1-y_test.mean()), 2), "%")