# learningsphinx

Nothing to see here. This is just a test repository for Ben to learn sphinx and to experiment without breaking docs in a real, in-production, package.

---

## Local development

1. Create a new environment using Python >=3.8, for example 3.10

```
conda create --name learning-sphinx python=3.10
```

2. Activate environment:

```
conda activate learning-sphinx
```


3. Install development dependencies

```
pip install -r requirements-docs.txt
```

4. Optional: You may have to run the following command to make Jupyter Lab aware of the environment.

```
python -m ipykernel install --user --name learning-sphinx
```