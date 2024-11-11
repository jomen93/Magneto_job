import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed

class MutantDetectorService:

    def __init__(self):
        self.mutant_sequence_length = 4

    def is_mutant(self, dna: list[str]) -> bool:

        dna_matrix = np.array([list(row) for row in dna])

        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self._has_horizontal_sequence, dna_matrix),
                executor.submit(self._has_vertical_sequence, dna_matrix),
                executor.submit(self._has_diagonal_sequence, dna_matrix),
                executor.submit(self._has_antidiagonal_sequence, dna_matrix)
            ]

            for future in as_completed(futures):
                if future.result():
                    return True
        return False

    def _has_horizontal_sequence(self, dna_matrix: np.ndarray) -> bool:

        for row in dna_matrix:
            if self._has_consecutive_letters(row):
                return True
        return False

    def _has_vertical_sequence(self, dna_matrix: np.ndarray) -> bool:

        for col in dna_matrix.T:
            if self._has_consecutive_letters(col):
                return True
        return False

    def _has_diagonal_sequence(self, dna_matrix: np.ndarray) -> bool:

        for offset in range(-dna_matrix.shape[0] + 4, dna_matrix.shape[1] - 3):
            diag = dna_matrix.diagonal(offset)
            if len(diag) >= 4 and self._has_consecutive_letters(diag):
                return True
        return False

    def _has_antidiagonal_sequence(self, dna_matrix: np.ndarray) -> bool:

        flip_matrix = np.fliplr(dna_matrix)
        for offset in range(-flip_matrix.shape[0] + 4, flip_matrix.shape[1] - 3):
            antidiag = flip_matrix.diagonal(offset)
            if len(antidiag) >= 4 and self._has_consecutive_letters(antidiag):
                return True
        return False

    def _has_consecutive_letters(self, sequence: np.ndarray) -> bool:

        count = 1
        for i in range(1, len(sequence)):
            if sequence[i] == sequence[i-1]:
                count += 1
                if count == 4:
                    return True
            else:
                count = 1
        return False
