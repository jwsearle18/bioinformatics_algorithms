# Bioinformatics Algorithms

This repository contains a collection of bioinformatics algorithms implemented in Python. These algorithms were implemented as part of the Bioinformatics Algorithms course on Coursera.

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Algorithms](#algorithms)
  * [Lesson 1: Introduction to Bioinformatics](#lesson-1-introduction-to-bioinformatics)
  * [Lesson 2: Motif Finding](#lesson-2-motif-finding)
  * [Lesson 3: Genome Assembly](#lesson-3-genome-assembly)
  * [Lesson 4: Sequence Alignment](#lesson-4-sequence-alignment)
  * [Lesson 5: Phylogenetic Trees](#lesson-5-phylogenetic-trees)
  * [Lesson 6: Burrows-Wheeler Transform and Suffix Arrays](#lesson-6-burrows-wheeler-transform-and-suffix-arrays)
  * [Lesson 7: Hidden Markov Models](#lesson-7-hidden-markov-models)
* [Testing](#testing)

## Installation

To run the code in this repository, you will need to have Python 3 installed. You will also need to install the following dependencies:

```
pip install -r requirements.txt
```

## Usage

Each of the Python files in the `src` directory can be run from the command line. For example, to run the `frequent_words_with_mismatches.py` file, you would use the following command:

```
python src/lesson_1/frequent_words_with_mismatches.py
```

## Algorithms

### Lesson 1: Introduction to Bioinformatics

* `frequent_words_with_mismatches.py`: Finds the most frequent k-mers with mismatches in a string.
* `frequent_words_with_mismatches_and_reverse_complements.py`: Finds the most frequent k-mers with mismatches and reverse complements in a string.
* `minimum_skew.py`: Finds the minimum skew of a DNA string.
* `neighbors.py`: Finds all neighbors of a string with at most d mismatches.
* `reverse_complement.py`: Finds the reverse complement of a DNA string.

### Lesson 2: Motif Finding

* `greedy_motif_search.py`: Finds the best motifs in a list of DNA strings using a greedy algorithm.
* `greedy_motif_search_with_pseudocounts.py`: Finds the best motifs in a list of DNA strings using a greedy algorithm with pseudocounts.
* `profile_most_probable_kmer.py`: Finds the most probable k-mer in a string, given a profile.
* `gibbs_sampler.py`: Finds the best motifs in a list of DNA strings using the Gibbs sampler algorithm.

### Lesson 3: Genome Assembly

* `de_bruijn_string.py`: Constructs a de Bruijn graph from a string.
* `string_reconstruction.py`: Reconstructs a string from its k-mer composition.
* `string_reconstruction_from_read_pairs.py`: Reconstructs a string from a collection of read-pairs.

### Lesson 4: Sequence Alignment

* `global_alignment.py`: Performs a global alignment of two strings.
* `local_alignment.py`: Performs a local alignment of two strings.
* `longest_common_subsequence.py`: Finds the longest common subsequence of two strings.

### Lesson 5: Phylogenetic Trees

* `nearest_neighbors_tree.py`: Finds the nearest neighbors of a tree.
* `neighbor_joining.py`: Implements the neighbor joining algorithm.
* `small_parsimony.py`: Implements the small parsimony algorithm.

### Lesson 6: Burrows-Wheeler Transform and Suffix Arrays

* `better_burrows_wheeler_matching.py`: Matches patterns in a string using the better Burrows-Wheeler matching algorithm.
* `burrows_wheeler_transform.py`: Computes the Burrows-Wheeler transform of a string.
* `burrows_wheeler_matching.py`: Matches patterns in a string using the Burrows-Wheeler matching algorithm.
* `inverse_burrows_wheeler_transform.py`: Computes the inverse Burrows-Wheeler transform of a string.
* `suffix_array.py`: Constructs the suffix array of a string.
* `suffix_array_construction.py`: Constructs the suffix array of a string.
* `trie_construction.py`: Constructs a trie from a list of patterns.

### Lesson 7: Hidden Markov Models

* `outcome_likelihood.py`: Calculates the likelihood of an outcome given a hidden Markov model.
* `probability_of_a_hidden_path.py`: Calculates the probability of a hidden path in a hidden Markov model.
* `probability_of_an_outcome_given_a_hidden_path.py`: Calculates the probability of an outcome given a hidden path in a hidden Markov model.
* `profile_hmm.py`: Constructs a profile HMM from a multiple alignment.
* `viterbi_algorithm.py`: Implements the Viterbi algorithm.

## Testing

To run the tests, you can use the following command:

```
python tests/test.py
```