
#!/usr/bin/env python3
# Copyright (c) 2025 Joseph Meyer. All Rights Reserved.


import torch
from torch import log, sqrt
from torch.nn.functional import l1_loss as mae
from torch.nn.functional import mse_loss as mse


class EmbeddingsAssessor:
    """Helper class for train_audio_novelifier."""

    def __init__(self, instability_tolerance: float = 1.2):
        assert instability_tolerance > 0
        self.instability_tolerance = instability_tolerance

    def assess_transformed_embeddings(
            self,
            embeddings_transformed: torch.Tensor,  # to assess
            embeddings_transformed_prime: torch.Tensor,  # decoded to audio and back to latent space
            embeddings_original: torch.Tensor,  # embeddings before transformation
            embeddings_ref: torch.Tensor,  # reference embeddings of other audio data
            embeddings_ref_transformed: torch.Tensor,  # e.g. novelified reference embeddings
            embeddings_silence: torch.Tensor,  # projection of silence into latent space
    ):
        embeddings_transformed_formatted = embeddings_transformed.transpose(0, 1).expand(1, -1, -1)

        novelty = self.assess_novelty(embeddings_transformed=embeddings_transformed, embeddings_ref=embeddings_ref) + self.assess_novelty(embeddings_transformed=abs(embeddings_transformed), embeddings_ref=abs(embeddings_ref))
        diversity = self.assess_diversity(embeddings_transformed=embeddings_transformed, embeddings_ref_transformed=embeddings_ref_transformed) + self.assess_diversity(embeddings_transformed=abs(embeddings_transformed), embeddings_ref_transformed=abs(embeddings_ref_transformed))
        transformation_depth = self.assess_transformation_depth(embeddings_transformed=embeddings_transformed, embeddings_original=embeddings_original) + self.assess_transformation_depth(embeddings_transformed=abs(embeddings_transformed), embeddings_original=abs(embeddings_original))
        nonsilence = self.assess_nonsilence(embeddings_transformed_formatted=embeddings_transformed_formatted, embeddings_silence=embeddings_silence) + self.assess_nonsilence(embeddings_transformed_formatted=abs(embeddings_transformed_formatted), embeddings_silence=abs(embeddings_silence))
        stability = self.assess_stability(embeddings_transformed_formatted=embeddings_transformed_formatted, embeddings_transformed_prime=embeddings_transformed_prime)

        reward = novelty + diversity + transformation_depth + nonsilence + stability
        return reward

    def assess_divergence(
        self,
        embeddings_original: torch.Tensor,
        embeddings_silence: torch.Tensor,
        embeddings_transformed: torch.Tensor,
        embeddings_transformed_prime: torch.Tensor,
        embeddings_ref: torch.Tensor,
        embeddings_ref_transformed: torch.Tensor,
    ) -> float:
        embeddings_transformed_formatted = embeddings_transformed.transpose(0, 1).expand(1, -1, -1)

        novelty = self.assess_novelty(embeddings_transformed=embeddings_transformed, embeddings_ref=embeddings_ref) + self.assess_novelty(embeddings_transformed=abs(embeddings_transformed), embeddings_ref=abs(embeddings_ref))
        diversity = self.assess_diversity(embeddings_transformed=embeddings_transformed, embeddings_ref_transformed=embeddings_ref_transformed) + self.assess_diversity(embeddings_transformed=abs(embeddings_transformed), embeddings_ref_transformed=abs(embeddings_ref_transformed))
        transformation_depth = self.assess_transformation_depth(embeddings_transformed=embeddings_transformed, embeddings_original=embeddings_original) + self.assess_transformation_depth(embeddings_transformed=abs(embeddings_transformed), embeddings_original=abs(embeddings_original))
        nonsilence = self.assess_nonsilence(embeddings_transformed_formatted=embeddings_transformed_formatted, embeddings_silence=embeddings_silence) + self.assess_nonsilence(embeddings_transformed_formatted=abs(embeddings_transformed_formatted), embeddings_silence=abs(embeddings_silence))
        return novelty + diversity + transformation_depth + nonsilence

    def assess_stability(
        self,
        embeddings_original: torch.Tensor,
        embeddings_silence: torch.Tensor,
        embeddings_transformed: torch.Tensor,
        embeddings_transformed_prime: torch.Tensor,
        embeddings_ref: torch.Tensor,
        embeddings_ref_transformed: torch.Tensor,
    ) -> float:
        embeddings_transformed_formatted = embeddings_transformed.transpose(0, 1).expand(1, -1, -1)
        return self.assess_stability(embeddings_transformed_formatted=embeddings_transformed_formatted, embeddings_transformed_prime=embeddings_transformed_prime)

    def assess_novelty(self, embeddings_transformed: torch.Tensor, embeddings_ref: torch.Tensor):
        return log(mae(embeddings_transformed, embeddings_ref) + 1) * self.instability_tolerance - 1 / (sqrt(mae(embeddings_transformed, embeddings_ref)) + 1)

    def assess_diversity(self, embeddings_transformed: torch.Tensor, embeddings_ref_transformed: torch.Tensor):
        return log(mae(embeddings_transformed, embeddings_ref_transformed) + 1) * self.instability_tolerance - 1 / (sqrt(mae(embeddings_transformed, embeddings_ref_transformed)) + 1)

    def assess_transformation_depth(self, embeddings_transformed: torch.Tensor, embeddings_original: torch.Tensor):
        return log(mae(embeddings_transformed, embeddings_original) + 1) * self.instability_tolerance - 1 / (sqrt(mae(embeddings_transformed, embeddings_original)) + 1)

    def assess_nonsilence(self, embeddings_transformed_formatted: torch.Tensor, embeddings_silence: torch.Tensor):
        return log(mae(embeddings_transformed_formatted, embeddings_silence) + 1) * self.instability_tolerance - 1 / (sqrt(mae(embeddings_transformed_formatted, embeddings_silence)) + 1)

    def assess_stability(self, embeddings_transformed_formatted: torch.Tensor, embeddings_transformed_prime: torch.Tensor):
        return -mse(embeddings_transformed_formatted, embeddings_transformed_prime)  # negative because we want higher to mean more consistent
