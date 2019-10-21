# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import Dict, List
import spacy
from spacy.language import Language


class SpacyExtractor:
    """class SpacyExtractor encapsulates logic to pipe Records with an id and text body
    through a spacy model and return entities separated by Entity Type
    """

    def __init__(
        self, nlp: Language, input_id_col: str = "id", input_text_col: str = "text"
    ):
        """Initialize the SpacyExtractor pipeline.
        
        nlp (spacy.language.Language): pre-loaded spacy language model
        input_text_col (str): property on each document to run the model on
        input_id_col (str): property on each document to correlate with request

        RETURNS (EntityRecognizer): The newly constructed object.
        """
        self.nlp = nlp
        self.input_id_col = input_id_col
        self.input_text_col = input_text_col

    def _name_to_id(self, text: str):
        """Utility function to do a messy normalization of an entity name

        text (str): text to create "id" from
        """
        return "-".join([s.lower() for s in text.split()])

    def extract_entities(self, records: List[Dict[str, str]]):
        """Apply the pre-trained model to a batch of records
        
        records (list): The list of "document" dictionaries each with an
            `id` and `text` property
        
        RETURNS (list): List of responses containing the id of 
            the correlating document and a list of entities.
        """
        ids = (doc[self.input_id_col] for doc in records)
        texts = (doc[self.input_text_col] for doc in records)

        res = []

        for doc_id, spacy_doc in zip(ids, self.nlp.pipe(texts)):
            entities = {}
            for ent in spacy_doc.ents:
                ent_id = ent.kb_id
                if not ent_id:
                    ent_id = ent.ent_id
                if not ent_id:
                    ent_id = self._name_to_id(ent.text)

                if ent_id not in entities:
                    if ent.text.lower() == ent.text:
                        ent_name = ent.text.capitalize()
                    else:
                        ent_name = ent.text
                    entities[ent_id] = {
                        "name": ent_name,
                        "label": ent.label_,
                        "matches": [],
                    }
                entities[ent_id]["matches"].append(
                    {"start": ent.start_char, "end": ent.end_char, "text": ent.text}
                )

            res.append({"id": doc_id, "entities": list(entities.values())})
        return res
