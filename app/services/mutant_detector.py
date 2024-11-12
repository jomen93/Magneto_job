import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
from sqlalchemy.orm import Session
from app.models.dna_sequence import DNASequence


class MutantDetectorService:

    def __init__(self, db: Session):
        self.db = db
        self.mutant_sequence_length = 4

    def is_mutant(self, dna: list[str]) -> bool:

        dna_matrix = np.array([list(row) for row in dna])
        sequence_length = len(dna_matrix)

        mutant_patterns = []
        human_patterns = []

        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self._has_horizontal_sequence, dna_matrix, mutant_patterns, human_patterns),
                executor.submit(self._has_vertical_sequence, dna_matrix, mutant_patterns, human_patterns),
                executor.submit(self._has_diagonal_sequence, dna_matrix, mutant_patterns, human_patterns),
                executor.submit(self._has_antidiagonal_sequence, dna_matrix, mutant_patterns, human_patterns)
            ]

            is_mutant = any(future.result() for future in as_completed(futures))
        
        dna_entry = DNASequence(
            sequence=dna_matrix,
            is_mutant=is_mutant,
            sequence_length=sequence_length,
            mutant_sequence_count=len(mutant_patterns),
            human_sequence_count=len(human_patterns),
            detected_patterns=mutant_patterns if is_mutant else None
        )

        self.db.add(dna_entry)
        self.db.commit()

        return is_mutant



    def _has_horizontal_sequence(self, dna_matrix: np.ndarray, mutant_patterns: list, human_patterns: list) -> bool:

        for row in dna_matrix:
            if self._has_consecutive_letters(row, mutant_patterns, human_patterns):
                return True
        return False

    def _has_vertical_sequence(self, dna_matrix: np.ndarray, mutant_patterns: list, human_patterns: list) -> bool:

        for col in dna_matrix.T:
            if self._has_consecutive_letters(col, mutant_patterns, human_patterns):
                return True
        return False

    def _has_diagonal_sequence(self, dna_matrix: np.ndarray, mutant_patterns: list, human_patterns: list) -> bool:

        for offset in range(-dna_matrix.shape[0] + 4, dna_matrix.shape[1] - 3):
            diag = dna_matrix.diagonal(offset)
            if len(diag) >= 4 and self._has_consecutive_letters(diag, mutant_patterns, human_patterns):
                return True
        return False

    def _has_antidiagonal_sequence(self, dna_matrix: np.ndarray, mutant_patterns:list, human_patterns:list) -> bool:

        flip_matrix = np.fliplr(dna_matrix)
        for offset in range(-flip_matrix.shape[0] + 4, flip_matrix.shape[1] - 3):
            antidiag = flip_matrix.diagonal(offset)
            if len(antidiag) >= 4 and self._has_consecutive_letters(antidiag, mutant_patterns, human_patterns):
                return True
        return False

    def _has_consecutive_letters(self, sequence: np.ndarray, mutant_patterns: list, human_patterns: list) -> bool:

        count = 1
        for i in range(1, len(sequence)):
            if sequence[i] == sequence[i-1]:
                count += 1
                if count == self.mutant_sequence_length:
                    mutant_patterns.append(sequence[i] * self.mutant_sequence_length)
                    return True
            else:
                if count > 1:
                    human_patterns.append(sequence[i-1] * count)
                count = 1
        return False
