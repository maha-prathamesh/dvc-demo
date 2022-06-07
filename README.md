conda activate mlops
pip install -r requirements.txt



git init
dvc init
dvc add .\data_given\winequality.csv

git add .
git commit -m "first commit"

git remote add origin https://github.com/maha-prathamesh/dvc-demo
git branch -M main