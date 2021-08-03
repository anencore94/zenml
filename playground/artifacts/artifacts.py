import pandas as pd

from playground.artifacts.base_artifact import BaseArtifact


# Artifact types

class DataArtifact(BaseArtifact):
    TYPE_NAME = 'data_artifact'

    def read(self):
        return pd.read_csv(self.uri)

    def write(self, df: pd.DataFrame):
        df.to_csv(self.uri)