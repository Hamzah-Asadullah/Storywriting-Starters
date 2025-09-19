---
license: mit
task_categories:
- text-generation
language:
- en
tags:
- creative
- writing
- storywriting
- rp
- roleplay
- synthetic
size_categories:
- 1K<n<10K
---

> [!NOTE]
> Creating a pipeline to synthesize this dataset to reasonable quality took quite some effort, money and time.  
> If you use this dataset, please consider liking this repo to show your appreciation.

```
8,192 samples of "first-message" stuff, mainly designed for storywriting/roleplay/similar.

Here's how I created this dataset:
- Wrote a small Python script which resends the same input using a temperature of 1.1 and other sampling settings 8,192 times
  - Script saved under `first_messages.py`, took some time to tweak sampler settings to get somewhat diverse content
  - Results saved under `first_messages.json` as a list of strings
- Downloaded KoboldCPP for easily creating a compatible OpenAI-ish endpoint for the script
- Downloaded LLaMA3.1-8B-Q4 and inferenced on a RTX4060 8GB (6GB used) and let the script run for around 24h
- Created this repo, wrote a README.md, and uploaded the results under the MIT license.

Indexing the dataset is simple using any language, here's an example using Python:
---
from json import loads
with open("first_messages.json", 'r') as r:
  data: list[str] = loads(r.read())

for x in range(len(data)):
  print(f">> {x}th first message:\n---")
  print(data[x])
  input("---\n>_ Press enter to see next index.")
---

Happy coding.
```