#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2022-2024 SATURN
# AUTHORS:
# Sukbong Kwon (Galois)


import json
import pandas as pd
import editdistance as ed
import numpy as np
from pathlib import Path
from typing import Text, Dict, Tuple
from pydantic import BaseModel


class ScoringConfig(BaseModel):
    data: Dict = {}
    threshold: float = 0.4


class Scoring(ScoringConfig):
    def __init__(
        self,
        codebook: Text,
    )-> None:
        """Scoring the sentence with target words in the sentence

        """
        super().__init__()

        # Load codebook
        df = pd.read_csv(codebook, sep='\t')
        self.data = df.set_index("word")["score"].to_dict()

    def __call__(
        self,
        sentence: Text,
    )-> Dict:
        """Scoring the sentence with target words in the sentence

        Parameters
        ----------
        sentence : Text

        Returns
        -------
        float
            Score of the sentence
        """
        words = sentence.split()
        matched_words = []
        mathced_distance = []
        mathced_scores = []
        for word in sentence.split():
            best, distance, score = self.find_best(word)
            matched_words.append(best)
            mathced_distance.append(distance)
            mathced_scores.append(score)

        # Cancatenate the matched words and scores
        result = {}
        for word, best, distance, score in zip(words, matched_words, mathced_distance, mathced_scores):
            result[word] = {"best_word": best, "distance": str(distance), "score": str(score)}

        # Compute the final score
        final_score = 0.0
        for distance, score in zip(mathced_distance, mathced_scores):
            final_score += distance * score
        result["final_score"] = round(final_score,2)

        return result

    def find_best(
        self,
        word: Text,
    )-> Tuple[Text, float, float]:
        """Find the best word from the codebook

        Parameters
        ----------
        word : Text

        Returns
        -------
        Text
            Best word
        """
        best_word = ""
        best_distance = 1
        best_score = 0.0

        # best_distance is 0 in editdistance
        for key, value in self.data.items():
            distance = ed.eval(word, key) / len(key)
            if distance < best_distance:
                best_word = key
                best_distance = distance
                best_score = value

        if best_distance > self.threshold:
            return "", 0.0, 0.0

        return best_word, (1.0 - best_distance), best_score

    def get_statistics(
        self,
    )-> Dict
        """Get the statistics of the codebook

        Returns
        -------
        Dict
            Statistics of the codebook
        """
        statistics = {
            "mean": np.mean(list(self.data.values())),
            "std": np.std(list(self.data.values())),
            "min": np.min(list(self.data.values())),
            "max": np.max(list(self.data.values())),
        }

        return statistics


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Scoring the sentence with target words in the sentence')

    parser.add_argument(
        'sentence',
        type=str,
        help='Sentence',
    )

    parser.add_argument(
        '-c',
        '--codebook',
        type=str,
        default='data/emotion_codebook.tsv',
        help='Codebook file for scoring',
    )

    parser.add_argument(
        '-th',
        '--threshold',
        type=float,
        default=0.4,
        help='Threshold for scoring',
    )
    args = parser.parse_args()


    app = Scoring(
        codebook=args.codebook,
    )

    result = app(
        sentence=args.sentence,
    )
    print(result)

    statistics = app.get_statistics()
    print (statistics)
    print(json.dump(statistics, open("data/statistics.json", "w")))



if __name__ == "__main__":
    main()