# ML Algorithms

Machine-learning implementations spanning regression, classification, clustering, neural networks, and computer vision.

Python notebooks and source are organized by method, with dependency guidance, attribution, and repository validation.

## Contents

| Area | Implementations |
|---|---|
| Fundamentals | [Entropy calculation](fundamentals/entropy) and a [neural network implementation](neural-networks/from-scratch) |
| Supervised learning | [Linear regression](supervised-learning/linear-regression), [automobile regression](supervised-learning/automobile-regression), [Titanic classification](supervised-learning/titanic-classification), and [KNN on Abalone](supervised-learning/abalone-knn) |
| Unsupervised learning | K-means clustering on [Iris](unsupervised-learning/iris-k-means) and [Abalone](unsupervised-learning/abalone-k-means) |
| Computer vision | [Multi-label image classification](computer-vision/multi-label-classification) and CS231n [KNN](computer-vision/cs231n/knn), [SVM](computer-vision/cs231n/svm), and [Softmax](computer-vision/cs231n/softmax) implementations on CIFAR-10 |

## Data policy

Large third-party datasets are not committed to this repository. Dataset download instructions or scripts are provided where available. The three CS231n modules exclude roughly 500 MB of duplicated CIFAR-10 binaries.

## Environment

The notebooks have different dependency requirements. A shared starting environment is provided:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter lab
```

Individual notebooks may require compatibility adjustments with newer library versions.

## Attribution

The CS231n implementations build on upstream scaffolding distributed under the license retained in each directory. Attribution for the upstream code is documented alongside the implementation work.

## Provenance and licensing

See [PROVENANCE.md](PROVENANCE.md) for source history and licensing. Existing component licenses are retained; no blanket license is applied to code that previously had no declared license.
