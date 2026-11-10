import pandas as pd                                          # table tool (like Excel)
from sklearn.ensemble import RandomForestClassifier          # the model
from sklearn.model_selection import train_test_split         # the splitter

df = pd.read_csv(r"C:\Users\alex_\OneDrive\Bureau\Adelaide Uni\Security Principle\Research Project\scenario10.binetflow\scenario10.csv")   # 1. load the data

df["answer"] = df["Label"].str.contains("botnet", case=False).astype(int)   # 2. new column: 1 if botnet, else 0

clues  = df[["Dur","TotPkts","TotBytes","SrcBytes"]].fillna(0)  # 3a. the clues (4 number columns)
answer = df["answer"]                                           # 3b. the answer (botnet yes/no)

# 4. hide 30% for testing, keep 70% for learning
clues_train, clues_test, answer_train, answer_test = train_test_split(
    clues, answer, test_size=0.30, random_state=42)

model = RandomForestClassifier(n_jobs=-1)      # 5a. create the model
model.fit(clues_train, answer_train)           # 5b. LEARN from the 70%
score = model.score(clues_test, answer_test)   # 5c. TEST on the hidden 30%

print("The model is", round(100*score, 2), "% accurate")   # show the result