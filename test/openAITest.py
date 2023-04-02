import os
import openai
openai.organization = "org-e6l56c2p8LLHLlJmj40gA4xh"
openai.api_key = os.getenv("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")
openai.Model.list()