# Bioinformatics Algorithms

This repository contains a collection of bioinformatics algorithms implemented in Python. These algorithms were developed as part of the Bioinformatics Algorithms course at BYU.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Algorithms](#algorithms)

## Installation

To run the code in this repository, you will need to have Python 3 installed. You can then install the dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Usage

The Python scripts for each algorithm are located in the `src` directory. You can run each script directly from the command line. For example, to run the Burrows-Wheeler Transform algorithm, you can use the following command:

```bash
python src/burrows_wheeler_transform.py
```

The Jupyter notebooks in the `notebooks` directory provide a more interactive way to explore the algorithms.

## Testing

Unit tests for the algorithms are located in the `tests` directory. You can run all the tests using the following command:

```bash
python -m unittest discover tests
```

## Algorithms

The following is a list of the algorithms included in this repository:

*   **Better BWT Matching:** An improved version of the BWT matching algorithm.
*   **Burrows-Wheeler Transform:** A data compression algorithm that rearranges a string to make it more compressible.
*   **BWT Matching:** A pattern matching algorithm that uses the Burrows-Wheeler Transform.
*   **Calculate GC Content:** A simple algorithm to calculate the percentage of Guanine (G) and Cytosine (C) bases in a DNA sequence.
*   **De Bruijn Graph from String:** An algorithm to construct a De Bruijn graph from a given string.
*   **Frequent Words with Mismatches and Reverse Complements:** An algorithm to find the most frequent k-mers with mismatches and their reverse complements.
*   **Frequent Words with Mismatches:** An algorithm to find the most frequent k-mers with at most d mismatches in a string.
*   **Gibbs Sampler:** A randomized algorithm for motif finding.
*   **Global Alignment:** An algorithm to find the optimal alignment between two sequences.
*   **Greedy Motif Search:** A greedy algorithm for motif finding.
*   **Greedy Motif Search with Pseudocounts:** A greedy algorithm for motif finding that uses pseudocounts to avoid zero probabilities.
*   **Inverse Burrows-Wheeler Transform:** An algorithm to reverse the Burrows-Wheeler Transform.
*   **Local Alignment:** An algorithm to find the best local alignment between two sequences.
*   **Longest Common Subsequence:** An algorithm to find the longest common subsequence between two sequences.
*   **Minimum Skew:** An algorithm to find the position in a genome where the skew between G and C is minimized.
*   **Multiple Pattern Matching:** An algorithm to find all occurrences of a set of patterns in a text.
*   **Nearest Neighbors Tree:** An algorithm to construct a nearest neighbors tree.
*   **Neighbor Joining:** A bottom-up clustering method for the creation of phylogenetic trees.
*   **Neighbors:** A function to generate the d-neighborhood of a string.
*   **Outcome Likelihood:** An algorithm to calculate the likelihood of an outcome given a hidden path in an HMM.
*   **Probability of Hidden Path:** An algorithm to calculate the probability of a hidden path in an HMM.
*   **Probability of Outcome Given Hidden Path:** An algorithm to calculate the probability of an outcome given a hidden path in an HMM.
*   **Profile HMM:** An algorithm to construct a profile HMM from a multiple alignment.
*   **Profile Most Probable k-mer:** An algorithm to find the most probable k-mer in a string, given a profile matrix.
*   **Reverse Complement:** An algorithm to find the reverse complement of a DNA string.
*   **Small Parsimony:** An algorithm to find the most parsimonious evolutionary tree for a set of sequences.
*   **String Reconstruction:** An algorithm to reconstruct a string from its k-mer composition.
*   **String Reconstruction from Read Pairs:** An algorithm to reconstruct a string from a set of read pairs.
*   **Suffix Array:** An algorithm to create a suffix array for a string.
*   **Suffix Array Construction:** An algorithm to construct a suffix array.
*   **Trie Construction:** An algorithm to construct a trie from a set of patterns.
*   **Viterbi Algorithm:** An algorithm to find the most likely sequence of hidden states in an HMM.
