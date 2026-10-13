# Machine Learning Foundations

A curated collection of foundational machine-learning implementations and experiments spanning regression, classification, clustering, neural networks, and computer vision.

These projects document my learning progression. The implementations and notebooks remain close to their original form; the collection improves organization, attribution, dependency guidance, and repository hygiene.

## Contents

| Area | Exercises |
|---|---|
| Fundamentals | [Entropy calculation](fundamentals/entropy) and a [neural network implementation](neural-networks/from-scratch) |
| Supervised learning | [Linear regression](supervised-learning/linear-regression), [automobile regression](supervised-learning/automobile-regression), [Titanic classification](supervised-learning/titanic-classification), and [KNN on Abalone](supervised-learning/abalone-knn) |
| Unsupervised learning | K-means clustering on [Iris](unsupervised-learning/iris-k-means) and [Abalone](unsupervised-learning/abalone-k-means) |
| Computer vision | [Multi-label image classification](computer-vision/multi-label-classification) and CS231n [KNN](computer-vision/cs231n/knn), [SVM](computer-vision/cs231n/svm), and [Softmax](computer-vision/cs231n/softmax) exercises on CIFAR-10 |

## Data policy

Large third-party datasets are not committed to this repository. Dataset download instructions or scripts are retained where available. The three CS231n exercises exclude the roughly 500 MB of duplicated CIFAR-10 binaries present in their original repositories.

## Environment

The collection uses Python notebooks from different stages of learning, so dependency requirements vary by exercise. A shared starting environment is provided:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab
```

Individual notebooks may require small compatibility adjustments when run with newer library versions; their original implementation cells have not been rewritten during consolidation.

## Attribution

The CS231n exercises build on course scaffolding distributed under the license retained in each exercise directory. My notebooks and completed implementation work are presented alongside that attribution rather than as wholly original course infrastructure.

## Provenance and licensing

See [PROVENANCE.md](PROVENANCE.md). Original per-project license files are retained. No blanket license is applied to projects that previously had no declared license.
