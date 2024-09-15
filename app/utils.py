import pandas as pd
import great_expectations as ge
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def validate_raw_data(df):
    df_ge = ge.from_pandas(df)
    # Definir suas expectativas aqui
    # Exemplo:
    df_ge.expect_column_values_to_not_be_null('field1')
    df_ge.expect_column_values_to_be_between('field2', min_value=0, max_value=100)
    results = df_ge.validate()
    return results.success


def enrich_data(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Enriqueça o seguinte texto: {text}",
        max_tokens=150
    )
    enriched_text = response.choices[0].text.strip()
    return enriched_text
