``` bash
conda activate mlops
pip install -r requirements.txt
```
``` bash
git init
dvc init
dvc add .\data_given\winequality.csv
```

``` bash
git add .
git commit -m "first commit"

git remote add origin https://github.com/maha-prathamesh/dvc-demo
git branch -M main
```