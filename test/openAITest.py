import os
import openai
openai.organization = "org-e6l56c2p8LLHLlJmj40gA4xh"
openai.api_key = os.getenv("")
openai.Model.list()